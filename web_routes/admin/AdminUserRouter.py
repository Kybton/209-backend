from flask import (
    Blueprint,
    request,
    render_template,
    redirect
)

from configs.Constants import UserTypes
from configs.Database import SessionLocal
from models.UserModel import User
from schemas.UserSchema import UserReturnSchema

AdminUserRouter = Blueprint("admin_user_route", __name__, url_prefix="/admin/users")

@AdminUserRouter.route("/", methods=["GET"])
def admin_user_index():
    with SessionLocal() as db:
        users = db.query(User).all()
        
    data = UserReturnSchema(detail="User read successfully.", data=[user.json() for user in users])

    return render_template("admin/user-index.html", data = data)

@AdminUserRouter.route("/<id>", methods=["GET"])
def get_user(id: int):
    with SessionLocal() as db:
        user = db.get(User, id)

    return render_template("admin/user-edit.html", data=user.json(), title="User Edit")
    
@AdminUserRouter.route("/update", methods=["POST"])
def update_user():
    user_id = request.form.get("id")
    user_full_name = request.form.get("name")
    user_email_address = request.form.get("email")
    is_admin = 0 if request.form.get("is_admin") is None else 1
    
    with SessionLocal() as db:
        user = db.get(User, user_id)
        
        user.full_name = user_full_name
        user.email_address = user_email_address
        user.is_admin = is_admin
        
        db.commit()

    return redirect("/admin/users")