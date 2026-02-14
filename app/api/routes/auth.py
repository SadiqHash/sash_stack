from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate
from app.schemas.auth import Token
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.db.session import get_db

router = APIRouter()

user_service = UserService()
auth_service = AuthService()


@router.post("/register", response_model=Token)
async def register(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user = await user_service.register_user(
        db, payload.email, payload.password
    )

    token = await auth_service.authenticate(
        db, payload.email, payload.password
    )

    return {"access_token": token}


@router.post("/login", response_model=Token)
async def login(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    token = await auth_service.authenticate(
        db, payload.email, payload.password
    )

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token}
