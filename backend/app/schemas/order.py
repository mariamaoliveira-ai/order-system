from pydantic import BaseModel, Field, field_validator

class Order(BaseModel):
    items: str = Field(..., description="Items in a order")
    
    @field_validator("items")
    @classmethod
    def prevent_empty_or_whitespace(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Field cannot be empty or contain only whitespace")
        return value.strip()
    
    
class OrderResponse(BaseModel):
    id: int = Field(..., description="Id in the DB of an order")
    status: str = Field(..., description="Status in the DB of an order")
    