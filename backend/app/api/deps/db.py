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

    with Session(engine) as db:
        yield db


dbDep = Annotated[Session, Depends(get_db)]  # pylint: disable=invalid-name
