from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from Database.Base import Base



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password_sha512 = Column(String, index=True)
    userRole = Column(String, index=True)
    

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    productName = Column(String, index=True)
    model = Column(String, index=True)
    barcode = Column(String, index=True)
    quantity = Column(Integer)
    imagePath = Column(String, index=True)
    price = Column(Float)
    identifier = Column(String, index=True)
    dimensions = Column(String, index=True)
    sold = Column(Integer)
    bought = Column(Float)
    market = Column(Float)
    earned = Column(Float)
    description = Column(String, index=True)
    link = Column(String, index=True)
    reference = Column(String, index=True)
    availableColors = Column(String, index=True)
    materialLink = Column(String, index=True)