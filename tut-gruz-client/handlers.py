"""
Обработчики событий
Логика обработки входящих сообщений и автоответа
"""
import time
from typing import Dict
from telethon import events
from telethon.tl.types import User
from telethon.errors import FloodWaitError, RPCError
from logger import app_logger
from const import RESPONSE_COOLDOWN, WEBAPP_URL, TRIGGER_PHRASE, LOG_FILE

class MessageHandler:
    """Обработчик входящих сообщений"""
    
    def __init__(self, client):
        self.client = client
        self.logger = app_logger
        
        # Антиспам: словарь {user_id: timestamp последнего ответа}
        self.last_response_time: Dict[int, float] = {}
    
    def _is_bot(self, sender) -> bool:
        """Проверка, является ли отправитель ботом"""
        return isinstance(sender, User) and sender.bot
    
    def _is_channel_or_group(self, event) -> bool:
        """Проверка, является ли чат каналом или группой"""
        return event.is_channel or event.is_group
    
    async def _is_self(self, sender_id: int) -> bool:
        """Проверка, является ли отправитель самим пользователем"""
        me = await self.client.get_me()
        return sender_id == me.id
    
    def _check_cooldown(self, user_id: int) -> bool:
        """
        Проверка кулдауна для пользователя
        
        Args:
            user_id: ID пользователя
            
        Returns:
            bool: True если можно отправить ответ
        """
        current_time = time.time()
        last_time = self.last_response_time.get(user_id, 0)
        
        if current_time - last_time < RESPONSE_COOLDOWN:
            return False
        
        return True
    
    def _update_cooldown(self, user_id: int):
        """Обновление времени последнего ответа"""
        self.last_response_time[user_id] = time.time()
    
    async def handle_new_message(self, event: events.NewMessage.Event):
        """
        Обработка нового сообщения
        
        Args:
            event: Событие нового сообщения
        """
        try:
            # Получение информации об отправителе
            sender = await event.get_sender()
            message_text = event.message.text
            
            if not message_text:
                return
            
            # Фильтр 1: Проверка на бота
            if self._is_bot(sender):
                self.logger.debug(f"Игнорирую бота: {sender.username}")
                return
            
            # Фильтр 2: Проверка на канал/группу
            if self._is_channel_or_group(event):
                self.logger.debug("Игнорирую сообщение из канала/группы")
                return
            
            # Фильтр 3: Проверка на самого себя
            if await self._is_self(sender.id):
                self.logger.debug("Игнорирую собственное сообщение")
                return
            
            # Проверка на точное совпадение с триггерной фразой
            if message_text.strip() != TRIGGER_PHRASE:
                self.logger.debug(
                    f"Сообщение не соответствует триггеру: '{message_text}'"
                )
                return
            
            # Антиспам: проверка кулдауна
            if not self._check_cooldown(sender.id):
                self.logger.info(
                    f"Кулдаун активен для пользователя {sender.id} "
                    f"(@{sender.username})"
                )
                return
            
            # Отправка ответа
            await self._send_response(event, sender)
            
        except FloodWaitError as e:
            self.logger.warning(
                f"FloodWait: необходимо подождать {e.seconds} секунд"
            )
            # В продакшене здесь можно добавить автоматическое ожидание
            
        except RPCError as e:
            self.logger.error(f"RPC ошибка: {e}")
            
        except Exception as e:
            self.logger.error(f"Неожиданная ошибка при обработке сообщения: {e}")
    
    async def _send_response(self, event: events.NewMessage.Event, sender: User):
        """
        Отправка ответа пользователю
        
        Args:
            event: Событие сообщения
            sender: Отправитель
        """
        try:
            await event.respond(WEBAPP_URL)
            
            # Обновление кулдауна
            self._update_cooldown(sender.id)
            
            self.logger.info(
                f"Отправлен ответ пользователю {sender.id} "
                f"(@{sender.username or 'no_username'}): {WEBAPP_URL}"
            )
            
        except FloodWaitError as e:
            self.logger.error(
                f"FloodWait при отправке ответа: {e.seconds} секунд"
            )
            raise
            
        except RPCError as e:
            self.logger.error(f"RPC ошибка при отправке ответа: {e}")
            raise
            
        except Exception as e:
            self.logger.error(f"Ошибка отправки ответа: {e}")
            raise
    
    def register_handlers(self):
        """Регистрация обработчиков событий"""
        # Обработчик новых личных сообщений
        @self.client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
        async def new_message_handler(event):
            await self.handle_new_message(event)
        
        self.logger.info("Обработчики сообщений зарегистрированы")