all: init
init: up migrate collect_static mine_all export_all

# -------------------------
# API Development Commands
# -------------------------
up:
	# Bring up API environment
	cd api && docker-compose up -d
restart:
	# Restart API process
	./scripts/restart-api.sh
collect_static:
	# Collect static files
	./scripts/django-collect-static.sh
migrate:
	# Migrate API DB
	cd api && docker-compose run --rm keyboardlist-api python manage.py migrate; \
	docker-compose run --rm keyboardlist-api python manage.py makemigrations
rebuild:
	# Rebuild API containers
	./scripts/rebuild-api.sh

# -------------------------
# UI Development Commands
# -------------------------
watch:
	cd api/keyboardlist-ui && gulp watch

# ---------------------------
# Miner Development Commands
# ---------------------------
mine_all: mine_mk
export_all: export_mk

# Start mining mechanicalkeyboards.com
mine_mk:
	cd miner && docker-compose run --rm miner mine mechanicalkeyboards.com

# Export data from mechanicalkeyboards.com. Exporting data triggers request
# to /ingestion/ endpoint of the API to dump miner data into API database
export_mk:
	cd miner && docker-compose run --rm miner export_data mechanicalkeyboards
