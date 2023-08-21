from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    String
)

from sqlalchemy.dialects.mysql import INTEGER

from models.BaseModel import EntityMeta


class Category(EntityMeta):
    __tablename__ = "categories"

    id = Column(INTEGER(unsigned=True), autoincrement=True)
    name = Column(String(255), nullable=False)

    PrimaryKeyConstraint(id)

    def json(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__()
        }
