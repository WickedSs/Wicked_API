from typing import Mapping, Type
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from Settings import settings
from Models.Base_Models import Persistant, User
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

connection = settings.SQLALCHEMY_POSTGRES_DATABASE_URI if settings.SQLALCHEMY_MYSQL_DATABASE_URI == None else settings.SQLALCHEMY_MYSQL_DATABASE_URI
engine = create_engine(connection, pool_pre_ping=True)
Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
default_user(SessionLocal(), User)
default_persistant(SessionLocal(), Persistant)
Base = declarative_base()




