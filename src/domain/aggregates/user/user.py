from sqlalchemy import Column, String, UUID

from src.domain.aggregates.base import Base

class User(Base):
    __tablename__ = "t_user"

    oid = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=True)
