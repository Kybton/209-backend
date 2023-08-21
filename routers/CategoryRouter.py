from http import HTTPStatus, HTTPMethod
from models.CategoryModel import Category
from flask import Blueprint
from flask_pydantic import validate

from schemas.BaseReturnSchema import (
    BaseReturnSchema, 
    BaseReturnListSchema
)

from schemas.CategorySchema import CategoryPostRequestSchema
from configs.Database import SessionLocal

CategoryRouter = Blueprint("category_router", __name__, url_prefix="/categories")

@CategoryRouter.route("/", methods=["POST"])
@validate()
def create(body: CategoryPostRequestSchema):
    with SessionLocal() as session:
        if (session.query(Category).filter(Category.name == body.name).first()):
            return BaseReturnSchema(detail="Cannot create duplicate categories."), HTTPStatus.NOT_ACCEPTABLE

        category = Category(name=body.name)
        session.add(category)
        session.commit()

    return BaseReturnSchema(detail="New category added.", data=category.json())


@CategoryRouter.route("/", methods=["GET"])
@validate()
def get_all():
    with SessionLocal() as session:
        categories = session.query(Category).all()

    return BaseReturnListSchema(detail="Category read successfully.", data=[category.json() for category in categories]), HTTPStatus.OK


@CategoryRouter.route("/<id>", methods=["GET"])
@validate()
def get(id: int):
    with SessionLocal() as session:
        category = session.get(Category, id)
        
        if not category:
            return BaseReturnSchema(detail="Category not found."), HTTPStatus.NOT_FOUND

    return BaseReturnSchema(detail="Category read successfully", data=category.json()), HTTPStatus.OK

@CategoryRouter.route("/<id>", methods=[HTTPMethod.PATCH])
@validate()
def update(id: int, body: CategoryPostRequestSchema):
    with SessionLocal() as session:
        category = session.get(Category, id)
        
        if not category:
            return BaseReturnSchema(detail="Category not found."), HTTPStatus.NOT_FOUND

        if (session.query(Category).filter(Category.name == body.name).first()):
            return BaseReturnSchema(detail="Cannot create duplicate categories."), HTTPStatus.NOT_ACCEPTABLE

        category.name = body.name
        session.merge(category)
        session.commit()
        
    return BaseReturnSchema(detail="Category updated.", data=category.json()), HTTPStatus.OK


@CategoryRouter.route("/<id>", methods=["DELETE"])
@validate()
def delete(id: int):
    with SessionLocal() as session:
        category = session.get(Category, id)

        if not category:
            return BaseReturnSchema(detail="Not found"), HTTPStatus.NOT_FOUND

        session.delete(category)
        session.commit()
        
    return BaseReturnSchema(detail="Category deleted successfully", data=category.json()), HTTPStatus.OK