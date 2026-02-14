from pydantic import BaseSettings, Field
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = Field(default="sash_stack")
    app_env: str = Field(default="development")

    database_url: str

    secret_key: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
