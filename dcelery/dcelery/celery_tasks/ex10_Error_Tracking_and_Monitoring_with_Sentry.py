from dcelery.celery_config import app
from sentry_sdk import capture_exception

@app.task(queue="tasks")
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        raise e