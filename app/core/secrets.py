from app.core.config import settings


def get_secret_key() -> str:
    return settings.secret_key
