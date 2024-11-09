from dataclasses import dataclass


@dataclass
class ResultError:
    key: str
    reason: str