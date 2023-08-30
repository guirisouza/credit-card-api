from fastapi import HTTPException


class CreditCardNotFound(HTTPException):
    def __init__(self, id: int):
        self.status_code = 404
        self.detail = f"Credit Card id {id} not found"
