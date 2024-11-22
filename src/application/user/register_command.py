from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class RegisterCommand:
    name: str
    last_name: str
    email: str
    password: str