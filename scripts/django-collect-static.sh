#!/bin/sh
set -ev
cd api

docker exec api_keyboardlist-api_1 python manage.py collectstatic --noinput
