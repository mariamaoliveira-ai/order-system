from sqlalchemy.orm import Session

from app.schemas import Order, OrderResponse
from app.database.models import Order as OrderModel

class OrderService:
    
    def __init__(self, db: Session):
        self.db = db
        
    def createOrder(self, order: Order) -> OrderResponse:
        
        db_order = OrderModel(**order.model_dump())
        
        try: 
            self.db.add(db_order)
            self.db.commit()
            self.db.refresh(db_order)
            return db_order
        except Exception:
            self.db.rollback()
            raise 
        
    
    