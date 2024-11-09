DC = docker compose
APP = docker_compose/app.yaml
# Убраны KAFKA и MONGO
APP_SERVICE = main-app
ENV = --env-file .env

.PHONY: app-dev
app-dev:
	${DC} -f ${APP} ${ENV} up --build -d

.PHONY: app-dev-logs
app-dev-logs:
	${DC} -f ${APP} logs -f

.PHONY: down-dev
down-dev:
	${DC} -f ${APP} ${ENV} down

.PHONY: down
down:
	${DC} -f ${APP} ${ENV} down

.PHONY: purge
purge:
	# Здесь тоже удалены все строки, связанные с Kafka, Mongo и Mongo Express
	${DC} -f ${ENV} down -v

.PHONY: shell
shell:
	${DC} -f ${APP} exec -it ${APP_SERVICE} bash

.PHONY: test
test:
	${DC} -f ${APP} exec ${APP_SERVICE} pytest
