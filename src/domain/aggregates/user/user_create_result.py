import uuid
from dataclasses import dataclass

@dataclass
class UserCreateResult:
    success: bool
    user_oid: uuid.UUID