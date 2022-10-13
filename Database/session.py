from pyexpat import model
from statistics import mode
from typing import Mapping, Tuple, Type
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from Settings import settings
from Models.Base_Models import Persistant, Product, User
from Database.Base import Base
from Routes.Security import get_password_hash


def default_user(db: Session, model: Type[User]):
    default_exist = db.query(model).filter(model.username == "Root").first()
    if not default_exist:
        default = User(
            username = "Root",
            password_sha512 = get_password_hash("toor"),
            userRole = "Admin"       
        )
        db.add(default)
        db.commit()

def default_persistant(db: Session, model: Type[Persistant]):
    default_exist = db.query(model).filter(model.id == 1).first()
    if not default_exist:
        default = Persistant(
            percentageOff = 10,
            benefitPercentage = 30,
            stockOff = 5        
        )
        db.add(default)
        db.commit()

def default_product(db: Session, model: Type[Product]):
    default_exist = db.query(model).filter(model.product_name == "Default Product").first()
    if not default_exist:
        default = Product(
            id=1,
            product_name = "Default Product",
            model = "Model",
            barcode = "0000001",
            quantity = 999,
            imagePath = "default.png",
            price = 1000.00,
            identifier = "abcdefjh",
            sold = 0,
            bought = 500.00,
            market = 950.00,
            earned = 0,
            description = "Default Product to send on first request!",
            product_link = "AAAAAAAA",
            reference = "BBBBBBBB",
            colors = "Black",
            sizes = "",
            material_link = "CCCCCCCCCC",
            is_active = True,
            is_saved = ""
        )
        db.add(default)
        db.commit()

connection = settings.SQLALCHEMY_POSTGRES_DATABASE_URI if settings.SQLALCHEMY_MYSQL_DATABASE_URI == None else settings.SQLALCHEMY_MYSQL_DATABASE_URI
engine = create_engine(connection, pool_pre_ping=True)
Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

local_session = SessionLocal()
default_user(local_session, User)
default_persistant(local_session, Persistant)
default_product(local_session, Product)

Base = declarative_base()




