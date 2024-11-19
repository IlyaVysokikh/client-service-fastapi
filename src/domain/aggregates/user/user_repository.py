from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.aggregates.user.user import User
from src.domain.aggregates.user.register_result import RegisterResult
from src.domain.result.abstract_result_with_value import AbstractResultWithValue


@dataclass
class UserRepository(ABC):
    @abstractmethod
    async def create(
            self,
            name: str,
            last_name: str,
            email: str,
            password: str
    ) -> AbstractResultWithValue[RegisterResult]:
        pass

    @abstractmethod
    async def get_by_oid(self, oid: str) -> User | None:
        pass

