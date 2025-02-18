configure-env:
	pyenv install 3.11.10
	pyenv local 3.11.10

install-dependencies-prod:
	pip install -r "./requirements/prod.txt"

install-dependencies-dev:
	pip install -r "./requirements/dev.txt"

run-dev:
	 python manage.py runserver