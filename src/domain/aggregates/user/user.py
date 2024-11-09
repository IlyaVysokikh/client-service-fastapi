import uuid
from dataclasses import dataclass

from src.domain.aggregates.user.user_errors import UserErrors
from src.domain.aggregates.user.sex import Sex
from src.domain.result.result_error import ResultError


@dataclass(eq=False)
class User:
    oid: uuid.UUID
    name: str
    last_name: str
    email: str
    phone: str
    sex: Sex

    MIN_NAME_LENGTH: int = 2

    def validate_name(self) -> ResultError | None:
        if self.name is None or len(self.name) > self.MIN_NAME_LENGTH:
            return UserErrors.too_short_name

    def validate_email(self) -> ResultError | None:
        pass

