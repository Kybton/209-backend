from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    String,
)

from sqlalchemy.dialects.mysql import (
    INTEGER,
    # TINYINT,
    # TIMESTAMP
)

from models.BaseModel import EntityMeta


class User(EntityMeta):
    __tablename__ = "users"

    id = Column(INTEGER(unsigned=True), autoincrement=True)
    full_name = Column(String(255), nullable=False)
    email_address = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(INTEGER(unsigned=True), nullable=False)
    # is_banned = Column(TINYINT(unsigned=True), nullable=False)
    # banned_before = Column(TIMESTAMP, nullable=False)

    PrimaryKeyConstraint(id)

    def json(self):
        return {
            "id": self.id.__str__(),
            "full_name": self.full_name.__str__(),
            "email_address": self.email_address.__str__(),
            "is_admin": self.is_admin
        }
