"""
User pydantic schemas
"""

from __future__ import annotations

from typing import Optional


from pydantic import EmailStr, Field
from app.models import UserRoleEnum

from ._base import BaseClass, USPhoneNumber


class UserBase(BaseClass):
    """
    User schema
    """

    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    phone: Optional[USPhoneNumber] = None
    role: UserRoleEnum


class User(UserBase):
    """User schema"""

    user_id: int


class UserRead(User):
    """User read schema"""

    # Relationships
    # TODO: Add permissions schema
    # permissions: List[Permission]


class UserCreate(UserBase):
    """User create schema"""


# TODO: Add user update schema
