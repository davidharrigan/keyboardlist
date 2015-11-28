#!/bin/sh
set -ev
cd api

docker-compose build
docker-compose up -d
