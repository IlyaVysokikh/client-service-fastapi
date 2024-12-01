from functools import lru_cache

import punq

from src.application.auth.register_result_dto import RegisterResultDTO
from src.application.common.handling.Handler import Handler
from src.application.auth.register_command import RegisterCommand
from src.application.auth.register_command_handler import RegisterCommandHandler
from src.domain.aggregates.user.user_repository import UserRepository
from src.domain.events.message_producer import MessageProducer
from src.infrastructure.postgresql.Database import Database
from src.infrastructure.postgresql.repositories.user_repository import PostgreSQLUserRepository
from src.infrastructure.rabbitmq.RabbitMqConnectionFactory import RabbitMqConnectionFactory
from src.infrastructure.rabbitmq.rabbitmq_producer import RabbitMQProducer
from src.web.configs import Configs


@lru_cache(1)
def get_container() -> punq.Container:
    return _init_container()


def _init_container() -> punq.Container:
    container = punq.Container()

    container.register(
        Configs,
        scope=punq.Scope.singleton,
        instance=Configs()
    )
    configs: Configs = container.resolve(Configs)
    container.register(
        Database,
        scope=punq.Scope.singleton,
        factory=lambda: Database(
            url=configs.PG_CONNECTION_URI,
            ro_url=configs.PG_RO_CONNECTION_URI,
        ),
    )

    container.register(
        RabbitMqConnectionFactory,
        scope=punq.Scope.singleton,
        factory=lambda: RabbitMqConnectionFactory(
            host=configs.RABBITMQ_HOST,
            port=int(configs.RABBITMQ_PORT),
            user=configs.RABBITMQ_USER,
            password=configs.RABBITMQ_PASS
        ),
    )



    def init_user_repository() -> UserRepository:
        return PostgreSQLUserRepository(
            database=container.resolve(Database),
        )

    container.register(UserRepository, factory=init_user_repository, scope=punq.Scope.singleton)

    def init_producer() -> MessageProducer:
        return RabbitMQProducer(factory=container.resolve(RabbitMqConnectionFactory))

    def init_register_command_handler() -> Handler[RegisterCommand, RegisterResultDTO]:
        return RegisterCommandHandler(
            user_repository=container.resolve(UserRepository),
            producer=init_producer()
        )

    container.register(
        Handler[RegisterCommand, RegisterResultDTO],
        factory=init_register_command_handler,
        scope=punq.Scope.singleton
    )

    return container