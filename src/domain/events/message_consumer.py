from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True, eq=False)
class MessageConsumer(ABC):

    @abstractmethod
    def consume(self, topic: str, callback: Callable) -> None:
        pass