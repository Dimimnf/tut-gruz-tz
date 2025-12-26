FROM python:3.12-slim-bullseye

WORKDIR /app

# Устанавливаем uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Копируем файл зависимостей
COPY pyproject.toml uv.lock ./

# Устанавливаем зависимости
RUN uv sync --frozen --no-cache

# Копируем исходный код
COPY src/ ./src/

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
