# Backend API for Tut Gruz

Это бэкенд-сервис для приложения Tut Gruz. Реализован на Python (FastAPI).

## Требования

- Python 3.12+
- Менеджер пакетов `uv` (рекомендуется) или `pip`

## Установка

1. Склонируйте репозиторий.
2. Перейдите в директорию бэкенда:
   ```bash
   cd tut-gruz-back
   ```
3. Создайте виртуальное окружение и установите зависимости:

   **С помощью uv:**
   ```bash
   uv sync
   ```

   **С помощью pip:**
   ```bash
   python -m venv .venv
   # Активация:
   # Windows: .venv\Scripts\activate
   # Linux/macOS: source .venv/bin/activate
   pip install -r requirements.txt
   ```
   *(Примечание: если `requirements.txt` отсутствует, используйте `pyproject.toml`)*

## Конфигурация (.env)

Проект ожидает файл `.env` на уровень выше корневой папки бэкенда (в корне репозитория `tut-gruz-tz`).

Пример переменных:
```ini
MODE=DEV  # или PROD, TEST
LOG_LEVEL=INFO

BOT_TOKEN=your_telegram_bot_token  # Токен от BotFather
WEB_HOST=http://localhost:5173     # Хост фронтенда
WEB_BACK=http://localhost:8000     # Хост бэкенда

# Дополнительные переменные (если используются)
VITE_MODE=development
VITE_API=http://localhost:8000
```

## Запуск

### Локальная разработка

```bash
python src/main.py
```
Или через uvicorn напрямую:
```bash
uvicorn src.main:app --reload
```

Сервер запустится на `http://0.0.0.0:8000`.

### Документация API

После запуска документация доступна по адресу:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Структура проекта

- `src/main.py`: Точка входа приложения.
- `src/container_router.py`: Роутер endpoints для контейнеров.
- `src/dao.py`: Слой доступа к данным (DAO).
- `src/dependencies.py`: Зависимости (верификация пользователя).
- `src/config.py`: Конфигурация приложения.
- `src/models.py`: Pydantic модели.
