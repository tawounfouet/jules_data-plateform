.PHONY: up down restart

COMPOSE_FILES=-f docker-compose.yml -f docker-compose.infra.yml -f docker-compose.lakehouse.yml -f docker-compose.orchestration.yml -f docker-compose.observability.yml

up:
	docker compose $(COMPOSE_FILES) up -d

down:
	docker compose $(COMPOSE_FILES) down -v

restart: down up

build:
	docker compose $(COMPOSE_FILES) build\n