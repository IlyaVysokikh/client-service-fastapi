from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class MessageProducer(ABC):

    @abstractmethod
    def produce(self, topic: str, message) -> None:
        pass