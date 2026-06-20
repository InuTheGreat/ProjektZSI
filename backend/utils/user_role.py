from enum import Enum


class UserRole(str, Enum):
    STANDARD = "STANDARD"
    ADMINISTRATOR = "ADMINISTRATOR"