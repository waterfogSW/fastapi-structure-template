from pydantic import BaseSettings
from app.common.constants import Environment


class Settings(BaseSettings):
    CORS_ORIGINS: list[str]
    CORS_HEADERS: list[str]

    ENVIRONMENT: Environment = Environment.LOCAL

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
