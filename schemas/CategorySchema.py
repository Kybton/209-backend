from pydantic import BaseModel


class CategoryPostRequestSchema(BaseModel):
    name: str


class CategorySchema(CategoryPostRequestSchema):
    id: int
