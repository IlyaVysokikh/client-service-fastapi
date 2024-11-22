from collections.abc import Iterable
from dataclasses import dataclass
from typing import List

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
        return ValuableResult(value=value, errors=[])

    @staticmethod
    def failure(error: ResultError) -> 'VoidFailedResult':
        return VoidFailedResult([error])

    @staticmethod
    def failure_errors(errors: Iterable[ResultError]) -> 'VoidFailedResult':
        return VoidFailedResult(errors)

    @staticmethod
    def failure_value[T](error: ResultError) -> 'ValuableFailedResult[T]':
        return ValuableFailedResult([error], value=None)

    @staticmethod
    def failure_value_errors[T](errors: List[ResultError]) -> 'ValuableFailedResult[T]':
        return ValuableFailedResult(errors, value=None)


@dataclass
class ValuableResult[T](AbstractResultWithValue[T]):
    errors: Iterable[ResultError]
    value: T

    def is_succeeded(self) -> bool:
        return True

    def errors(self) -> Iterable[ResultError]:
        return []

    def value(self) -> T:
        return self.value


@dataclass(eq=False)
class ValuableFailedResult[T](AbstractResultWithValue[T]):
    errors: Iterable[ResultError]
    value: T

    def is_succeeded(self) -> bool:
        return False

    def errors(self) -> Iterable[ResultError]:
        return self.errors

    def value(self) -> T:
        raise ValueError("Getting value is not allowed for failed result.")


@dataclass
class VoidResult(AbstractResult):
    errors: Iterable[ResultError]

    def is_succeeded(self) -> bool:
        return True

    def errors(self) -> Iterable[ResultError]:
        return self.errors


@dataclass
class VoidFailedResult(AbstractResult):
    errors: Iterable[ResultError]

    def is_succeeded(self) -> bool:
        return False

    def errors(self) -> Iterable[ResultError]:
        return self.errors

