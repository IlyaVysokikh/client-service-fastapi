DC = docker compose
APP = docker_compose/app.yaml
RABBITMQ = docker_compose/rabbitmq.yaml
POSTGRESQL = docker_compose/postgresql.yaml
APP_SERVICE = main-app

.PHONY: app-dev
app-dev:
	${DC} -f ${APP} -f ${RABBITMQ} -f ${POSTGRESQL} up --build -d

.PHONY: app-dev-logs
app-dev-logs:
	${DC} -f ${APP} -f ${RABBITMQ} -f ${POSTGRESQL} logs -f

.PHONY: down-dev
down-dev:
	${DC} -f ${APP} -f ${RABBITMQ} -f ${POSTGRESQL} down

.PHONY: down
down:
	${DC} -f ${APP} -f ${RABBITMQ} -f ${POSTGRESQL} down

.PHONY: purge
purge:
	# Удаляем все данные, включая volumes
	${DC} -f ${APP} -f ${RABBITMQ} -f ${POSTGRESQL} down -v

.PHONY: shell
shell:
	${DC} -f ${APP} exec -it ${APP_SERVICE} bash

.PHONY: test
test:
	${DC} -f ${APP} exec ${APP_SERVICE} pytest
