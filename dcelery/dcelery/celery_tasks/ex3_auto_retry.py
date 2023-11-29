import logging
from celery import Task
from dcelery.celery_config import app

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection error ocurred... - Admin Notified')
        else:
            print('{0!r} failed: {1!r}'.format(task_id, exc))
            #Perform additional error handling actions if needed

app.Task = CustomTask

@app.task(
        queue='tasks', 
        autoretry_for=(ConnectionError,), 
        default_retry_delay=5,
        retry_kwargs={'max_retries': 5}
        )
def my_task():
    raise ConnectionError("Connection error ocurred...")
    return