from typing import List
from pydantic import BaseModel
from schemas.UserSchema import UserSchema
from schemas.CategorySchema import CategorySchema


class BaseReturnSchema(BaseModel):
    detail: str
    data: UserSchema | CategorySchema = {}


class BaseReturnListSchema(BaseModel):
    detail: str
    data: List[UserSchema | CategorySchema] = []
