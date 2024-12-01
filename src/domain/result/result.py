from collections.abc import Iterable
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from src.domain.result.abstract_result import AbstractResult
from src.domain.result.abstract_result_with_value import AbstractResultWithValue
from src.domain.result.result_error import ResultError


@dataclass(frozen=True)
class Result:
    @staticmethod
    def success() -> 'VoidResult':
        return VoidResult(errors=[])

    @staticmethod
    def success_value[T](value: T) -> 'ValuableResult[T]':
        return ValuableResult[T](value=value, errors=[])

    @staticmethod
    def failure(error: ResultError) -> 'VoidFailedResult':
        return VoidFailedResult([error])

    @staticmethod
    def failure_errors(errors: Iterable[ResultError]) -> 'VoidFailedResult':
        return VoidFailedResult(errors)

    @staticmethod
    def failure_value[T](error: ResultError) -> 'ValuableFailedResult[T]':
        return ValuableFailedResult[T]([error], value=None)

    @staticmethod
    def failure_value_errors[T](errors: List[ResultError]) -> 'ValuableFailedResult[T]':
        return ValuableFailedResult[T](errors, value=None)


class ValuableResult[T](BaseModel, AbstractResultWithValue[T]):
    value: T
    errors: List[ResultError]

    def is_success(self) -> bool:
        return True

    def get_errors(self) -> Iterable[ResultError]:
        return []

    def get_value(self) -> T:
        return self.value


class ValuableFailedResult[T](BaseModel, AbstractResultWithValue[T]):
    value: T
    errors: List[ResultError]

    def is_success(self) -> bool:
        return False

    def get_errors(self) -> Iterable[ResultError]:
        return self.errors

    def get_value(self) -> T:
        raise ValueError("Getting value is not allowed for failed result.")


class VoidResult(BaseModel, AbstractResult):
    errors: List[ResultError]

    def is_success(self) -> bool:
        return True

    def get_errors(self) -> Iterable[ResultError]:
        return self.errors


class VoidFailedResult(BaseModel, AbstractResult):
    errors: List[ResultError]

    def is_success(self) -> bool:
        return False

    def get_errors(self) -> Iterable[ResultError]:
        return self.errors

