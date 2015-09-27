#!/bin/sh
set -ev
cd api
docker-compose run keyboardlist-api pep8 --exclude=migrations --ignore=E501 .
docker-compose run --service-ports keyboardlist-api python manage.py makemigrations sellers keyboards
docker-compose run --service-ports keyboardlist-api python manage.py migrate
docker-compose run --service-ports keyboardlist-api python manage.py test --noinput