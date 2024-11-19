import uuid
from dataclasses import dataclass

@dataclass
class RegisterResult:
    user_oid: uuid.UUID