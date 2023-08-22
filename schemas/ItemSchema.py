from typing import Optional
from pydantic import BaseModel

class ItemPostRequestSchema(BaseModel):
    category_id: int
    name: str
    status: str
    total_quantity: int
    price: int
    
    
class ItemUpdateRequestSchema(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    status: Optional[str] = None
    available_quantity: Optional[int] = None
    hold_quantity: Optional[int] = None
    total_quantity: Optional[int] = None
    price: Optional[int] = None
    
    
class ItemGetRequestSchema(BaseModel):
    category_id: int
    name: str
    status: str
    available_quantity: int
    hold_quantity: int
    total_quantity: int
    price: int
    

class ItemSchema(ItemGetRequestSchema):
    id: int