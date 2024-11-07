"""
Database models for the application.

Written with SQLAlchemy ORM.


General Notes:
- Use the Base class for all models.
"""

# pylint: disable=too-few-public-methods

from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    ForeignKey,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    mapped_column,
    relationship,
    declared_attr,
)
from sqlalchemy.types import Enum
from pydantic.alias_generators import to_snake
from .enums import PermissionEnum, UserRoleEnum


class Base(DeclarativeBase):
    """
    Base class for all models.

    This class sets the table name to the snake case version of the class name.
    See https://docs.sqlalchemy.org/en/20/orm/declarative_mixins.html
    """

    @declared_attr.directive
    def __tablename__(cls) -> Optional[str]:  # pylint: disable=no-self-argument
        return to_snake(cls.__name__)

    # This removes warning for func.now()
    # pylint: disable=not-callable

    # Set the default table args
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
    )


class User(Base):
    """
    User table

    Schema: app/schemas/user.py
    Route: app/api/routers/user.py
    """

    # Keys + Fields
    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[Optional[str]]
    role: Mapped[UserRoleEnum] = mapped_column(Enum(UserRoleEnum))

    # Relationships
    permissions: Mapped[List[Permission]] = relationship(
        back_populates="user",
    )


class Permission(Base):
    """
    Permission table

    Schema: app/schemas/permission.py
    Route: app/api/routers/permission.py
    """

    # Keys + Fields
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), primary_key=True)
    permission: Mapped[PermissionEnum] = mapped_column(
        Enum(PermissionEnum), primary_key=True
    )

    # Relationships
    user: Mapped[User] = relationship(
        back_populates="permissions",
    )
