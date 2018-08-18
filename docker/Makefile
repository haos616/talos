.ONESHELL:

init:
	echo COMPOSE_PROJECT_NAME=talos > .env
	echo COMPOSE_FILE=common.yml:dev.yml >> .env
	echo PROJECT_VERSION=dev >> .env
	echo PROJECT_NAME=auth >> .env
	echo HUB_HOST=hub.exampple.com >> .env

build:
	docker-compose -f habitus/docker-compose.yml run --rm habitus

build-live: build
	docker-compose -f habitus/docker-compose.yml run --rm habitus-live

build-habitus:
	docker-compose -f habitus/docker-compose.yml build

push-django:
	export COMPOSE_FILE=common.yml:live.yml:push.yml \
	&& docker-compose push django

push-nginx:
	export COMPOSE_FILE=common.yml:live.yml:push.yml \
	&& docker-compose push nginx

push-postgres:
	export COMPOSE_FILE=common.yml:live.yml:push.yml \
	&& docker-compose push postgres

push: push-django push-nginx push-postgres

config-live:
	export PROJECT_VERSION=`git describe --always` \
	&& export COMPOSE_FILE=common.yml:live.yml \
	&& docker-compose config
