from datetime import timedelta

from fastapi import Depends, APIRouter
from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database.database import get_db
from src.user.repository import UserRepository
from src.credit_card.utils import CryptHandler
from src.user.schemas import CreateUserInputSchema
from src.user.utils import authenticate_user, create_access_token, get_current_user

router = APIRouter()


@router.post("/", status_code=201)
async def create_user(body: CreateUserInputSchema, db: Session = Depends(get_db)):
    crypt_handler = CryptHandler()
    crypt_handler.load_fernet()
    body.password = crypt_handler.encrypt(data=body.password)
    user_repository = UserRepository()
    await user_repository.create(db=db, data=body)


@router.post("/token")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: Session = Depends(get_db)
    ):
    user = authenticate_user(form_data.username, form_data.password, db)
    token = create_access_token(username=user.username, user_id=user.id, expires=timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}


