from pydantic import BaseModel


# Shared properties
class CategoryBase(BaseModel):
    category_name: str
    category_key: str
    
# Properties to receive on Category creation
class CategoryCreate(CategoryBase):
    pass

# Properties to receive on Category update
class CategoryUpdate(CategoryBase):
    pass


# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):
    id: int
    category_name: str
    category_key: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Category(CategoryInDBBase):
    pass

# Properties properties stored in DB
class CategoryInDB(CategoryInDBBase):
    pass
