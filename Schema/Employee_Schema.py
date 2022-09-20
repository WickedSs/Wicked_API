from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class EmployeeBase(BaseModel):
    fullname: str
    birthday: str
    avatar: str = "default.png"
    telephone: str
    employedAt: str
    monthlyPayment: float
    salary: float
    specialKey: str
    
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
    rfid: str
    fullname: str
    birthday: str
    avatar: str = "default.png"
    telephone: str
    employedAt: str
    monthlyPayment: float
    salary: float
    specialKey: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Employee(EmployeeInDBBase):
    pass

# Properties properties stored in DB
class EmployeeInDB(EmployeeInDBBase):
    pass
