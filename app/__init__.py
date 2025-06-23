from fastapi import FastAPI
from .logger import configure_logging
from .routes import router


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title="analytics_service", version="1.0.0")
    app.include_router(router)
    return app


app = create_app()
