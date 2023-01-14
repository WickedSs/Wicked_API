from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    user_name: str
    user_type: str
    user_role: str
    user_key: str
    
# Properties to receive on Product creation
class UserCreate(UserBase):
    user_password: str

# Properties to receive on Product update
class UserUpdate(UserBase):
    user_refresh_token: str


# Properties shared by models stored in DB
class ProductInDBBase(UserBase):
    id: int
    user_name: str
    user_type: str
    user_role: str
    user_key: str

    class Config:
        orm_mode = True
        


class User(ProductInDBBase):
    pass


class UserInDB(ProductInDBBase):
    pass
