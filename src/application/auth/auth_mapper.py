import uuid

from src.application.auth.register_result_dto import RegisterResultDTO
from src.domain.result.abstract_result_with_value import AbstractResultWithValue


class AuthMapper:

    @staticmethod
    def to_register_result_dto(result: AbstractResultWithValue[uuid.UUID]) -> RegisterResultDTO:
        return RegisterResultDTO(
            success=result.is_success(),
            oid=result.get_value(),
            errors=result.get_errors(),
        )