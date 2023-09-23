from flask import (
    Blueprint,
    request,
    render_template,
    redirect
)

from datetime import datetime

from configs.Constants import ItemStatus, default_image_url, OrderStatus, OrderStatusValue
from configs.Database import SessionLocal
from models.OrderModel import Order
from models.OrderItemModel import OrderItem
from models.ItemModel import Item

AdminOrderRouter = Blueprint(
    "admin_order_router", __name__, url_prefix="/admin/orders")


@AdminOrderRouter.route("/")
def get_all_orders():
    data = []

    with SessionLocal() as session:
        orders = session.query(Order).all()

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

    return render_template("/admin/order.html", data=data), 200


@AdminOrderRouter.route("/status", methods=["POST"])
def admin_update_order_status():
    order_id = request.form.get("order-id")
    order_status = request.form.get("order-status")

    print(order_status)

    with SessionLocal() as session:
        order = session.get(Order, order_id)
        order.status = OrderStatus[order_status]
        session.commit()

    return redirect("/admin/orders")
