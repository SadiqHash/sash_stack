from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user_id
from app.db.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserRead

router = APIRouter()
repo = UserRepository()


@router.get("/me", response_model=UserRead)
async def read_current_user(
    user_id: int = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
):
    user = await repo.get_by_email(db, user_id)
    return user
