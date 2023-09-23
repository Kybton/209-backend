from flask import (
    Blueprint,
    request,
    redirect,
    render_template
)
from datetime import datetime

from configs.Constants import ItemStatus, default_image_url, OrderStatus
from configs.Database import SessionLocal
from models.ItemModel import Item
from models.OrderModel import Order
from models.OrderItemModel import OrderItem

UserItemRouter = Blueprint(
    "user_item_router", __name__, url_prefix="/user/items")


@UserItemRouter.route("/", methods=["GET"])
def get_user_item_index():
    with SessionLocal() as db:
        items = db.query(Item).filter_by(status=ItemStatus["listed"]).all()

    data = []

    for item in items:
        d = item.json()

        if not d["img_url"]:
            d["img_url"] = default_image_url

        data.append(d)

    return render_template("user/index.html", title="Index", data=data)


@UserItemRouter.route("/place_order", methods=["GET"])
def user_place_order():
    user_id = request.args.get("user_id")
    item_id = request.args.get("item_id")

    return render_template("user/place_order.html", user_id=user_id, item_id=item_id)


@UserItemRouter.route("/final_place_order", methods=["POST"])
def user_final_place_order():
    user_id = request.args.get("user_id")
    item_id = request.args.get("item_id")

    quantity = int(request.form.get("quantity"))
    phone_number = request.form.get("phone_number")
    address = request.form.get("address")
    remark = request.form.get("remark")

    with SessionLocal() as session:
        order = Order(user_id=user_id, status=OrderStatus["pending"],
                      delivery_address=address, contact_number=phone_number, remark=remark, order_time=datetime.now())
        session.add(order)
        session.commit()

        item = session.query(Item).filter_by(id=item_id).first()

        order_item = OrderItem(
            order_id=order.id, item_id=item_id, quantity=quantity, price=item.price, total=item.price * quantity)

        session.add(order_item)
        session.commit()

    return redirect(f"/user/{user_id}/items")
