"""
CRUD operations for User route
"""

from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models
from app.schemas.user import UserCreate


def create(db: Session, user: UserCreate) -> models.User:
    """
    Create a new user in the database.
    """

    db_user = models.User(**user.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_many(db: Session) -> Sequence[models.User]:
    """
    Get many users
    """

    stmt = select(models.User)
    db_users = db.scalars(stmt).all()

    return db_users


def get_one(db: Session, user_id: int) -> models.User:
    """
    Get a user by ID.
    """

    db_user = db.get(models.User, user_id)

    if not db_user:
        raise ValueError("User not found")

    return db_user
