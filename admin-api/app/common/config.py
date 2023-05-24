from pydantic import BaseSettings
from app.common.constants import Environment


class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'


class Settings(BaseSettings):
    class Config(Config):
        pass

    CORS_ORIGINS: list[str]
    CORS_HEADERS: list[str]

    ENVIRONMENT: Environment = Environment.LOCAL


class AuthConfig(BaseSettings):
    class Config(Config):
        pass

    JWT_ALG: str
    JWT_SECRET: str
    JWT_EXP: int = 5  # minutes

    REFRESH_TOKEN_KEY: str = "refreshToken"
    REFRESH_TOKEN_EXP: int = 60 * 60 * 24 * 21  # 21 days

    SECURE_COOKIES: bool = True


settings = Settings()
auth_config = AuthConfig()
