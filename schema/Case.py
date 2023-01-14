from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class CaseBase(BaseModel):
    caseName: str
    key: str
    
# Properties to receive on Case creation
class CaseCreate(CaseBase):
    pass

# Properties to receive on Case update
class CaseUpdate(CaseBase):
    pass


# Properties shared by models stored in DB
class CaseInDBBase(CaseBase):
    id: int
    caseName: str
    key: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Case(CaseInDBBase):
    pass

# Properties properties stored in DB
class CaseInDB(CaseInDBBase):
    pass
