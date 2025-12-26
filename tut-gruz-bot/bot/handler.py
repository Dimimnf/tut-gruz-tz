from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo

from bot.confing import settings

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Открыть каталог",
                    web_app=WebAppInfo(url=settings.WEB_HOST + "/catalog-containers"),
                )
            ]
        ]
    )

    await message.answer(
        text="Привет! Нажми на кнопку ниже, чтобы открыть каталог.", reply_markup=markup
    )
