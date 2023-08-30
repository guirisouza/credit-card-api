from pathlib import Path
from fastapi import FastAPI
from src.router import api_router
from database.database import engine, Base

APP_ROOT = Path(__file__).parent

Base.metadata.create_all(bind=engine)

def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI()

    app.include_router(
        prefix="/api/v1",
        router=api_router,
    )
    return app