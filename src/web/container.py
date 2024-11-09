from functools import lru_cache

import punq

from src.infrastructure.postgresql.Database import Database
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


    return container