#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python python-project-52/manage.py collectstatic --no-input
python python-project-52/manage.py makemigrations
python python-project-52/manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  python python-project-52/manage.py createsuperuser --no-input
fi