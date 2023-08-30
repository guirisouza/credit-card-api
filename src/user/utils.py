from typing import Annotated


from fastapi import HTTPException, Depends
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from src.credit_card.utils import CryptHandler
from src.user.models import UsersModel
from src.user.repository import UserRepository

ALGORITHM = "HS256"
JWT_SECRET_KEY = "GATOGORDOCOMETUDO1"

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def authenticate_user(username: str, password: str, db) -> UsersModel:
    crypt_handler = CryptHandler()
    crypt_handler.load_fernet()
    user = UserRepository().get_user_by_username(username=username, db=db)
    decrypted_password = crypt_handler.decrypt(data=user.password).decode()
    if not user:
        raise HTTPException(status_code=status.HTTP_401,
                            detail="Could not validate user")
    if not decrypted_password == password:
        raise HTTPException(status_code=401)
    return user


def create_access_token(username: str, user_id: int, expires: timedelta) -> str:
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires
    encode.update({'exp': expires})
    return jwt.encode(encode, JWT_SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        user_id = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user')
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user')


