from fastapi.routing import APIRouter

from src import credit_card, user

api_router = APIRouter()

api_router.include_router(
    user.router,
    prefix="/auth",
    tags=["Authentication"],
)

api_router.include_router(
    credit_card.router,
    prefix="/credit-card",
    tags=["Credit Card"],
)
