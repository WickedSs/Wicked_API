from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Case
from Schema.Case_Schema import CaseCreate, CaseUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDCase(CRUDBase[Case, CaseCreate, CaseUpdate]):
    def __init__(self, model: Type[Case]):    
        super().__init__(model)
    
    def read_by_key(self, db: Session, key : str) -> List[Case]:
        return db.query(self.model).where(self.model.key == key).all()
        
        
case = CRUDCase(Case)