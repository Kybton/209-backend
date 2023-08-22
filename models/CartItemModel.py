from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.mysql import (
    INTEGER
)

from models.BaseModel import EntityMeta

class CartItem(EntityMeta):
    __tablename__ = "cart_items"
    
    id = Column(INTEGER(unsigned=True), autoincrement=True)
    cart_id = Column(INTEGER(unsigned=True), ForeignKey("carts.id"), nullable=False)
    item_id = Column(INTEGER(unsigned=True), ForeignKey("items.id"), nullable=False)
    quantity = Column(INTEGER(unsigned=True), nullable=False)
    
    cart = relationship(
        "Cart"
    )
    
    items = relationship(
        "Item"
    )
    
    PrimaryKeyConstraint(id)
    
    def json(self):
        return {
            "id": self.id,
            "cart_id": self.cart_id,
            "item_id": self.item_id,
            "quantity": self.quantity
        }