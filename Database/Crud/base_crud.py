from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Database.Base import Base
from Models.Base_Models import Product
from Schema.Product_Schema import ProductCreate


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
    
    def update(self, db: Session, *, db_obj: Model, obj_in: Union[UpdateSchema, Dict[str, Any]]) -> Model:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        return db_obj
    
    def delete(self, db: Session, id: int) -> Model:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return 
    