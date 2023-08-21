from http import HTTPStatus
from flask import Blueprint
from flask_pydantic import validate

from models.ItemModel import Item
from schemas.ItemSchema import ItemUpdateRequestSchema


ItemRouter = Blueprint("item_router", __name__, url_prefix="/items")

@ItemRouter.route("/", methods=["PATCH"])
@validate()
def update(body: ItemUpdateRequestSchema):
    return body