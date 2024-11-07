"""
FastAPI main application file

This file is the entry point for the FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import api_router


# Initialize FastAPI application
app = FastAPI()


# CORS
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(api_router, prefix="/api")


# Root route
@app.get("/")
async def root():
    """
    Root route
    """

    return {"Hello": "World"}
