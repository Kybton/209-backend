from flask import Blueprint

from configs.Database import SessionLocal
from configs.Constants import OrderStatus
from models.OrderModel import Order
from models.UserModel import User
from models.OrderItemModel import OrderItem
from schemas.OrderSchema import OrderGetRequestSchema, OrderPostRequestSchema, OrderListReturnSchema

OrderRouter = Blueprint("order", __name__, url_prefix="/orders")