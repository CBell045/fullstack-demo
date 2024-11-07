"""
Main API router.
"""

from fastapi import APIRouter
from .routers import user

api_router = APIRouter(responses={404: {"description": "Not found"}})

api_router.include_router(
    user.router,
    prefix="/user",
    tags=["user"],
)
