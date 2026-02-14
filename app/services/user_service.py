from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.core.crypto import hash_password


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    async def register_user(
        self, db: AsyncSession, email: str, password: str
    ):
        existing = await self.repo.get_by_email(db, email)
        if existing:
            return existing

        hashed = hash_password(password)
        return await self.repo.create(db, email, hashed)
