# pipenv
# ---------------------------------
shell:
	pipenv shell
lock:
	pipenv lock
sync:
	pipenv sync --dev
update:
	pipenv update


# Docker & gunicorn
# ---------------------------------
build:
	docker build .
up:
	docker-compose up -d
psa:
	docker-compose ps -a
upb:
	docker-compose up -d --build
down:
	docker-compose down
docbuild:
	docker-compose build
doccol:
	docker-compose exec app python manage.py collectstatic
docmag:
	docker-compose exec app python manage.py makemigrations
docmig:
	docker-compose exec app python manage.py migrate
docsup:
	docker-compose exec app python manage.py createsuperuser
docapp:
	docker-compose exec app python manage.py startapp
doctest:
	docker-compose exec app python manage.py test

# ---------------------------------
reload:
	uvicorn main:app --reload
gun:
	gunicorn src.config.wsgi:application --bind


# ---------------------------------
cq:
	flake8 ./ && black ./ && isort ./ && mypy ./


# Django
# ---------------------------------
rs:
	python manage.py runserver

col:
	python manage.py collectstatic

mag:
	python manage.py makemigrations

mig:
	python manage.py migrate

sup:
	python manage.py createsuperuser

app:
	python manage.py startapp

hel:
	python manage.py help

test:
	python manage.py test
