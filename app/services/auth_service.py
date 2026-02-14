from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repository import UserRepository
from app.core.crypto import verify_password
from app.core.security import create_access_token


class AuthService:

    def __init__(self):
        self.repo = UserRepository()

    async def authenticate(
        self, db: AsyncSession, email: str, password: str
    ) -> str | None:
        user = await self.repo.get_by_email(db, email)
        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return create_access_token(str(user.id))
