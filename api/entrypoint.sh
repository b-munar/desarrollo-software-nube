#!/bin/bash

sleep 5

python3 -m flask db init

sleep 5

python3 -m flask db migrate

sleep 5

python3 -m flask db upgrade

sleep 3

mkdir -p /home/celery/var/run/

sleep 5

# celery -A tasks.compress.celery worker -B -s /home/celery/var/run/celerybeat-schedule --detach

gunicorn --bind 0.0.0.0:5000 wsgi:app