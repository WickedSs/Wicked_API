from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Expense
from Schema.Expense_Schema import ExpenseCreate, ExpenseUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDExpense(CRUDBase[Expense, ExpenseCreate, ExpenseUpdate]):
    def __init__(self, model: Type[Expense]):    
        super().__init__(model)
    
    def read_by_key(self, db: Session, key : str) -> List[Expense]:
        return db.query(self.model).where(self.model.key == key).all()
        
        
expense = CRUDExpense(Expense)