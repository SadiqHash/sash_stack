from fastapi import FastAPI
from app.api.routes import auth, users
from app.core.logging import configure_logging
from app.core.config import settings

configure_logging()

app = FastAPI(
    title=sash_stack,
    version="0.1.0",
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])


@app.get("/health", tags=["system"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
