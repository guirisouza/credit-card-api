from sqlalchemy import Column, Date, Integer, String

from database.base import BaseModel
from src.credit_card.custom_types import CreditCardNumber


class CreditCardModel(BaseModel):
    __tablename__ = "credit_card"

    number = Column(CreditCardNumber)
    holder = Column(String, nullable=True)
    cvv = Column(String, nullable=True)
    exp_date = Column(Date)
