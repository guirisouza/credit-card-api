from datetime import datetime

from sqlalchemy import Column, DateTime, Integer

from database.database import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer,
                   primary_key=True,
                   autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)