from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from schemas.ItemSchema import ItemSchema

class OrderGetRequestSchema(BaseModel):
    id: int
    user_id: int
    status: str
    delivery_address: str
    contact_number: str
    order_time: datetime
    remark: Optional[str] = None
    item_data: List[ItemSchema] = []
    
class OrderPostRequestSchema(BaseModel):
    user_id: int
    status: str
    delivery_address: str
    contact_number: str
    remark: Optional[str] = None
    item_id: List
    
class OrderListReturnSchema(BaseModel):
    detail: str
    data: List[OrderGetRequestSchema] = None