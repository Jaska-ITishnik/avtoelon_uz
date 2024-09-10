mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

super:
	python3 manage.py createsuperuser

coverage:
	pytest --cov-report html --cov .

check:
	isort .
	flake8 .

build_index:
	python manage.py search_index --rebuild