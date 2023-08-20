from celery import Celery
from fastapi import FastAPI
import os

app = FastAPI()

# config
# redis_url = os.getenv('REDIS_URL', 'redis://default:redispw@localhost:32768')
celery = Celery(
    __name__, 
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@celery.task()
def divide(x, y):
    import time
    time.sleep(5)
    return x / y
