#!/bin/bash
set -e

cmd=$1
params=${@:2}

function mine {
  cd /miner && scrapy crawl $@
}

function dump {
  cd /miner && python -m dumper.$@
}

case "$cmd" in
  mine)
    mine $params
    ;;
  export_data)
    dump $params
    ;;
  *)
    echo "Unknown command: $cmd."
    ;;
esac
