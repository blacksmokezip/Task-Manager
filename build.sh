#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

poetry run python3 manage.py collectstatic --no-input
poetry run python3 manage.py makemigrations
poetry run python3 manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
  poetry run python3 manage.py createsuperuser --no-input
fi