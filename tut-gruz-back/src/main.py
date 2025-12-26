from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import logging
from src.container_router import router as container_router
from src.logging_config import setup_logging
from src.exception_handlers import (
    not_found_error_handler,
    internal_server_error_handler,
)

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="backend tut-gruz", redirect_slashes=False)

app.add_exception_handler(404, not_found_error_handler)
app.add_exception_handler(Exception, internal_server_error_handler)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Request completed: {response.status_code}")
    return response


app.include_router(container_router)
origins = [
    "http://localhost:5173",
    "https://6mfm08fw-8000.euw.devtunnels.ms",
    "https://dqwcjsrn-5173.euw.devtunnels.ms",
    "https://dj1z9xtc-5173.euw.devtunnels.ms",
    "https://gtchmfm3-5173.euw.devtunnels.ms",
    "https://dj1z9xtc-8000.euw.devtunnels.ms",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=[
        "X-Init-Data",
        "Content-Type",
        "Authorization",
        "Accept-Language",
        "X-Environment",
    ],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
