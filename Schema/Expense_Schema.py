from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class ExpenseBase(BaseModel):
    creditCard: str
    serviceName: str
    note: str
    amount: float
    imagePath: str
    expenseType: str
    opDate: str
    key: str
    
# Properties to receive on Expense creation
class ExpenseCreate(ExpenseBase):
    pass

# Properties to receive on Expense update
class ExpenseUpdate(ExpenseBase):
    pass


# Properties shared by models stored in DB
class ExpenseInDBBase(ExpenseBase):
    id: int
    creditCard: str
    serviceName: str
    note: str
    amount: float
    imagePath: str
    expenseType: str
    opDate: str
    key: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Expense(ExpenseInDBBase):
    pass

# Properties properties stored in DB
class ExpenseInDB(ExpenseInDBBase):
    pass
