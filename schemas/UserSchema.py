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


class UserSchema(UserBaseSchema):
    id: int
