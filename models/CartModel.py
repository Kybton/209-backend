from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    ForeignKey
)

from sqlalchemy.dialects.mysql import INTEGER
from models.BaseModel import EntityMeta


class Cart(EntityMeta):
    __tablename__ = "carts"

    id = Column(INTEGER(unsigned=True), autoincrement=True)
    user_id = Column(INTEGER(unsigned=True),
                     ForeignKey("users.id"), nullable=False)
    PrimaryKeyConstraint(id)

    def json(self):
        return {
            "id": self.id.__str__(),
        }
