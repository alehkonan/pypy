from fastapi import FastAPI

from app.api.routers import items
from app.api.routers import health


def create_app() -> FastAPI:
    application = FastAPI(title="Simple CRUD API", version="1.0.0")

    application.include_router(health.router)
    application.include_router(items.router)
    return application


app = create_app()
