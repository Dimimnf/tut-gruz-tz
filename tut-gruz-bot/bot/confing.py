from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    MODE: Literal["DEV", "PROD", "TEST"]
    LOG_LEVEL: str = "INFO"

    BOT_TOKEN: str

    WEB_HOST: str
    WEB_BACK: str

    VITE_MODE: str
    VITE_API: str
    APP_HASH: str
    APP_ID: str
    PHONE_NUMBER: str

    class Config:
        env_file = "../.env"


settings = Settings()
