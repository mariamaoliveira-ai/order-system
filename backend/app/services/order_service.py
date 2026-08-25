from sqlalchemy.orm import Session
from app.schemas import Order, OrderResponse

class OrderService:
    
    def __init__(self, db: Session):
        self.db = db
        
    def createOrder(self, order: Order) -> OrderResponse:
        pass
    
    