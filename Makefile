MANAGE := poetry run python3 manage.py

dev:
	poetry run python3 manage.py runserver

start:
	poetry run gunicorn task_manager.wsgi:application

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

install:
	poetry install

build:
	./build.sh

lint:
	poetry run flake8 task_manager

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

gettext:
	poetry run python3 manage.py makemessages -l ru

trans:
	poetry run python3 manage.py compilemessages

migrate:
	poetry run python3 manage.py makemigrations && poetry run python3 manage.py migrate