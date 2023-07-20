SHELL = /bin/sh
DEVELOP_COMPOSE_FILE_PATH = "./docker/docker-compose.dev.yml"

# 🐳 Docker Compose
up: CMD=up
down: CMD=down

.PHONY: up down
up down:
	docker-compose -f $(DEVELOP_COMPOSE_FILE_PATH) $(CMD)
