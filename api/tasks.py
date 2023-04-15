from celery import Celery
from config import Config
import zipfile, shutil, py7zr, tarfile
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

@app.task
def compress_zip():
    with zipfile.ZipFile('b.zip', 'w') as f:
        f.write('a.pdf')
        shutil.move('b.zip', 'path')
@app.task
def compress_7z():
    with py7zr.SevenZipFile('h.7z', 'w') as z:
        z.writeall('a.pdf')
        shutil.move('b.zip', 'path')\

@app.task
def compress_tar_gz():
    with tarfile.open('g.tar.gz', 'w:gz') as tar:
        tar.add('a.pdf')
        shutil.move('b.zip', 'path')\

@app.task
def compress_tar_gz():
    with tarfile.open('g.tar.bz2', 'w:bz2') as tar:
        tar.add('a.pdf')
        shutil.move('b.zip', 'path')

