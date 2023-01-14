from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class EmployeeBase(BaseModel):
    fullname: str
    started_at: str
    stopped_at: str
    employee_key: str
    monthly_salary: str
    birthday: str
    monthly_expenses: float
    phone_number: str
    avatar: str
    
# Properties to receive on Employee creation
class EmployeeCreate(EmployeeBase):
    rfid: str
    pass

# Properties to receive on Employee update
class EmployeeUpdate(EmployeeBase):
    pass


# Properties shared by models stored in DB
class EmployeeInDBBase(EmployeeBase):
    id: int
    fullname: str
    started_at: str
    stopped_at: str
    employee_key: str
    monthly_salary: str
    birthday: str
    monthly_expenses: float
    phone_number: str
    avatar: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Employee(EmployeeInDBBase):
    pass

# Properties properties stored in DB
class EmployeeInDB(EmployeeInDBBase):
    pass
