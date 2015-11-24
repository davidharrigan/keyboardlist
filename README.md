[![Build Status](https://travis-ci.org/davidharrigan/keyboardlist.svg?branch=master)](https://travis-ci.org/davidharrigan/keyboardlist)

# keyboardlist

## Development
Dependencies: docker, docker-compose

**keyboardlist API**
```
# Bring up API environment
make up

# Restart API uWSGI
make restart

# DB migration
make migrate
```

**miner**
```
# Start mining all sites (currently only mechanicalkeyboards.com
mine_all

# Dump data into keyboardlist API
export_all
```

## TODOs
- less hard-coded stuff for automation
- static file management
- unittests for api endpoints
- frontend automation
