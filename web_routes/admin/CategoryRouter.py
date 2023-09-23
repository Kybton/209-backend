from flask import (
    Blueprint,
    request,
    redirect,
    render_template
)

from configs.Database import SessionLocal
from models.CategoryModel import Category

CategoryRouter = Blueprint("admin_category_router", __name__, url_prefix="/admin/category")

@CategoryRouter.route("/", methods=["GET"])
def get_category():
    with SessionLocal() as db:
        categories = db.query(Category).all()
        
    data = []

    for category in categories:
        data.append(category.json())

    return render_template("admin/category.html", data=data)

@CategoryRouter.route("/", methods=["POST"])
def update_or_add_category():
    category_id = request.form.get("id")
    category_name = request.form.get("name")

    with SessionLocal() as db:
        # add new 
        if (len(category_id) == 0):
            category = Category(name=category_name)
            db.add(category)
        # update
        else:
            category = db.get(Category, category_id)
            category.name = category_name
        
        db.commit()
    
    return redirect("/admin/category")
