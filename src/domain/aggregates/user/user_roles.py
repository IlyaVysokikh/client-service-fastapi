from enum import StrEnum


class UserRoles(StrEnum):
    student: str = "student"
    teacher: str = "teacher"
    expert: str = "expert"
    admin: str = "admin"
