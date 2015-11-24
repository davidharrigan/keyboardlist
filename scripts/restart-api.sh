#!/bin/sh
set -ev
cd api

docker exec api_keyboardlist-api_1 uwsgi --reload /tmp/keyboardlist-api-master.pid;
