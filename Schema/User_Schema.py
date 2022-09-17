from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    username: str
    userRole: str
    
# Properties to receive on Product creation
class UserCreate(UserBase):
    password_sha512: str

# Properties to receive on Product update
class UserUpdate(UserBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(UserBase):
    id: int
    username: str
    userRole: str

    class Config:
        orm_mode = True
        


class User(ProductInDBBase):
    pass


class UserInDB(ProductInDBBase):
    pass
