"""
Настройка логирования
Логирование в файл и консоль с разными уровнями
"""
import logging
import sys
from const import LOG_FILE

def setup_logger(name: str = 'telegram_client') -> logging.Logger:
    """
    Настройка логгера с выводом в файл и консоль
    
    Args:
        name: Имя логгера
        
    Returns:
        logging.Logger: Настроенный логгер
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Форматирование
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Хэндлер для файла
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    
    # Хэндлер для консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    # Добавление хэндлеров
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


# Глобальный логгер
app_logger = setup_logger()