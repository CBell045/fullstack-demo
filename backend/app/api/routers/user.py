"""
User routes
"""

from fastapi import APIRouter
from app.api.deps.db import dbDep
from app.schemas.user import UserRead, UserCreate
from app.crud import user as user_crud

router = APIRouter()


### CREATE ###
@router.post("/", response_model=UserRead)
def create_user(db: dbDep, user: UserCreate):
    """
    Route to create a new user.
    """

    # Create the user in the database
    db_user = user_crud.create(db, user)

    # Return the user
    return db_user


### READ ###
# TODO: Implement get many users route


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: str, db: dbDep):
    """
    Route to get a user.
    """

    # Get the user from the database
    db_user = user_crud.get_one(db, user_id)

    # Return the user
    return db_user


### UPDATE ###
# TODO: Add update route


### DELETE ###
# TODO: Add delete route
