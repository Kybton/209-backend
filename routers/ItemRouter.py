from http import HTTPStatus
from flask import Blueprint
from flask_pydantic import validate

from sqlalchemy.exc import IntegrityError
from configs.Database import SessionLocal
from configs.Constants import ItemStatus
from models.ItemModel import Item
from models.CategoryModel import Category
from schemas.ItemSchema import ItemUpdateRequestSchema, ItemPostRequestSchema
from schemas.BaseReturnSchema import ItemReturnSchema, ItemReturnListSchema


ItemRouter = Blueprint("item_router", __name__, url_prefix="/items")


@ItemRouter.route("/", methods=["POST"])
@validate()
def create(body: ItemPostRequestSchema):
    if not ItemStatus.get(body.status):
        return ItemReturnSchema(detail="Invalid item status."), HTTPStatus.BAD_REQUEST

    with SessionLocal() as session:
        try:
            item = Item(
                category_id=body.category_id,
                name=body.name,
                status=ItemStatus.get(body.status),
                available_quantity=body.total_quantity,
                hold_quantity=0,
                total_quantity=body.total_quantity ,
                price=body.price
            )
            session.add(item)
            session.commit()
        except IntegrityError:
            session.rollback()
            return ItemReturnSchema(detail="Invalid 'category_id'."), HTTPStatus.BAD_REQUEST

    return ItemReturnSchema(detail="Item created successfully.", data=item.json()), HTTPStatus.CREATED

@ItemRouter.route("/", methods=["GET"])
@validate()
def get():
    with SessionLocal() as session:
        items = session.query(Item).all()
    
    return ItemReturnListSchema(detail="Items read successfully.", data=[item.json() for item in items])

@ItemRouter.route("/<id>", methods=["PATCH"])
@validate()
def update(id: int, body: ItemUpdateRequestSchema):

    with SessionLocal() as session:
        item = session.get(Item, id)
        
        if not item:
            return ItemReturnSchema(detail="Item not found."), HTTPStatus.NOT_FOUND
        
        if body.name:
            item.name = body.name
            
        if body.status:
            if not ItemStatus.get(body.status):
                return ItemReturnSchema(detail="Invalid 'status'. Update Failed."), HTTPStatus.BAD_REQUEST
            item.status = ItemStatus.get(body.status)
            
        if body.total_quantity:
            if item.hold_quantity > body.total_quantity:
                return ItemReturnSchema(detail="Total quantity cannot be smaller than hold quantity."), HTTPStatus.BAD_REQUEST
            
            item.total_quantity = body.total_quantity
            item.available_quantity = item.total_quantity - item.hold_quantity
        
        if body.price and body.price >= 0:
            item.price = body.price
            
        if body.category_id:
            if not session.get(Category, body.category_id):
                return ItemReturnSchema(detail="Invalid 'category_id'. Update Failed."), HTTPStatus.BAD_REQUEST
            item.category_id = body.category_id
        
        session.merge(item)
        session.commit()

    return ItemReturnSchema(detail="Item updated successfully.", data=item.json()), HTTPStatus.OK


@ItemRouter.route("/<id>", methods=["DELETE"])
@validate()
def delete(id: int):
    with SessionLocal() as session:
        item = session.get(Item, id)
        
        if not item:
            return ItemReturnSchema(detail="Item not found."), HTTPStatus.NOT_FOUND
        
        session.delete(item)
        session.commit()
    
    return ItemReturnSchema(detail="Item deleted successfully."), HTTPStatus.OK