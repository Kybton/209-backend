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

class OrderItem(EntityMeta):
    __tablename__ = "order_items"

    id = Column(INTEGER(unsigned=True), autoincrement=True)
    order_id = Column(INTEGER(unsigned=True), ForeignKey("orders.id"), nullable=False)
    item_id = Column(INTEGER(unsigned=True), ForeignKey("items.id"), nullable=False)
    price = Column(INTEGER(unsigned=True), nullable=False)
    quantity = Column(INTEGER(unsigned=True), nullable=False)
    total = Column(INTEGER(unsigned=True), nullable=False)
    
    order = relationship(
        "Order"
    )
    
    items = relationship(
        "Item"
    )
    
    PrimaryKeyConstraint(id)
    
    def json(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "item_id": self.item_id,
            "price": self.price,
            "quantity": self.quantity,
            "total": self.total
        }