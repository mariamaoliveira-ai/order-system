from pydantic import BaseModel, Field

class Order(BaseModel):
    items: str = Field(..., description="Items in a order")
    
class OrderResponse(BaseModel):
    id: int = Field(..., description="Id in the DB of an order")
    status: str = Field(..., description="Status in the DB of an order")