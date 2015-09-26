#!/bin/bash
set -e

cmd=$1
params=${@:2}

function mine {
  cd /miner && ls -la && scrapy crawl $@
}

case "$cmd" in
  mine)
    mine $params
    ;;
  export_data)
    echo "Not Implemented"
    ;;
  help)
    man ./miner_man
    ;;
  *)
    echo "Unknown command: $cmd."
    echo "try help command to list available commands"
    ;;
esac

exec "$@"
