from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Material
from Schema.Material_Schema import MaterialCreate, MaterialUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDMaterial(CRUDBase[Material, MaterialCreate, MaterialUpdate]):
    def __init__(self, model: Type[Material]):    
        super().__init__(model)
    
    def read_by_key(self, db: Session, key : str) -> List[Material]:
        return db.query(self.model).filter(self.model.materialKey == key).all()
    
    def read_by_link(self, db: Session, materialLink : str) -> List[Material]:
        return db.query(self.model).filter(self.model.materialKey == materialLink).all()
        
        
material = CRUDMaterial(Material)