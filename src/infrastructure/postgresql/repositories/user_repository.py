import uuid
import logging
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import insert
from typing_extensions import override

from src.domain.aggregates.user.user import User
from src.domain.aggregates.user.user_repository import UserRepository
from src.domain.result.abstract_result_with_value import AbstractResultWithValue
from src.domain.result.result import Result
from src.infrastructure.postgresql.Database import Database

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    ) -> AbstractResultWithValue[uuid.UUID]:
        async with self.database.get_session() as session:
            stmt = (insert(User)
                    .values(name=name, last_name=last_name, email=email)
                    .returning(User.oid))

            result = await session.execute(stmt)
            created_oid = result.scalar_one_or_none()

            if created_oid:
                return Result.success_value(created_oid)

            # Возврат ошибки, если идентификатор не был получен
            return Result.failure_value()

    @override
    async def get_by_oid(self, oid: str) -> User | None:
        pass
