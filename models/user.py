from sqlalchemy import Column, String
from db import Base
from utils import generic


class User(Base):
    __tablename__ = "users"
    id = Column(
        String(6), primary_key=True, default=generic.generator.random_6_digit_number
    )
    name = Column(String(50), unique=True, defaut=generic.person.name)
    email = Column(String(120), unique=True, default=generic.person.email)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User {self.name}: {self.email} - {self.email}>"
