#!/bin/bash

#celery -A tasks.compress.celery worker -B -s /home/celery/var/run/celerybeat-schedule --detach

# poetry run python -m flask run --host=0.0.0.0 --port=4000

poetry run gunicorn --bind 0.0.0.0:5000 wsgi:app