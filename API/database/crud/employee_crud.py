from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Employee
from Schema.Employee_Schema import EmployeeCreate, EmployeeUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeUpdate]):
    def __init__(self, model: Type[Employee]):    
        super().__init__(model)
    
    def read_by_key(self, db: Session, key : str) -> List[Employee]:
        return db.query(self.model).where(self.model.key == key).all()
        
        
employee = CRUDEmployee(Employee)