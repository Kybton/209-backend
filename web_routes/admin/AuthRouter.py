from flask import (
    Blueprint, 
    render_template, 
    request, 
    redirect
)

from configs.Database import SessionLocal
from configs.Constants import UserTypes
from models.UserModel import User
from services.PasswordService import PasswordService

AdminAuthRouter = Blueprint("admin_auth_router", __name__, url_prefix="/admin")

@AdminAuthRouter.route("/login", methods=["GET"])
def admin_login_landing_page():
    return render_template("admin/login.html")

@AdminAuthRouter.route("/dashboard", methods=["GET"])
def admin_dashboard():
    return render_template("admin/dashboard.html")

@AdminAuthRouter.route("/login", methods=["POSt"])
def admin_login_action():
    email_address = request.form.get("email_address")
    password = request.form.get("password")
    
    if not email_address or not password:
        return redirect("admin/login.html")

    with SessionLocal() as session:
        # data = session.query(User, Cart.id).filter(User.email_address == email_address, Cart.user_id == User.id).first()
        user = session.query(User).filter(User.email_address == email_address, User.is_admin == UserTypes["admin"]).first()

        if not user:
            return render_template("admin/login.html", data=1)
        
        passwordService = PasswordService(password=password, hashed_password=user.password)
        if not (passwordService.check_password()):
            return render_template("admin/login.html", data=2)
        
        user = user.json()

    return redirect("/admin/dashboard")