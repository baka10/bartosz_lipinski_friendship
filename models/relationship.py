from sqlalchemy import Column, String
from db import Base


class RelationShip(Base):
    __tablename__ = "users"
    from_user = Column(String(6), primary_key=True)
    to_user = Column(String(6), unique=True)

    def __init__(self, from_user=None, to_user=None):
        self.from_user = from_user
        self.to_user = to_user

    def __repr__(self):
        return f"<RelationShip from {self.from_user} to {self.to_user}"
