from sqlalchemy.orm import Session

from src.credit_card.models import CreditCardModel
from src.credit_card.schemas import CreditCardCreateSchema

#TODO: fix size of the lines
# Add the returning ype
class CreditCardRepository:
    async def create(self, db: Session, credit_card_schema: CreditCardCreateSchema, date):
        if credit_card_schema.cvv:
            credit_card_schema.cvv = None
        db_credit_card = CreditCardModel(
            number=credit_card_schema.number,
            cvv=credit_card_schema.cvv,
            holder=credit_card_schema.holder,
            exp_date=date
        )
        db.add(db_credit_card)
        db.commit()
        db.refresh(db_credit_card)
        return db_credit_card

    def get_by_id(self, db: Session, _id):
        return db.query(CreditCardModel).filter(CreditCardModel.id == _id).first()

    def get_all(self, db: Session):
        return db.query(CreditCardModel).all()
