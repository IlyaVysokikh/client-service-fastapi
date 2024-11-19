from functools import lru_cache

import punq

from src.application.common.handling.Handler import Handler
from src.application.user.register_command import RegisterCommand
from src.application.user.register_command_handler import RegisterCommandHandler
from src.domain.aggregates.user.register_result import RegisterResult
from src.domain.aggregates.user.user_repository import UserRepository
from src.infrastructure.postgresql.Database import Database
from src.infrastructure.postgresql.repositories.user_repository import PostgreSQLUserRepository
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

    def init_user_repository() -> UserRepository:
        return PostgreSQLUserRepository(
            database=container.resolve(Database),
        )

    container.register(UserRepository, factory=init_user_repository, scope=punq.Scope.singleton)

    def init_register_command_handler() -> Handler[RegisterCommand, RegisterResult]:
        return RegisterCommandHandler(
            user_repository=container.resolve(UserRepository)
        )

    container.register(
        Handler[RegisterCommand, RegisterResult],
        factory=init_register_command_handler,
        scope=punq.Scope.singleton
    )

    return container