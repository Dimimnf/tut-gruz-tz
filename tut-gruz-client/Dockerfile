FROM python:3.12-slim

WORKDIR /app

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Копируем uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Копируем файл зависимостей
COPY pyproject.toml uv.lock* ./

# Устанавливаем зависимости
RUN uv sync --frozen

# Копируем приложение
COPY . .

# Запускаем приложение
CMD ["uv", "run", "python", "main.py"]
