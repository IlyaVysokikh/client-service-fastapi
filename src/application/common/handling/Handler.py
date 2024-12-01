from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class Handler[TParameters, TResult](ABC):
    @abstractmethod
    async def execute(self, parameters: TParameters) -> TResult:
        pass