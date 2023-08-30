import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URLS = {
    "prod": "sqlite:///./sql_app.db",
    "test": "sqlite:///./sql_app_test.db"
}
ENV = os.getenv('ENV', "prod")

engine = create_engine(
    SQLALCHEMY_DATABASE_URLS[ENV],
    connect_args={
        "check_same_thread": False
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()