#!/bin/bash
cd $WORKDIR
if [ -z "$1" ]; then
  CMD=$CMD
else
  CMD=$1
fi

if [ "$CMD" = 'build' ] || [ -z "$CMD" ]; then
  ./node_modules/gulp/bin/gulp.js
fi

if [ "$CMD" = 'watch' ]; then
  ./node_modules/gulp/bin/gulp.js dev
fi

exec "$@";
