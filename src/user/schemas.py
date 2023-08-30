import re
from pydantic import BaseModel, validator
from datetime import datetime


class CreateUserInputSchema(BaseModel):
    username: str
    password: str

    @validator('username')
    def valid_username(cls, value):
        if not bool(re.match(r'^[\w.-]+$', value)):
            raise ValueError('Invalid Username')
        return value

class TokenDataSchema(BaseModel):
    access_token: str
    token_type: datetime

