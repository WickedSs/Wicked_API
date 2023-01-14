from pydantic import BaseModel


# Shared properties
class ExpenseBase(BaseModel):
    expense_paid_by: str
    expense_category: str
    expense_note: str
    expense_amount: float
    expense_avatar: str
    expense_type: str
    expense_date: str
    expense_key: str
    
# Properties to receive on Expense creation
class ExpenseCreate(ExpenseBase):
    pass

# Properties to receive on Expense update
class ExpenseUpdate(ExpenseBase):
    pass


# Properties shared by models stored in DB
class ExpenseInDBBase(ExpenseBase):
    id: int
    expense_paid_by: str
    expense_category: str
    expense_note: str
    expense_amount: float
    expense_avatar: str
    expense_type: str
    expense_date: str
    expense_key: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Expense(ExpenseInDBBase):
    pass

# Properties properties stored in DB
class ExpenseInDB(ExpenseInDBBase):
    pass
