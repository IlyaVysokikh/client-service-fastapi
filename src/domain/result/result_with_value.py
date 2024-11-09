from abc import abstractmethod
from dataclasses import dataclass

from src.domain.result.result import Result


@dataclass
class ResultWithValue[T](Result):

    @property
    @abstractmethod
    def value(self) -> T:
        pass
