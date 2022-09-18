from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Database.Base import Base


Model = TypeVar("Model", bound=Base)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class CRUDBase(Generic[Model, CreateSchema, UpdateSchema]):
    def __init__(self, model: Type[Model]):
        self.model = model
        
    def read_by_id(self, db: Session, id : int) -> Optional[Model]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def read_all(self, db: Session, skip: int = 0, limit: int = 5000) -> List[Model]:
        return db.query(self.model).offset(skip).limit(limit).all()
    
    def create(self):
        return
    
    def update(self):
        return
    
    def delete(self):
        return
    