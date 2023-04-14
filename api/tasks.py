from celery import Celery
from config import Config

app = Celery('tasks', backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL )

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, queueing.s())

@app.task
def queueing(args):
    print(args)

@app.task
def add(x, y):
    return x + y