# Tut Gruz - Полный проект

Проект состоит из четырех компонентов:
- **tut-gruz-back** — Backend API (FastAPI)
- **tut-gruz-bot** — Telegram бот
- **tut-gruz-front** — Frontend приложение (React + Vite)
- **tut-gruz-client** — User API-клиент (Telethon)

## Структура проекта

```
tut-gruz-tz/
├── .env                 # Файл конфигурации для всего проекта
├── tut-gruz-back/       # Backend (FastAPI)
├── tut-gruz-bot/        # Telegram бот
├── tut-gruz-front/      # Frontend (React + Vite)
└── tut-gruz-client/     # User API-клиент (Telethon)
```

## Требования

### Backend и Bot
- Python 3.12+
- Менеджер пакетов `uv` (рекомендуется) или `pip`

### Frontend
- Node.js v20+
- npm или yarn

### Конфигурация
- Файл `.env` в корневой папке проекта (см. раздел [Конфигурация](#конфигурация))

---

## Конфигурация (.env)

Создайте файл `.env` в корневой папке репозитория (`tut-gruz-tz/.env`) со следующими переменными:

```ini
# Режим работы
MODE=DEV                              # DEV, PROD, TEST
LOG_LEVEL=INFO

# Telegram
BOT_TOKEN=your_telegram_bot_token     # Получить у @BotFather
APP_ID=your_app_id                    # Получить на my.telegram.org
APP_HASH=your_app_hash                # Получить на my.telegram.org

# User API (для клиента)
PHONE_NUMBER=+1234567890              # Номер телефона для Telethon клиента

# Web приложение
WEB_HOST=http://localhost:5173        # URL фронтенда
WEB_BACK=http://localhost:8000        # URL бэкенда

# Frontend
VITE_API=http://localhost:8000        # API URL для frontend
VITE_MODE=DEV                         # DEV или PROD
```

---

## Быстрый старт

### Способ 1: Запуск всех компонентов вручную

#### 1. Backend (FastAPI)

```bash
cd tut-gruz-back

# С помощью uv
uv sync
uv run python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# Или с помощью pip
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Backend будет доступен по адресу: **http://localhost:8000**

#### 2. Telegram Bot

В новом терминале:

```bash
cd tut-gruz-bot

# С помощью uv
uv sync
uv run python main.py

# Или с помощью pip
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Бот будет слушать обновления от Telegram.

#### 3. Frontend (React + Vite)

В новом терминале:

```bash
cd tut-gruz-front

# Установка зависимостей
npm install

# Запуск dev сервера
npm run dev
```

Frontend будет доступен по адресу: **http://localhost:5173**

#### 4. User API-клиент (Telethon)

В новом терминале:

```bash
cd tut-gruz-client

# С помощью uv
uv sync
uv run python main.py

# Или с помощью pip
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

### Способ 2: Использование Docker Compose (рекомендуется)

Самый простой способ запустить все компоненты одновременно:

```bash
# Убедитесь, что файл .env находится в корневой папке проекта
docker-compose --env-file .\.env  up --build
```

Команды для управления:

```bash
# Запуск всех сервисов
docker-compose up -d

# Остановка всех сервисов
docker-compose down

# Просмотр логов
docker-compose logs -f

# Логи конкретного сервиса
docker-compose logs -f backend
docker-compose logs -f bot
docker-compose logs -f frontend
docker-compose logs -f client

# Перестроение образов
docker-compose --env-file .\.env  up --build
```

**Порты после запуска:**
- Backend: http://localhost:8000
- Frontend: http://localhost:5173
- Bot: работает в фоне
- Client: работает в фоне

---

### Способ 3: Использование Docker (отдельные команды)

Каждый компонент можно запустить в Docker контейнере отдельно.

#### Backend

```bash
cd tut-gruz-back
docker build -t tut-gruz-back .
docker run --env-file ../.env -p 8000:8000 tut-gruz-back
```

#### Bot

```bash
cd tut-gruz-bot
docker build -t tut-gruz-bot .
docker run --env-file ../.env tut-gruz-bot
```

#### Frontend

```bash
cd tut-gruz-front
docker build -t tut-gruz-front .
docker run --env-file ../.env -p 5173:5173 tut-gruz-front
```

#### Client

```bash
cd tut-gruz-client
docker build -t tut-gruz-client .
docker run --env-file ../.env tut-gruz-client
```

---

## Запуск для разработки (все компоненты одновременно)

Рекомендуется открыть несколько терминалов или использовать tmux/screen.

**Терминал 1 - Backend:**
```bash
cd tut-gruz-back && uv sync && uv run python -m uvicorn src.main:app --reload
```

**Терминал 2 - Bot:**
```bash
cd tut-gruz-bot && uv sync && uv run python main.py
```

**Терминал 3 - Frontend:**
```bash
cd tut-gruz-front && npm install && npm run dev
```

**Терминал 4 - Client (опционально):**
```bash
cd tut-gruz-client && uv sync && uv run python main.py
```

---

## Порты и URL

| Компонент | Порт | URL |
|-----------|------|-----|
| Backend | 8000 | http://localhost:8000 |
| Frontend | 5173 | http://localhost:5173 |
| Telegram Bot | - | Слушает обновления от Telegram |
| User API-клиент | - | Работает с Telegram API |

---

## Документация компонентов

- [Backend API](./tut-gruz-back/README.md)
- [Telegram Bot](./tut-gruz-bot/README.md)
- [Frontend приложение](./tut-gruz-front/README.md)
- [User API-клиент](./tut-gruz-client/README.md)

---

## Возможные проблемы

### Ошибка подключения между компонентами
Убедитесь, что переменные в `.env` соответствуют реально запущенным сервисам:
- `WEB_BACK` должен указывать на рабочий Backend
- `WEB_HOST` должен указывать на рабочий Frontend
- `VITE_API` в Frontend должен указывать на Backend

### Bot не реагирует на команды
Проверьте:
1. Корректность `BOT_TOKEN` в `.env`
2. Что Bot процесс запущен и активен
3. Логи Bot'а на ошибки

### Frontend не подключается к API
Проверьте:
1. Что Backend запущен на `http://localhost:8000`
2. Значение `VITE_API` в `.env` совпадает с адресом Backend

### Python зависимости не устанавливаются
Убедитесь, что используете Python 3.12+:
```bash
python --version
```

Если используете `pip`, убедитесь, что virtual environment активирован.

---

## Разработка

Для внесения изменений:

1. Создайте ветку для вашей функции: `git checkout -b feature/your-feature`
2. Сделайте изменения и протестируйте их локально
3. Commit'ьте: `git commit -am 'Add your feature'`
4. Push'ьте: `git push origin feature/your-feature`
5. Откройте Pull Request

---

## Лицензия

[Укажите лицензию если необходимо]

---

## Контакты

[Укажите контакты если необходимо]
