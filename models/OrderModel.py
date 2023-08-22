from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    ForeignKey,
    String,
)

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.mysql import (
    INTEGER,
    TIMESTAMP
)

from models.BaseModel import EntityMeta

class Order(EntityMeta):
    __tablename__ = "orders"
    
    id = Column(INTEGER(unsigned=True), autoincrement=True)
    uesr_id = Column(INTEGER(unsigned=True), ForeignKey("users.id"), nullable=False)
    status = Column(INTEGER(unsigned=True), nullable=False)
    delivery_address = Column(String(255), nullable=False)
    contact_number = Column(String(255), nullable=False)
    order_time = Column(TIMESTAMP, nullable=False)
    remark = Column(String(255))
    
    users = relationship(
        "User"
    )
    
    PrimaryKeyConstraint(id) 
    
    def json(self):
        return {
            "id": self.id,
            "user_id": self.uesr_id,
            "status": self.status,
            "delivery_address": self.delivery_address,
            "contact_number": self.contact_number,
            "ordered_time": self.ordered_time,
            "remark": self.remark
        }