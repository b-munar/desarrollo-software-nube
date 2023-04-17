import zipfile
import tarfile
from models import File, Task
from tasks.make_celery import make_celery
from app import create_app
from db import db

flask_app = create_app()
celery = make_celery(flask_app)

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, queueing.s())

@celery.task()
def compress_zip(file_id):
    file_to_zip = File.query.filter(File.id == file_id).first() 
    with zipfile.ZipFile(f"{file_to_zip.dir}/{file_to_zip.name.split('.')[0]}.zip", 'w') as zip:
        zip.write(file_to_zip.path)
        task = Task.query.filter_by(file_id=file_id).first()
        task.status=True
        db.session.commit()
        
@celery.task()
def compress_targz(file_id):
    file_to_tar = File.query.filter(File.id == file_id).first() 
    with tarfile.open(f"{file_to_tar.dir}/{file_to_tar.name.split('.')[0]}.tar.gz", 'w:gz') as tar:
        tar.add(file_to_tar.path)
        task = Task.query.filter_by(file_id=file_id).first()
        task.status=True
        db.session.commit()

@celery.task()
def compress_tarbz2(file_id):
    file_to_tar = File.query.filter(File.id == file_id).first() 
    with tarfile.open(f"{file_to_tar.dir}/{file_to_tar.name.split('.')[0]}.tar.bz2", 'w:bz2') as tar:
        tar.add(file_to_tar.path)
        task = Task.query.filter_by(file_id=file_id).first()
        task.status=True
        db.session.commit()

@celery.task()
def queueing():
    for task_to_zip in Task.query.filter_by(status = False, type_task=1):
        compress_zip.delay(task_to_zip.file_id)
    for task_to_targz in Task.query.filter_by(status = False, type_task=2):
        compress_targz.delay(task_to_targz.file_id)
    for task_to_tarbz2 in Task.query.filter_by(status = False, type_task=3):
        compress_tarbz2.delay(task_to_tarbz2.file_id)
        
        
