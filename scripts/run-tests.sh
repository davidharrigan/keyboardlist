#!/bin/sh
set -ev
cd api
docker-compose run --rm keyboardlist-api pep8 --exclude=migrations --ignore=E501 .
docker-compose run --rm keyboardlist-api python manage.py test --noinput -v 2
