from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.aggregates.user.user import User
from src.domain.aggregates.user.user_create_result import UserCreateResult


@dataclass
class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> UserCreateResult:
        pass

    @abstractmethod
    async def get_by_oid(self, oid: str) -> User | None:
        pass

