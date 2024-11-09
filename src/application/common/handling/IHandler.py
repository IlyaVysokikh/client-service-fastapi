from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class IHandler[TParameters, TResult](ABC):
    @abstractmethod
    def execute(self, parameters: TParameters) -> TResult:
        pass