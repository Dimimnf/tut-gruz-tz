from pydantic_settings import BaseSettings
from typing import Literal, Optional


class Settings(BaseSettings):
    MODE: Literal["DEV", "PROD", "TEST"]
    LOG_LEVEL: str = "INFO"

    BOT_TOKEN: str

    WEB_HOST: str
    WEB_BACK: str

    # Frontend variables (optional for bot)
    VITE_MODE: Optional[str] = "DEV"
    VITE_API: Optional[str] = None
    
    # Client variables (optional for bot)
    APP_HASH: Optional[str] = None
    APP_ID: Optional[str] = None
    PHONE_NUMBER: Optional[str] = None

    class Config:
        env_file = "../.env"
        extra = 'ignore'


settings = Settings()
