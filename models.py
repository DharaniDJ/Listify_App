from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    items = relationship("Items",back_populates="owner") # owner is variable declared in items model relationship

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User",back_populates="items") # items is variable declared in User model relationship

