from pydantic import BaseModel

from src.domain.result.result_error import ResultError


class BaseDTO(BaseModel):
    success: bool
    message: str = ""
    errors: list[ResultError]