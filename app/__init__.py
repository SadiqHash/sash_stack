"""
sash_stack application package.
Provides the main FastAPI app factory.
"""

from app.main import create_app

__all__ = ["create_app"]
