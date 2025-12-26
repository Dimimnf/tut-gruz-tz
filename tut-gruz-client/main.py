"""
Главный модуль приложения
Точка входа и основной цикл работы клиента
"""
import asyncio
import signal
import sys
from const import RESPONSE_COOLDOWN, WEBAPP_URL, TRIGGER_PHRASE, LOG_FILE
from logger import app_logger
from auth import AuthManager
from handlers import MessageHandler


class TelegramAutoResponder:
    """Основной класс приложения"""
    
    def __init__(self):
        self.logger = app_logger
        self.auth_manager = AuthManager()
        self.is_running = False
    
    async def start(self):
        """Запуск приложения"""
        try:
            self.logger.info("=" * 60)
            self.logger.info("Запуск Telegram Auto Responder")
            self.logger.info("=" * 60)
            
            # Подключение
            if not await self.auth_manager.connect():
                self.logger.error("Не удалось подключиться к Telegram")
                return False
            
            # Авторизация
            if not await self.auth_manager.authorize():
                self.logger.error("Не удалось авторизоваться")
                await self.auth_manager.disconnect()
                return False
            
            # Регистрация обработчиков
            client = self.auth_manager.get_client()
            message_handler = MessageHandler(client)
            message_handler.register_handlers()
            
            self.is_running = True
            self.logger.info("=" * 60)
            self.logger.info("Клиент запущен и слушает сообщения...")
            self.logger.info(f"Триггерная фраза: '{TRIGGER_PHRASE}'")
            self.logger.info("Нажмите Ctrl+C для остановки")
            self.logger.info("=" * 60)
            
            # Основной цикл
            await client.run_until_disconnected()
            
            return True
            
        except KeyboardInterrupt:
            self.logger.info("\nПолучен сигнал прерывания")
            await self.stop()
            
        except Exception as e:
            self.logger.error(f"Критическая ошибка: {e}", exc_info=True)
            await self.stop()
            return False
    
    async def stop(self):
        """Остановка приложения"""
        if self.is_running:
            self.logger.info("Остановка клиента...")
            await self.auth_manager.disconnect()
            self.is_running = False
            self.logger.info("Клиент остановлен")


async def main():
    """Главная функция"""
    app = TelegramAutoResponder()
    
    # Обработка сигналов для graceful shutdown
    def signal_handler(signum, frame):
        app_logger.info(f"\nПолучен сигнал {signum}")
        asyncio.create_task(app.stop())
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Запуск приложения
    success = await app.start()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        app_logger.info("\nПриложение завершено пользователем")
    except Exception as e:
        app_logger.error(f"Неожиданная ошибка: {e}", exc_info=True)
        sys.exit(1)