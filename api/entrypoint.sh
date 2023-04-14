#!/bin/bash

python3 -m flask db init

python3 -m flask db migrate

python3 -m flask db upgrade

mkdir -p /home/celery/var/run/

celery -A tasks worker -B -s /home/celery/var/run/celerybeat-schedule --detach

python -m flask run --host=0.0.0.0