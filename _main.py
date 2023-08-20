from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from redis import Redis
from redis.lock import Lock as RedisLock

from src.tasks import task

redis_instance = Redis.from_url(task.redis_url)
lock = RedisLock(redis_instance, name='task_id')

REDIS_TASK_KEY = 'current_task'

app = FastAPI()


class TaskOut(BaseModel):
    id: str
    status: str
    result: str | None = None


@app.get('/start')
def start() -> TaskOut:
    try:
        if not lock.acquire(blocking_timeout=4):
            raise HTTPException(status_code=500, detail='Could not acquire lock')

        task_id = redis_instance.get(REDIS_TASK_KEY)
        if task_id is None or task.app.AsyncResult(task_id).ready():
            # no task was evert run, or the last task finished already
            r = task.dummy_task.delay()
            redis_instance.set(REDIS_TASK_KEY, r.task_id)
            return _to_task_out(r)

        else:
            raise HTTPException(status_code=400, detail='A task is already executed')

    finally:
        lock.release()


@app.get('/status')
def status(task_id: str = None) -> TaskOut:
    task_id = task_id or redis_instance.get(REDIS_TASK_KEY)
    if task_id is None:
        raise HTTPException(
            status_code=400, detail=f'Could not determine task {task_id}'
        )
    r = task.app.AsyncResult(task_id)
    return _to_task_out(r)



def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(
        id=r.task_id, 
        status=r.status,
        result=r.traceback if r.failed() else r.result
    )
