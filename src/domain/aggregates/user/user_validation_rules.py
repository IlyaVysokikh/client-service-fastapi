from enum import Enum


class UserValidationRules(Enum):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 50

    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 20