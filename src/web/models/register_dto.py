from pydantic import BaseModel

from src.application.user.register_command import RegisterCommand


class RegisterDto(BaseModel):
    name: str
    last_name: str
    email: str
    password: str

    def to_command(self) -> RegisterCommand:
        return RegisterCommand(
            name=self.name,
            last_name=self.last_name,
            email=self.email,
            password=self.password
        )