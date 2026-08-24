from sqlalchemy import Column, Integer, String, DateTime, Text

class OrderModel(Base):
    __tablename__= "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    