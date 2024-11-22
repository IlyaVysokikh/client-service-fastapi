from abc import ABC, abstractmethod

from src.domain.result.abstract_result import AbstractResult


class AbstractResultWithValue[T](AbstractResult, ABC):

    @property
    @abstractmethod
    def value(self) -> T:
        pass