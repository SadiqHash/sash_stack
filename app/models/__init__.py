"""
SQLAlchemy models registry.
Import all models here to ensure metadata binding.
"""

from app.models.user import User

__all__ = ["User"]
