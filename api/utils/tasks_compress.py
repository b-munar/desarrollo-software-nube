import zipfile
from models import File, Task
from broker import make_celery
from app import create_app

flask_app = create_app()
celery = make_celery(flask_app)
# app = Celery('tasks', backend=Config.CELERY_RESULT_BACKEND, broker=Config.CELERY_BROKER_URL )

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(1.0, queueing.s())


@celery.task()
def compress_zip(file_id):
    file_to_zip = File.query.filter(File.id == file_id).first() 
    with zipfile.ZipFile(f"{file_to_zip.dir}/{file_to_zip.name.split('.')[0]}.zip", 'w') as zip:
        zip.write(file_to_zip.path)

@celery.task()
def queueing():
    for task_to_zip in Task.query.filter_by(status = False):
        compress_zip.delay(task_to_zip.file_id)
