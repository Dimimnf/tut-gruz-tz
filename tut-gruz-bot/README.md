# Telegram Бот для "Тут Груз"

Это Telegram бот, разработанный с использованием `aiogram` и Python 3.12+.
На данный момент он служит точкой входа для Web App приложения "Тут Груз".

## Функционал

- **/start**: Отправляет приветственное сообщение и кнопку для открытия каталога в Web App.

## Требования

- Python 3.12 или выше.
- Токен Telegram бота (получить у @BotFather).
- HTTPS URL для вашего Web App (необходим для работы кнопки WebApp).

## Установка

1.  **Клонируйте репозиторий** (если еще не сделали этого):
    ```bash
    git clone <url_репозитория>
    cd tut-gruz-bot
    ```

2.  **Создайте виртуальное окружение**:
    ```bash
    # Создание venv
    python -m venv .venv
    
    # Активация на Windows
    .venv\Scripts\activate
    
    # Активация на Linux/macOS
    source .venv/bin/activate
    ```

3.  **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    # Или если используете uv/poetry
    uv sync
    ```

## Настройка

1.  Создайте файл `.env` в корневой директории (на основе `.env.example`).
2.  Заполните необходимые переменные окружения:

    ```env
    MODE=DEV
    LOG_LEVEL=INFO
    BOT_TOKEN=ваш_токен_бота
    WEB_HOST=https://your-webapp-url.com
    WEB_BACK=https://your-backend-url.com
    ```

## Запуск бота

Запустите бота следующей командой из корневой директории:

```bash
python bot/main.py
```

## Структура проекта

- `bot/main.py`: Точка входа в бота. Инициализация и поллинг (polling).
- `bot/handler.py`: Содержит обработчики сообщений (например, `/start`).
- `bot/confing.py`: Управление конфигурацией с использованием Pydantic.
