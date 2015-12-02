[![Build Status](https://travis-ci.org/davidharrigan/keyboardlist.svg?branch=master)](https://travis-ci.org/davidharrigan/keyboardlist)

# keyboardlist

## Development
Dependencies: docker, docker-compose

**update your /etc/hosts**
```
YOUR_DOCKER_HOST_IP keyboardlist-dev.com
```

**keyboardlist API**
```
# Bring up API environment
make up

# Restart API uWSGI
make restart

# DB migration
make migrate

# Collect static
make collect_static

# Rebuild API containers
make rebuild
```

**miner**
There's a good chance this will be broken at some point (whenever mechanicalkeyboards.com
decides to update their site).  This will be replaced sometime with list of keyboards
to dump straight into the database. We'll use updater to update inventory and prices.
```
# Start mining all sites (currently only mechanicalkeyboards.com
mine_all

# Dump data into keyboardlist API
export_all
```

### Get started
```
# Clone the repo
git clone git@github.com:davidharrigan/keyboardlist.git

# Build containers, migrate DB, collect static, mine keyboard websites, ingest data
make init
```

## TODOs
- ~~less hard-coded stuff for automation~~
- ~~static file management~~
- unittests for api endpoints
- frontend automation
- basic ui
- secret management
- inventory updater
