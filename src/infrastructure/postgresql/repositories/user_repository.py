from dataclasses import dataclass

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert
from typing_extensions import override

from src.domain.aggregates.user.register_result import RegisterResult
from src.domain.aggregates.user.user import User
from src.domain.aggregates.user.user_repository import UserRepository
from src.domain.result.abstract_result_with_value import AbstractResultWithValue
from src.domain.result.result import Result
from src.infrastructure.postgresql.Database import Database

@dataclass
class PostgreSQLUserRepository(UserRepository):
    database: Database

    @override
    async def create(
            self,
            name: str,
            last_name: str,
            email: str,
            password: str
    ) -> AbstractResultWithValue[RegisterResult]:
        with self.database.get_session() as session:
            stmt = (insert(User)
                    .values(name=name, last_name=last_name, email=email, password=password)
                    .returning(User.oid))

            result = await session.execute(stmt)
            created_oid = result.scalar_one_or_none()

            if created_oid:
                return Result.success_value(created_oid)

            # todo добавить ошибку
            return Result.failure_value()

    @override
    async def get_by_oid(self, oid: str) -> User | None:
        pass