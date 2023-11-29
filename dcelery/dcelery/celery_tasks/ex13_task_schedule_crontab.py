from datetime import timedelta
from celery.schedules import crontab
from dcelery.celery_config import app

#app.conf.beat_schedule = {
#    'task1':{
#        'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task1',
#        'schedule': crontab(minute='0-59/10', hour='0-5', day_of_week='mon'), #every 10 minutes between 00:00 and 05:59 on Mondays
#        'kwargs': {'foo': 'bar'},
#        'args': (1, 2),
#        'options': {
#            'queue':'tasks',
#            'priory':5,
#            }
#        },
#    'task2':{
#        'task': 'dcelery.celery_tasks.ex13_task_schedule_crontab.task2',
#        'schedule': timedelta(seconds=10),
#        }
#    }

@app.task(queue="tasks")
def task1(a, b, **kwargs):
    result = a + b
    print(f"Running task 1 - {result}")

@app.task(queue="tasks")
def task2():
    print("Running task 2")