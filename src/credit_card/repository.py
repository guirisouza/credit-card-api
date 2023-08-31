from typing import List

from sqlalchemy.orm import Session

from src.credit_card.models import CreditCardModel
from src.credit_card.schemas import CreditCardCreateSchema


class CreditCardRepository:
    async def create(
            self,
            db: Session,
            credit_card_schema: CreditCardCreateSchema,
            date) -> CreditCardModel:
        credit_card_schema.exp_date = date
        db_credit_card = CreditCardModel(**credit_card_schema.__dict__)
        db.add(db_credit_card)
        db.commit()
        db.refresh(db_credit_card)
        return db_credit_card

    def get_by_id(self, db: Session, _id) -> CreditCardModel:
        return db.query(CreditCardModel).filter(CreditCardModel.id == _id).first()

    def get_all(self, db: Session) -> List[CreditCardModel]:
        return db.query(CreditCardModel).all()
