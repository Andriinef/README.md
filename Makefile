shell:
	pipenv shell
lock:
	pipenv lock
sync:
	pipenv sync --dev
update:
	pipenv update
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
	docker-compose exec app python src/manage.py collectstatic
docmag:
	docker-compose exec app python src/manage.py makemigrations
docmig:
	docker-compose exec app python src/manage.py migrate
docsup:
	docker-compose exec app python src/manage.py createsuperuser
docapp:
	docker-compose exec app python src/manage.py startapp
doctest:
	docker-compose exec app python src/manage.py test
reload:
	uvicorn main:app --reload
gun:
	gunicorn src.config.wsgi:application --bind
cq:
	flake8 ./ && black ./ && isort ./ && mypy ./
