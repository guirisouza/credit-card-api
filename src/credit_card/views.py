from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from database.database import get_db
from src.credit_card.repository import CreditCardRepository
from src.credit_card.schemas import CreditCardCreateSchema
from src.credit_card.utils import CreditCardHelper
from src.credit_card.exceptions import CreditCardNotFound
from src.user.utils import get_current_user

router = APIRouter()

user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/")
async def fetch_all_credit_cards(user: user_dependency, db: Session = Depends(get_db)):
    repository = CreditCardRepository()
    credit_cards = repository.get_all(db=db)
    return credit_cards


@router.get("/{credit_card_id}")
async def fetch_credit_card_by_id(
        user: user_dependency,
        credit_card_id: Annotated[int, Path(title="The ID of the credit card to get")],
        db: Session = Depends(get_db)
):
    repository = CreditCardRepository()
    credit_card = repository.get_by_id(db=db, _id=credit_card_id)
    if not credit_card:
        raise CreditCardNotFound(id=credit_card_id)
    return credit_card

@router.post("/", status_code=201)
async def create_credit_card(user: user_dependency,
                             body: CreditCardCreateSchema,
                             db: Session = Depends(get_db)
                             ):
    custom_date = CreditCardHelper.parse_date(date=body.exp_date)
    repository = CreditCardRepository()
    credit_card = await repository.create(db=db, credit_card_schema=body, date=custom_date)
    return credit_card
