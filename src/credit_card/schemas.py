import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator

from src.credit_card.utils import CreditCardHelper


class CreditCardBaseSchema(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    number: str
    holder: str
    cvv: str = Optional[str]
    exp_date: str


class CreditCardCreateSchema(CreditCardBaseSchema):
    @validator('number')
    def validate_credit_card_number(cls, value):
        if not CreditCardHelper.credit_card_number_validator(number=value):
            raise ValueError(f"Invalid Credit Card Number {value}")
        return value

    @validator('exp_date')
    def validate_expiration_date(cls, value):
        if not bool(re.match("^\d{2}/\d{4}$", value)):
            raise ValueError("exp_date needs to be formatted in MM/YYYY ")
        day = datetime.utcnow().day
        month, year = value.split('/')
        if len(month) == 2 and month[0] == "0":
            month = month[1]
        date = datetime(int(year), int(month), int(day))
        if date.date() < datetime.utcnow().date():
            raise ValueError(f"exp_date can't be less than today")
        return value

    @validator('cvv')
    def validate_cvv(cls, value):
        if len(value) < 3 or len(value) > 4:
            raise ValueError(f"cvv must be between three and four characters")
        return value


class CreditCardSchema(CreditCardBaseSchema):
    id: int

    class Config:
        from_attributes = True
