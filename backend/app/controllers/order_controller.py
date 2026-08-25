from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from typing import Annotated

from app.database import get_db
from app.schemas import Order, OrderResponse
from app.services import OrderService

router = APIRouter(prefix="/orders")

def getOrderService(db: Session = Depends(get_db)) -> OrderService:
    return OrderService(db)

OrderServiceDep = Annotated[OrderService, Depends(getOrderService)]


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=OrderResponse)
def createOrder(order: Order, service: OrderServiceDep):
    try:
        return service.createOrder(order)
    except (OperationalError, ConnectionError):
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Connection Error."
        )
    
    