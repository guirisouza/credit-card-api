from sqlalchemy import Column, String

from database.base import BaseModel


class UsersModel(BaseModel):
    __tablename__ = "users"
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
