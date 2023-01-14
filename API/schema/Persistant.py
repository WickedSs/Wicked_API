from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class PersistantBase(BaseModel):
    percentageOff: int
    benefitPercentage: int
    stockOff: int
    
# Properties to receive on Persistant creation
class PersistantCreate(PersistantBase):
    pass

# Properties to receive on Persistant update
class PersistantUpdate(PersistantBase):
    pass


# Properties shared by models stored in DB
class PersistantInDBBase(PersistantBase):
    id: int
    percentageOff: int
    benefitPercentage: int
    stockOff: int

    class Config:
        orm_mode = True

# Properties to return to client        
class Persistant(PersistantInDBBase):
    pass

# Properties properties stored in DB
class PersistantInDB(PersistantInDBBase):
    pass
