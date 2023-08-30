from sqlalchemy.orm import Session

from src.user.schemas import CreateUserInputSchema
from src.user.models import UsersModel


class UserRepository:

    async def create(self, db: Session, data: CreateUserInputSchema):
        user = UsersModel(username=data.username, password=data.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_username(self, username: str, db: Session):
        user = db.query(UsersModel).filter(UsersModel.username == username).first()
        return user
