from typing import List, Optional
from schemas.ItemSchema import ItemSchema
from pydantic import BaseModel

class CartItemPostRequest(BaseModel):
    item_id: int
    
class CartItemSchema(ItemSchema):
    cart_item_id: Optional[int]
    
class CartItemRemoveSchema(BaseModel):
    cart_item_id: Optional[int]
    
class CartItemGetRequest(BaseModel):
    detail: str
    data: List[CartItemSchema] = []