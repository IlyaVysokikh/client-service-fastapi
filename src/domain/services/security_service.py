import bcrypt
from dataclasses import dataclass


@dataclass(frozen=True)
class SecurityService:

    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()

        return bcrypt.hashpw(password.encode(), salt).decode()

    @staticmethod
    def check_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())