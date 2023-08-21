from typing import Optional
from pydantic import BaseModel

class ItemPostRequestSchema(BaseModel):
    category_id: int
    name: str
    status: int
    total_quantity: int
    price: int
    
    
class ItemUpdateRequestSchema(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[int] = None
    available_quantity: Optional[int] = None
    hold_quantity: Optional[int] = None
    total_quantity: Optional[int] = None
    price: Optional[int] = None
    
    
class ItemGetRequestSchema(BaseModel):
    category_id: int
    name: str
    status: int
    available_quantity: int
    hold_quantity: int
    total_quantity: int
    price: int
    

class ItemSchema(ItemGetRequestSchema):
    id: int