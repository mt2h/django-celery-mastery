import sys
from dcelery.celery_config import app

@app.task(queue="tasks")
def long_running_task():
    raise ValueError("Something went wrong")

@app.task(queue="tasks")
def process_task_result(result):
    sys.stdout.write("Processs task results")
    sys.stdout.flush()

@app.task(queue="tasks")
def error_handler(task_id, exc, traceback):
    sys.stdout.write(">>>>")
    sys.stdout.write(str(exc))
    sys.stdout.write(">>>>")
    sys.stdout.flush()

def run_task():
    long_running_task.apply_async(link=[process_task_result.s(),], link_error=[error_handler.s(),])