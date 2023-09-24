from flask import (
    Blueprint,
    request,
    redirect,
    render_template
)
from datetime import datetime

from configs.Constants import ItemStatus, default_image_url, OrderStatus, OrderStatusValue
from configs.Database import SessionLocal
from models.OrderModel import Order
from models.OrderItemModel import OrderItem
from models.ItemModel import Item


UserOrderRouter = Blueprint(
    "user_order_router", __name__, url_prefix="/user/orders")


@UserOrderRouter.route("/")
def get_user_orders():
    user_id = request.args.get("user_id")

    data = []

    with SessionLocal() as session:
        orders = session.query(Order).filter_by(user_id=user_id).all()

        for order in orders:
            total = 0
            order_items = session.query(
                OrderItem.total).filter_by(order_id=order.id).all()

            for order_item in order_items:
                total += order_item.total

            data.append(
                {
                    "id": order.id,
                    "status": OrderStatusValue[order.status.__str__()],
                    "delivery_address": order.delivery_address,
                    "order_time": order.order_time.__str__(),
                    "contact_number": order.contact_number,
                    "remark": order.remark,
                    "total": total
                }
            )

    return render_template("/user/order.html", data=data, user_id=user_id), 200


@UserOrderRouter.route("/cancel")
def user_cancel_order():
    user_id = request.args.get("user_id")
    order_id = request.args.get("order_id")
    print(user_id)

    with SessionLocal() as session:
        order = session.get(Order, order_id)
        order.status = OrderStatus["rejected"]
        session.commit()

    return redirect(f"/user/orders?user_id={user_id}")
