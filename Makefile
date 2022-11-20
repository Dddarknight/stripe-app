lint:
	poetry run flake8

install:
	pip install poetry
	poetry install

run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

test:
	poetry run python manage.py test