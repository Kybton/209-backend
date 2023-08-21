from flask import Flask
from models.BaseModel import init
from routers.UserRouter import UserRouter
from routers.CartRouter import CartRouter
from routers.CategoryRouter import CategoryRouter
from routers.ItemRouter import ItemRouter

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(UserRouter)
    app.register_blueprint(CartRouter)
    app.register_blueprint(CategoryRouter)
    app.register_blueprint(ItemRouter)
    return app


init()
app = create_app()

if __name__ == "__main__":
    app.run()