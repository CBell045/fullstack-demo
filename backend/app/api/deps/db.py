"""
Database dependency
"""

from typing import Annotated

from fastapi import Depends

from sqlalchemy.orm import Session
from app.database import engine


#### Database dependency ####


def get_db():
    """
    Gets the database session
    """

    db = engine.connect()
    try:
        yield db
    finally:
        db.close()


dbDep = Annotated[Session, Depends(get_db)]  # pylint: disable=invalid-name
