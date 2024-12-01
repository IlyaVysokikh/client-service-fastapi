from abc import ABC, abstractmethod


from src.domain.result.result_error import ResultError


class AbstractResult(ABC):

    @abstractmethod
    def is_success(self) -> bool:
        pass

    @abstractmethod
    def get_errors(self) -> list[ResultError]:
        pass