from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class RegisterCommand:
    name: str
    last_name: str
    email: str
    password: str

    def to_dict(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
        }