from typing import List
from pydantic import BaseModel
from schemas.UserSchema import UserSchema
from schemas.CategorySchema import CategorySchema
from schemas.ItemSchema import ItemSchema


class BaseReturnSchema(BaseModel):
    detail: str
    data: UserSchema | CategorySchema = {}
    
class ItemReturnSchema(BaseReturnSchema):
    data: ItemSchema = {}
    
class ItemReturnListSchema(BaseReturnSchema):
    data: List[ItemSchema] = []

class BaseReturnListSchema(BaseReturnSchema):
    data: List[UserSchema | CategorySchema | ItemSchema] = []
