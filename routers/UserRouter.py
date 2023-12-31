from http import HTTPStatus
from flask import Blueprint
from flask_pydantic import validate
from configs.Database import SessionLocal
from models.UserModel import User
from models.CartModel import Cart
from schemas.BaseReturnSchema import BaseReturnSchema
from schemas.UserSchema import UserPostRequestSchema, UserLoginSchema, UserSchema
from services.PasswordService import PasswordService

UserRouter = Blueprint("user", __name__, url_prefix="/users")

@UserRouter.route("/", methods=["POST"])
@validate()
def create(body: UserPostRequestSchema):
    with SessionLocal() as session:

        if (session.query(User).filter(User.email_address == body.email_address).first()):
            return BaseReturnSchema(detail="This email address has already been registered."), HTTPStatus.BAD_REQUEST
        
        passwordService = PasswordService(password=body.password)
        passwordService.hash_it()
        body.password = passwordService.hashed_password

        user = User(full_name=body.full_name, email_address=body.email_address, password=body.password, is_admin=body.is_admin)
        session.add(user)
        session.commit()

        cart = Cart(user_id=user.id)
        session.add(cart)
        session.commit()

    return BaseReturnSchema(detail="User registered successfully.", data=user.json()), HTTPStatus.CREATED

@UserRouter.route("/login", methods=["POST"])
@validate()
def login(body: UserLoginSchema):

    with SessionLocal() as session:
        data = session.query(User, Cart.id).filter(User.email_address == body.email_address, Cart.user_id == User.id).first()

        if not data:
            return BaseReturnSchema(detail="User not found."), HTTPStatus.NOT_FOUND
 
        user = data[0]
        cart_id = data[1]
        
        if not user:
            return BaseReturnSchema(detail="User not found."), HTTPStatus.NOT_FOUND
        
        passwordService = PasswordService(password=body.password, hashed_password=user.password)
        if not (passwordService.check_password()):
            return BaseReturnSchema(detail="Wrong credentials."), HTTPStatus.UNAUTHORIZED
        
        user = user.json()
        user["cart_id"] = cart_id

    return BaseReturnSchema(detail="Logged in successfully.", data=user), HTTPStatus.OK