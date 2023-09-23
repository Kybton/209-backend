from flask import Flask, redirect
from models.BaseModel import init
from web_routes.user.AuthRouter import UserAuthRouter
from web_routes.user.ItemRouter import UserItemRouter
from web_routes.user.CartRouter import UserCartRouter
from web_routes.user.OrderRouter import UserOrderRouter
from web_routes.admin.AuthRouter import AdminAuthRouter
from web_routes.admin.AdminUserRouter import AdminUserRouter
from web_routes.admin.CategoryRouter import CategoryRouter
from web_routes.admin.ItemRouter import AdminItemRouter
from web_routes.admin.AdminOrderRouter import AdminOrderRouter


def create_app():
    app = Flask(__name__,
                static_url_path="",
                template_folder="web/templates/",
                static_folder="web/static")
    app.debug = True
    app.register_blueprint(UserAuthRouter)
    app.register_blueprint(AdminAuthRouter)
    app.register_blueprint(AdminUserRouter)
    app.register_blueprint(CategoryRouter)
    app.register_blueprint(AdminItemRouter)
    app.register_blueprint(UserItemRouter)
    app.register_blueprint(UserCartRouter)
    app.register_blueprint(UserOrderRouter)
    app.register_blueprint(AdminOrderRouter)
    return app


init()
app = create_app()


@app.route("/", methods=["GET"])
def app_root():
    return redirect("/user/login")


if __name__ == "__main__":
    app.run()
