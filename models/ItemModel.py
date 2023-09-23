from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    ForeignKey,
    String
)

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.mysql import (
    INTEGER,
    TINYINT,
    TEXT
)

from models.BaseModel import EntityMeta
from configs.Constants import ItemStatus


class Item(EntityMeta):
    __tablename__ = "items"

    id = Column(INTEGER(unsigned=True), primary_key=True)
    category_id = Column(INTEGER(unsigned=True), ForeignKey("categories.id"))
    name = Column(String(255), nullable=False)
    status = Column(TINYINT(unsigned=True), nullable=False)
    available_quantity = Column(
        INTEGER(unsigned=True),
        nullable=False,
    )
    hold_quantity = Column(
        INTEGER(unsigned=True),
        nullable=False,
    )
    total_quantity = Column(
        INTEGER(unsigned=True),
        nullable=False,
    )
    price = Column(
        INTEGER(unsigned=True),
        nullable=False,
    )
    img_url = Column(
        TEXT
    )
    
    categories = relationship(
        "Category",
    )
    
    PrimaryKeyConstraint(id)

    def json(self):
        return {
            "id": self.id.__str__(),
            "category_id": self.category_id.__str__(),
            "name": self.name.__str__(),
            "status": list(filter(lambda x: ItemStatus[x] == self.status, ItemStatus))[0],
            "available_quantity": self.available_quantity.__str__(),
            "hold_quantity": self.hold_quantity.__str__(),
            "total_quantity": self.total_quantity.__str__(),
            "price": self.price.__str__(),
            "img_url": self.img_url
        }
