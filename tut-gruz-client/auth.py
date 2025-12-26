"""
Слой авторизации
Управление подключением и авторизацией в Telegram
"""
from telethon import TelegramClient
from telethon.errors import (
    SessionPasswordNeededError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError
)
from config import settings
from logger import app_logger


class AuthManager:
    """Менеджер авторизации в Telegram"""
    
    def __init__(self):
        self.client = TelegramClient(
            'test.session',
            settings.APP_ID,
            settings.APP_HASH
        )
        self.logger = app_logger
    
    async def connect(self) -> bool:
        """
        Подключение к Telegram
        
        Returns:
            bool: True если успешно
        """
        try:
            await self.client.connect()
            self.logger.info("Подключение к Telegram установлено")
            return True
        except Exception as e:
            self.logger.error(f"Ошибка подключения: {e}")
            return False
    
    async def authorize(self) -> bool:
        """
        Авторизация пользователя
        
        Returns:
            bool: True если успешно авторизован
        """
        try:
            # Проверка существующей авторизации
            if await self.client.is_user_authorized():
                me = await self.client.get_me()
                self.logger.info(f"Уже авторизован как: {me.first_name} (@{me.username})")
                return True
            
            # Новая авторизация
            self.logger.info(f"Начало авторизации для {settings.PHONE_NUMBER}")
            
            # Отправка кода
            await self.client.send_code_request(settings.PHONE_NUMBER)
            self.logger.info("Код подтверждения отправлен")
            
            # Запрос кода у пользователя
            code = input('Введите код из Telegram: ')
            
            try:
                await self.client.sign_in(settings.PHONE_NUMBER, code)
                
            except SessionPasswordNeededError:
                # Если установлена двухфакторная аутентификация
                self.logger.info("Требуется пароль 2FA")
                password = input('Введите пароль 2FA: ')
                await self.client.sign_in(password=password)
            
            me = await self.client.get_me()
            self.logger.info(f"Успешная авторизация: {me.first_name} (@{me.username})")
            return True
            
        except PhoneCodeInvalidError:
            self.logger.error("Неверный код подтверждения")
            return False
        except PhoneNumberInvalidError:
            self.logger.error("Неверный номер телефона")
            return False
        except Exception as e:
            self.logger.error(f"Ошибка авторизации: {e}")
            return False
    
    async def disconnect(self):
        """Отключение от Telegram"""
        try:
            await self.client.disconnect()
            self.logger.info("Отключение от Telegram")
        except Exception as e:
            self.logger.error(f"Ошибка при отключении: {e}")
    
    def get_client(self) -> TelegramClient:
        """
        Получение клиента Telegram
        
        Returns:
            TelegramClient: Клиент для работы с API
        """
        return self.client