from http import HTTPStatus
from flask import Blueprint
from flask_pydantic import validate
from configs.Database import SessionLocal
from models.UserModel import User
from models.CartModel import Cart
from schemas.BaseReturnSchema import BaseReturnSchema

CartRouter = Blueprint("carts", __name__, url_prefix="/carts")