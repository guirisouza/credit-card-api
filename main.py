from pathlib import Path

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from database.database import Base, engine
from src.router import api_router

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
    openapi_schema = get_openapi(
        title="credit-card-api",
        version="1.0",
        description="Teste desenvolvido para MaisTodos por "
                    "<a href='https://www.linkedin.com/in/guilherme-ribeiro-de-souza/'>Guilherme Ribeiro</a>",
        routes=app.routes
    )

    app.openapi_schema = openapi_schema

    return app
