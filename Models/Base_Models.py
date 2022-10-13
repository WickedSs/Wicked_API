from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Numeric
from sqlalchemy.orm import relationship
from Database.Base import Base
import sqlalchemy.types as types
from decimal import Decimal as D


class SqliteNumeric(types.TypeDecorator):
    impl = types.String
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(types.VARCHAR(100))
    def process_bind_param(self, value, dialect):
        return str(value)
    def process_result_value(self, value, dialect):
        return D(value)



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password_sha512 = Column(String, index=True)
    userRole = Column(String, index=True)
    

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    model = Column(String, index=True)
    barcode = Column(String, index=True)
    quantity = Column(Integer)
    imagePath = Column(String, index=True)
    price = Column(Numeric(12, 2), index=True)
    identifier = Column(String, index=True)
    sold = Column(Integer)
    bought = Column(Numeric(12, 2), index=True)
    market = Column(Numeric(12, 2), index=True)
    earned = Column(Numeric(12, 2), index=True)
    description = Column(String, index=True)
    product_link = Column(String, index=True)
    reference = Column(String, index=True, nullable=True, default="")
    colors = Column(String, index=True)
    sizes = Column(String, index=True)
    material_link = Column(String, index=True)
    is_active = Column(Boolean, index=True)
    is_saved = Column(String, index=True)

class Case(Base):
    __tablename__ = "cases"
    
    id = Column(Integer, primary_key=True, index=True)
    caseName = Column(String, index=True)
    key = Column(String, index=True)


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    CategoryName = Column(String, index=True)
    key = Column(String, index=True)


class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    rfid = Column(String, index=True)
    fullname = Column(String, index=True)
    birthday = Column(String, index=True, nullable=True, default="")
    avatar = Column(String, index=True)
    telephone = Column(String, index=True, nullable=True, default="")
    employedAt = Column(String, index=True)
    monthlyPayment = Column(Numeric(12, 2), index=True)
    salary = Column(Numeric(12, 2), index=True)
    specialKey = Column(String, index=True)

  
class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    creditCard = Column(String, index=True)
    serviceName = Column(String, index=True)
    note = Column(String, index=True, nullable=True, default="")
    amount = Column(Numeric(12, 2), index=True)
    imagePath = Column(String, index=True)
    expenseType = Column(String, index=True)
    opDate = Column(String, index=True)
    key = Column(String, index=True)
 
   
class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    buyer_name = Column(String, index=True)
    buyer_address = Column(String, index=True, nullable=True, default="")
    operation_date = Column(String, index=True)
    invoice_total = Column(Numeric(12, 2), index=True)
    amount_paid = Column(Numeric(12, 2), index=True)
    amount_remaining = Column(Numeric(12, 2), index=True)
    invoice_identifier = Column(String, index=True)
    purchase_order = Column(String, index=True)
    purchase_order_date = Column(String, index=True)
    purchase_form = Column(String, index=True)
    purchase_form_date = Column(String, index=True)
    invoice_number = Column(String, index=True)
    trade_registry = Column(String, index=True)
    is_validated = Column(Boolean, index=True)
    validation_deadline = Column(String, index=True)
    invoice_note = Column(String, index=True, nullable=True, default="")
    invoice_tax = Column(String, index=True)
    invoice_tax_price = Column(Numeric(12, 2), index=True)
    is_delivered = Column(Boolean, index=True)
    invoice_discount = Column(Integer, index=True)


class InvoiceItem(Base):
    __tablename__ = "invoiceitems"
    
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    item_image = Column(String, index=True)
    item_price = Column(Numeric(12, 2), index=True)
    item_quantity = Column(Integer, index=True)
    item_identifier = Column(String, index=True)
    item_barcode = Column(String, index=True)
    is_manual = Column(Integer, index=True)
    reference = Column(String, index=True)
    item_size = Column(String, index=True, nullable=True, default="")
    item_model = Column(String, index=True, nullable=True, default="")


class Material(Base):
    __tablename__ = "materials"
    
    id = Column(Integer, primary_key=True, index=True)
    materialName = Column(String, index=True)
    materialType = Column(String, index=True)
    materialPrice = Column(Numeric(12, 2), index=True)
    materialQte = Column(Integer, index=True)
    materialKey = Column(String, index=True)
    
    

class Persistant(Base):
    __tablename__ = "persistants"
    
    id = Column(Integer, primary_key=True, index=True)
    percentageOff = Column(Integer, index=True)
    benefitPercentage = Column(Integer, index=True)
    stockOff = Column(Integer, index=True)