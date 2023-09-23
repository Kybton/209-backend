from typing import List
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    full_name: str
    email_address: str
    is_admin: int


class UserPostRequestSchema(UserBaseSchema):
    password: str
    
class UserLoginSchema(BaseModel):
    email_address: str
    password: str


class UserSchema(BaseModel):
    id: int
    full_name: str
    email_address: str
    is_admin: int
    # cart_id: int

class UserReturnSchema(BaseModel):
    detail: str
    data: List[UserSchema] = []