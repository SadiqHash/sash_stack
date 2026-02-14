from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError

from app.db.session import get_db
from app.core.security import decode_access_token


async def get_current_user_id(
    token: str,
    db: AsyncSession = Depends(get_db),
) -> int:
    try:
        payload = decode_access_token(token)
        return int(payload["sub"])
    except (JWTError, KeyError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
