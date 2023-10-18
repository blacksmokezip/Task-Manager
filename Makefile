start:
	poetry run gunicorn task_manager.wsgi:application

install:
	poetry install

build:
	./build.sh

lint:
	poetry run flake8 task_manager