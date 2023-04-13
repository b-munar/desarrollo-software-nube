from celery import Celery
from config import Config

app = Celery('tasks', backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL )

@app.task
def add(x, y):
    return x + y
