# pydantic_settings reads .env file automatically
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # These variable names MUST match your .env file keys exactly
    APP_NAME: str = "SecureTaskManager"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"
    DATABASE_URL: str                    # reads from .env
    SECRET_KEY: str                      # reads from .env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    WEATHER_API_KEY: str = ""
    WEATHER_BASE_URL: str = "https://api.openweathermap.org/data/2.5"

    class Config:
        env_file = ".env"     # tells pydantic WHERE the .env file is

# lru_cache = run this function only ONCE ever
# so settings are loaded once, not on every request
@lru_cache()
def get_settings():
    return Settings()

# This is the object we import everywhere
settings = get_settings()