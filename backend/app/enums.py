"""
Enums used in models and schemas.
"""

from enum import Enum


class UserRoleEnum(str, Enum):
    """
    UserRoleEnum class
    """

    ADMIN = "admin"
    PATIENT = "patient"
    DOCTOR = "doctor"


class PermissionEnum(str, Enum):
    """
    PermissionEnum class
    """

    # User permissions
    READ_USERS = "read:users"
    WRITE_USERS = "write:users"

    # Order permissions
    READ_ORDERS = "read:orders"
    WRITE_ORDERS = "write:orders"
