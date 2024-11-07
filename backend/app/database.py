"""
Initializes the database connection
"""

from sqlalchemy import create_engine

# Create db engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
