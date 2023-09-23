from flask import (
    Blueprint,
    request,
    redirect,
    render_template
)

from configs.Constants import default_image_url, ItemStatus
from models.ItemModel import Item
from models.CartModel import Cart
from models.CartItemModel import CartItem
from configs.Database import SessionLocal


UserCartRouter = Blueprint(
    "user_cart_router", __name__, url_prefix="/user/cart")


@UserCartRouter.route("/", methods=["GET"])
def user_get_cart_items():
    user_id = request.args.get("user_id")

    with SessionLocal() as session:
        items = session.query(Item, CartItem.id).filter(
            Item.id == CartItem.item_id, Cart.user_id == user_id, CartItem.cart_id == Cart.id, Item.status == ItemStatus["listed"]).all()

    data = []

    for (item, cart_item) in items:
        d = item.json()
        d["cart_item_id"] = cart_item

        if not d["img_url"]:
            d["img_url"] = default_image_url

        data.append(d)

    return render_template("/user/cart.html", data=data, user_id=user_id)


@UserCartRouter.route("/add_to_cart", methods=["GET"])
def user_add_to_cart():
    user_id = request.args.get("user_id")
    item_id = request.args.get("item_id")

    with SessionLocal() as session:
        cart = session.query(Cart).filter_by(user_id=user_id).first()
        cart_item = CartItem(cart_id=cart.id, item_id=item_id, quantity=1)

        session.add(cart_item)
        session.commit()

    return redirect(f"/user/{user_id}/items")


@UserCartRouter.route("/remove_from_cart")
def user_remove_cart_item():
    user_id = request.args.get("user_id")
    cart_item_id = request.args.get("cart_item_id")

    with SessionLocal() as session:
        cart_item = session.query(CartItem).filter_by(id=cart_item_id).first()
        session.delete(cart_item)
        session.commit()

    return redirect(f"/user/cart?user_id={user_id}")
