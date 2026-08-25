from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

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
    return service.createOrder(order)
    
    