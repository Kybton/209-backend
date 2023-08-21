from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    ForeignKey,
    String
)

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.mysql import (
    INTEGER,
    TINYINT
)

from models.BaseModel import EntityMeta


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
    
    categories = relationship(
        "Category",
        lazy="dynamic"
    )
    
    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "status": self.status.__str__(),
            "available_quantity": self.available_quantity.__str__(),
            "hold_quantity": self.hold_quantity.__str__(),
            "total_quantity": self.total_quantity.__str__(),
            "price": self.price.__str__()
        }
