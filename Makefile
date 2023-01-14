IMAGE_TAG ?= latest
NETWORK_NAME ?= upgradeNET
NETWORK_TYPE ?= bridge


.PHONY: create_network deploy_wicked_service deploy_database_service deploy_pgadmin_service
all: create_network deploy_wicked_service deploy_database_service deploy_pgadmin_service


deploy_wicked_service: ## build and run the database service
	docker rm -f wicked_service || true \
	&& docker build -t wicked_service . --no-cache \
	&& docker run -d --network $(NETWORK_NAME) --restart=always -p 3115:3115 --name wicked_service wicked_service \
	&& docker image prune --force


deploy_database_service: ## build and run the database service
	docker rm -f database_service || true \
	&& docker build -t database_service ./Database --no-cache \
	&& docker run -d --network $(NETWORK_NAME) --restart=always -p 5432:5432 --name database_service database_service \
	&& docker image prune --force


deploy_pgadmin_service: ## build and run the pgadmin service
	docker rm -f pgadmin_service || true \
	&& docker run -d --network $(NETWORK_NAME) --restart=always -p 3500:80 \
	-e PGADMIN_DEFAULT_EMAIL=gueridaweb@gmail.com \
	-e PGADMIN_DEFAULT_PASSWORD=sercretArea51 \
	-e PGADMIN_LISTEN_PORT=80 \
	--name pgadmin_service dpage/pgadmin4:latest \
	&& docker image prune --force
