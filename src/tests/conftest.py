from datetime import datetime

import pytest

from database.database import SessionLocal
from src.credit_card.models import CreditCardModel


@pytest.fixture()
def db_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()

@pytest.fixture()
def credit_cards_on_db(db_session):
    exp_date = datetime(2023, 10, 17).date()
    created_at = datetime(2023, 8, 1).date()
    credit_cards = [
        CreditCardModel(
            number="4539594725731594",
            holder="José Carlos",
            cvv="544",
            exp_date=exp_date,
            created_at=created_at
        ),
        CreditCardModel(
            number="5290896515399433",
            holder="Vitor Trindade",
            cvv="655",
            exp_date=exp_date,
            created_at=created_at
        ),
        CreditCardModel(
            number="374836548382568",
            holder="João Paulo",
            cvv="677",
            exp_date=exp_date,
            created_at=created_at
        ),
        CreditCardModel(
            number="4024007173984823",
            holder="Fernanda Silva",
            cvv="855",
            exp_date=exp_date,
            created_at=created_at
        )
    ]
    for card in credit_cards:
        db_session.add(card)
    db_session.commit()

    for card in credit_cards:
        db_session.refresh(card)

    yield credit_cards

    for card in credit_cards:
        db_session.delete(card)
    db_session.commit()

@pytest.fixture()
def credit_card_on_db(db_session):
    date = datetime(2020, 5, 17).date()
    card = CreditCardModel(
        number="4539594725731594",
        holder="José Carlos",
        cvv="544",
        exp_date=date
    )

    db_session.add(card)
    db_session.commit()
    db_session.refresh(card)

    yield card

    db_session.delete(card)
    db_session.commit()

@pytest.fixture()
def cleanup_cards(db_session):
    yield
    db_session.query(CreditCardModel).delete()
    db_session.commit()
