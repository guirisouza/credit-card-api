from sqlalchemy import Column, Date, Integer, LargeBinary, String

from database.base import BaseModel
from src.credit_card.custom_types import CreditCardNumber


class CreditCardModel(BaseModel):
    __tablename__ = "credit_card"

    number = Column(CreditCardNumber)
    holder = Column(String, nullable=True)
    cvv = Column(Integer)
    exp_date = Column(Date)
