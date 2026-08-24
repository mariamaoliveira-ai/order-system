import enum
from sqlalchemy import Column, Integer, DateTime, Enum, Text, func
from app.database.base import Base

class OrderStatus(str, enum.Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    items = Column(Text, nullable=False)
    status = Column(
        Enum(OrderStatus, name="order_status_enum"), 
        nullable=False, 
        default=OrderStatus.PENDING
    )
    timestamp = Column(
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    )
    