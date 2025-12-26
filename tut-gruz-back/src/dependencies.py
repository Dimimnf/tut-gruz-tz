from fastapi import Header, HTTPException

from aiogram.utils.web_app import safe_parse_webapp_init_data
from src.config import settings

async def verify_user(x_init_data: str = Header(..., alias="X-Init-Data")):
    """
    Dependency to verify X-Init-Data header.
    Verification logic to be implemented by user.
    """
    if not x_init_data:
        raise HTTPException(status_code=400, detail="X-Init-Data header is missing")
    if settings.MODE == "DEV":
        return x_init_data
    res = safe_parse_webapp_init_data(settings.BOT_TOKEN, x_init_data)
    return res
