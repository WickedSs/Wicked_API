from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    product_name: str
    category: str
    model: str
    barcode: str
    quantity: int
    imagePath: str = "default.png"
    price: float
    identifier: str
    sold: int
    bought: float
    market: float
    earned: float
    description: str
    product_link: str
    reference: str
    colors: str
    sizes: str
    material_link: str
    is_saved: str
    is_active: bool
    
# Properties to receive on Product creation
class ProductCreate(ProductBase):
    pass

# Properties to receive on Product update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    product_name: str
    category: str
    model: str
    barcode: str
    quantity: int
    imagePath: str = "default.png"
    price: float
    identifier: str
    sold: int
    bought: float
    market: float
    earned: float
    description: str
    product_link: str
    reference: str
    colors: str
    sizes: str
    material_link: str
    is_saved: str
    is_active: bool

    class Config:
        orm_mode = True

# Properties to return to client        
class Product(ProductInDBBase):
    pass

# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
