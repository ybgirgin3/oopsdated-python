from celery.app import Celery
from time import sleep
from datetime import datetime
import os


# config
redis_url = os.getenv('REDIS_URL', 'redis://default:redispw@localhost:32768')
app = Celery(__name__, broker=redis_url, backend=redis_url)



@app.task
def dummy_task(name='bekocan') -> str:
    # return open('tmp/celery/x.txt', 'w')

    # sleep(5)
    # return f'hello {name}'


    folder = '/tmp/celery'
    os.makedirs(folder, exist_ok=True)
    sleep(5)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%s")
    with open(f'{folder}/task-{now}.txt', 'w') as f:
        f.write(f'hello {name}: {now}')
