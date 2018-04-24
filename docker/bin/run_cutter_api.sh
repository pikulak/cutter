#!/usr/bin/env bash
# wait until postgres up
/wait-for-it.sh postgres:5432 -t 0

cd cutter
python manage.py makemigrations cutter_api
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
