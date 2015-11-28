#!/bin/bash

if [ "$1" = 'build' ] || [ -z "$1" ]; then
  cd $WORKDIR
  ./node_modules/gulp/bin/gulp.js
fi

$@
