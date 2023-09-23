from flask import (
    Blueprint,
    request,
    redirect,
    render_template
)

from configs.Constants import ItemStatus, default_image_url
from configs.Database import SessionLocal
from models.ItemModel import Item
from models.CategoryModel import Category

AdminItemRouter = Blueprint("admin_item_router", __name__, url_prefix="/admin/items")

@AdminItemRouter.route("/", methods=["GET"])
def admin_item_index():
    with SessionLocal() as db:
        items = db.query(Item).all()
        
    data = []
    
    for item in items:
        d = item.json()

        if not d["img_url"]:
            d["img_url"] = default_image_url

        data.append(d)
    
    return render_template("admin/item-index.html", title="Items", data=data)


@AdminItemRouter.route("/", methods=["POST"])
def admin_item_add_new():
    item_name = request.form.get("name")
    item_price = request.form.get("price")
    item_total_quantity = int(request.form.get("total"))
    item_status = request.form.get("status")
    item_img_url = request.form.get("img_url")
    category_id = request.form.get("category")
    
    with SessionLocal() as db:
        item = Item(
            category_id = category_id,
            name = item_name,
            status = ItemStatus[item_status],
            available_quantity = item_total_quantity,
            hold_quantity = 0,
            total_quantity = item_total_quantity,
            price = item_price,
            img_url = item_img_url
        )
        
        db.add(item)
        db.commit()

    return redirect("/admin/items")


@AdminItemRouter.route("/add_new", methods=["GET"])
def admin_item_new():

    with SessionLocal() as db:
        categories = db.query(Category).all()
        
    data = []
    
    for category in categories:
        data.append(category.json())

    return render_template("admin/item-add-new.html", title="Add New Item", categories=data)


@AdminItemRouter.route("/<id>", methods=["GET"])
def admin_get_item_by_id(id: int):
    with SessionLocal() as db:
        item = db.get(Item, id)
        
    return render_template("admin/item-edit.html", title="Edit Item", data=item.json())

@AdminItemRouter.route("/<id>", methods=["POST"])
def admin_update_item_by_id(id: int):
    item_name = request.form.get("name")
    item_price = request.form.get("price")
    item_total_quantity = int(request.form.get("total"))
    item_status = request.form.get("status")
    item_img_url = request.form.get("img_url")
    
    if item_img_url == "None":
        item_img_url = None

    with SessionLocal() as db:
        item = db.get(Item, id)
        item.name = item_name
        item.price = item_price
        
        if item_total_quantity >= item.hold_quantity:
            item.total_quantity = item_total_quantity
            item.available_quantity = item.total_quantity - item.hold_quantity

        item.status = ItemStatus[item_status]
        item.img_url = item_img_url
        
        db.commit()
    
    return redirect("/admin/items")