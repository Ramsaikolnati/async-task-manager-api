# app/models/__init__.py

from app.db import Base  # import Base from db.py

# Import models so Alembic sees them
from app.models.user import User
from app.models.task import Task

__all__ = ["Base", "User", "Task"]
