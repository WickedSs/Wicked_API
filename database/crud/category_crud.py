from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Category
from Schema.Category_Schema import CategoryCreate, CategoryUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def __init__(self, model: Type[Category]):    
        super().__init__(model)
    
    def read_by_key(self, db: Session, key : str) -> List[Category]:
        return db.query(self.model).where(self.model.key == key).all()
        
        
category = CRUDCategory(Category)