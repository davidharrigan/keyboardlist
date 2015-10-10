all: init
init: up migrate mine_all export_all


# API
up:
	cd api && docker-compose up -d
migrate: 
	cd api && docker-compose run --rm keyboardlist-api python manage.py migrate; \
	docker-compose run --rm keyboardlist-api python manage.py makemigrations


# Miner
mine_all: mine_mk
export_all: export_mk

# Start mining mechanicalkeyboards.com
mine_mk:
	cd miner && docker-compose run --rm miner mine mechanicalkeyboards.com

# Export data from mechanicalkeyboards.com
export_mk:
	cd miner && docker-compose run --rm miner export_data mechanicalkeyboards
