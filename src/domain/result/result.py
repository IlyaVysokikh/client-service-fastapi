from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.result.result_error import ResultError


@dataclass
class Result(ABC):

    @property
    @abstractmethod
    def success(self) -> bool:
        pass

    @property
    @abstractmethod
    def errors(self) -> list[ResultError]:
        pass