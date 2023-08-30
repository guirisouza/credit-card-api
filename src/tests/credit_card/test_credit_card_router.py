import pytest

from fastapi import status
from fastapi.testclient import TestClient

from main import get_app
from src.credit_card.models import CreditCardModel
from src.user.utils import get_current_user

app = get_app()
def skip_auth():
    pass

app.dependency_overrides[get_current_user] = skip_auth

client = TestClient(app)

PREFIX_API_ADDRESS = "/api/v1"

@pytest.fixture
def card_data():
    return {
        "number": "4485784983184503",
        "holder": "José Carlos",
        "cvv": "655",
        "exp_date": "07/2025"
    }

def test_create_valid_credit_card_number(
        db_session,
        card_data,
        cleanup_cards
):
    response = client.post(
        f"{PREFIX_API_ADDRESS}/credit-card",
        json=card_data
    )

    body_response = response.json()
    credit_cards = db_session.query(CreditCardModel).filter(
        CreditCardModel.id == body_response.get('id')
    ).all()

    assert response.status_code == status.HTTP_201_CREATED
    assert len(credit_cards) == 1



def test_create_invalid_credit_card(db_session, card_data):
    card_data.update(
        {
            "number": "4485784983184503123"
        }
    )

    response = client.post(
        f"{PREFIX_API_ADDRESS}/credit-card",
        json=card_data
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_create_invalid_credit_card_cvv(db_session, card_data):
    card_data.update(
        {
            "cvv": "22"
        }
    )

    response = client.post(
        f"{PREFIX_API_ADDRESS}/credit-card",
        json=card_data
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.parametrize(
    "invalid_exp_date",
    [
        "2025/09", "09/2021", "09-2024"
    ]
)
def test_create_invalid_exp_date(db_session, invalid_exp_date, card_data):
        card_data.update(
            {
                "exp_date": invalid_exp_date
            }
        )

        response = client.post(
            f"{PREFIX_API_ADDRESS}/credit-card",
            json=card_data
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_create_valid_credit_card_whitout_cvv(
        db_session,
        cleanup_cards,
        card_data
):
    del card_data["cvv"]
    response = client.post(
        f"{PREFIX_API_ADDRESS}/credit-card",
        json=card_data
    )
    body_response = response.json()

    credit_cards = db_session.query(CreditCardModel).filter(
        CreditCardModel.id == body_response.get('id')
    ).all()

    assert response.status_code == status.HTTP_201_CREATED
    assert len(credit_cards) == 1


def test_correct_list_credit_card(credit_cards_on_db):
    response = client.get(f"{PREFIX_API_ADDRESS}/credit-card")

    body_response = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert body_response == [
        {
            "created_at": "2023-08-01T00:00:00",
            "cvv": 544,
            "exp_date": "2023-10-17",
            "holder": "José Carlos",
            "id": 1,
            "number": "4539594725731594"
        },
        {
            "created_at": "2023-08-01T00:00:00",
            "cvv": 655,
            "exp_date": "2023-10-17",
            "holder": "Vitor Trindade",
            "id": 2,
            "number": "5290896515399433"},
        {
            "created_at": "2023-08-01T00:00:00",
            "cvv": 677,
            "exp_date": "2023-10-17",
            "holder": "João Paulo",
            "id": 3,
            "number": "374836548382568"
        },
        {
            "created_at": "2023-08-01T00:00:00",
            "cvv": 855,
            "exp_date": "2023-10-17",
            "holder": "Fernanda Silva",
            "id": 4,
            "number": "4024007173984823"
        }
    ]

# TODO: do the same as above
def test_exist_get_credit_card_by_id(credit_card_on_db):
    response = client.get(f"{PREFIX_API_ADDRESS}/credit-card/{credit_card_on_db.id}")

    assert response.status_code == status.HTTP_200_OK
    body_response = response.json()

    del body_response["created_at"]
    assert body_response == {
        "number": credit_card_on_db.number.decode(),
        "holder": credit_card_on_db.holder,
        "cvv": credit_card_on_db.cvv,
        "exp_date": str(credit_card_on_db.exp_date),
        "id": credit_card_on_db.id
    }

# TODO: the same as above, move the asserts to be together at the end of the test
def test_not_exist_get_credit_card_by_id():
    response = client.get(f"{PREFIX_API_ADDRESS}/credit-card/{999}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    body_response = response.json()

    assert body_response["detail"] == f"Credit Card id {999} not found"