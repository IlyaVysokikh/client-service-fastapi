import uuid

from src.application.common.base_dto import BaseDTO


class RegisterResultDTO(BaseDTO):
    oid: uuid.UUID | None