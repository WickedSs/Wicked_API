from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class CategoryBase(BaseModel):
    CategoryName: str
    key: str
    
# Properties to receive on Category creation
class CategoryCreate(CategoryBase):
    pass

# Properties to receive on Category update
class CategoryUpdate(CategoryBase):
    pass


# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):
    id: int
    CategoryName: str
    key: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Category(CategoryInDBBase):
    pass

# Properties properties stored in DB
class CategoryInDB(CategoryInDBBase):
    pass
