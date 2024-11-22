import uuid

from sqlalchemy import Column, String, Enum, UUID

from src.domain.aggregates.base import Base
from src.domain.aggregates.user.user_errors import UserErrors
from src.domain.result.result_error import ResultError


class User(Base):
    __tablename__ = "t_user"

    oid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=True)
