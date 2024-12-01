from abc import ABC, abstractmethod

from src.domain.result.abstract_result import AbstractResult


class AbstractResultWithValue[T](AbstractResult, ABC):

    @abstractmethod
    def get_value(self) -> T:
        pass