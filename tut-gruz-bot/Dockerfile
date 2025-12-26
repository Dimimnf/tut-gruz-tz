FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
# --frozen: sync validation against uv.lock
# --no-dev: exclude development dependencies
RUN uv sync --frozen --no-dev

# Copy application code
COPY . .

# Run the application
# 'uv run' will automatically use the virtual environment created by 'uv sync'
CMD ["uv", "run", "python", "-m", "bot.main"]
