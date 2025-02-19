configure-env:
	pyenv install 3.11.10
	pyenv local 3.11.10

install-dependencies-prod:
	pip install -r "./requirements/prod.txt"

install-dependencies-dev:
	pip install -r "./requirements/dev.txt"

run-dev:
	 ENVIRONMENT=.env python manage.py runserver

start-database:
	docker-compose up --detach

stop-database:
	docker-compose stop

generate-migrations:
	python manage.py makemigrations

apply-migrations:
	python manage.py migrate

test:
	pytest --cov . --cov-config=.coveragerc --cov-report term-missing
