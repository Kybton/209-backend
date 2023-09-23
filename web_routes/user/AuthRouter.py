from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from configs.Constants import default_image_url, ItemStatus
from configs.Database import SessionLocal
from models.ItemModel import Item
from models.UserModel import User
from models.CartModel import Cart
from services.PasswordService import PasswordService

UserAuthRouter = Blueprint("auth_router", __name__, url_prefix="/user")


@UserAuthRouter.route("/login", methods=["GET"])
def user_login_landing_page():
    return render_template("user/login.html")


@UserAuthRouter.route("/register", methods=["GET"])
def user_register_landing_page():
    return render_template("user/register.html", title="Register Member")


@UserAuthRouter.route("/register", methods=["POST"])
def user_register_new_member():
    full_name = request.form.get("full_name")
    email_address = request.form.get("email_address")
    password = request.form.get("password")

    with SessionLocal() as session:
        if (session.query(User).filter(User.email_address == email_address).first()):
            return render_template("user/register.html", title="Register Member")

        passwordService = PasswordService(password=password)
        passwordService.hash_it()
        password = passwordService.hashed_password

        user = User(full_name=full_name, email_address=email_address,
                    password=password, is_admin=0)
        session.add(user)
        session.commit()

        cart = Cart(user_id=user.id)
        session.add(cart)
        session.commit()

    return redirect("/user/login")


@UserAuthRouter.route("/login", methods=["POST"])
def user_login():
    email_address = request.form.get("email_address")
    password = request.form.get("password")

    if not email_address or not password:
        return redirect("/")

    with SessionLocal() as session:
        data = session.query(User, Cart.id).filter(
            User.email_address == email_address, Cart.user_id == User.id).first()

        if not data:
            return render_template("user/login.html", data=3)

        user = data[0]
        cart_id = data[1]

        if not user:
            return render_template("user/login.html", data=1)

        passwordService = PasswordService(
            password=password, hashed_password=user.password)
        if not (passwordService.check_password()):
            return render_template("user/login.html", data=2)

        user = user.json()
        user["cart_id"] = cart_id
        print(user["id"])

    return redirect(f"/user/{user['id']}/items")


@UserAuthRouter.route("/<user_id>/items", methods=["GET"])
def get_user_item_index(user_id):
    with SessionLocal() as db:
        items = db.query(Item).filter_by(status=ItemStatus["listed"]).all()

    data = []

    for item in items:
        d = item.json()

        if not d["img_url"]:
            d["img_url"] = default_image_url

        data.append(d)

    return render_template("user/index.html", title="Index", data=data, user_id=user_id)
