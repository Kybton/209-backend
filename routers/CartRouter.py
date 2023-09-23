from http import HTTPStatus
from flask import Blueprint
from flask_pydantic import validate
from configs.Database import SessionLocal
from configs.Constants import ItemStatus
from models.UserModel import User
from models.ItemModel import Item
from models.CartModel import Cart
from models.CartItemModel import CartItem
from schemas.CartItemSchema import (
    CartItemPostRequest,
    CartItemGetRequest,
    CartItemRemoveSchema
)

CartRouter = Blueprint("carts", __name__, url_prefix="/carts")


@CartRouter.route("/<id>", methods=["GET"])
@validate()
def get_cart(id: int):
    with SessionLocal() as db:
        if not (db.get(Cart, id)):
            return CartItemGetRequest(detail="Cart not found."), HTTPStatus.NOT_FOUND
        
        cartItem = db.query(Item, CartItem.id).filter(CartItem.cart_id == id, Item.id == CartItem.item_id, Item.status == ItemStatus["listed"], Item.available_quantity > 0).all()
        
        cart_item_data = []
        
        for item, cart_id in cartItem:
            item_data = item.json()
            item_data["cart_item_id"] = cart_id
            cart_item_data.append(item_data)

    return CartItemGetRequest(detail="Cart items read successfully.", data=cart_item_data), 200


@CartRouter.route("/<id>", methods=["POST"])
@validate()
def add_item_to_cart(id: int, body: CartItemPostRequest):
    with SessionLocal() as db:
        item = db.get(Item, body.item_id)

        if not (db.get(Cart, id)) or not item:
            return CartItemGetRequest(detail="Not found."), HTTPStatus.NOT_FOUND
        
        if item.status == ItemStatus["unlisted"]:
            return CartItemGetRequest(detail="Item is not listed"), HTTPStatus.BAD_REQUEST
        
        cartItem = CartItem(cart_id=id, item_id=item.id, quantity=1)
        db.add(cartItem)
        db.commit()

    return CartItemGetRequest(detail="Item added to the cart."), HTTPStatus.CREATED


@CartRouter.route("/", methods=["DELETE"])
@validate()
def remove_item_from_cart(body: CartItemRemoveSchema):
    pass