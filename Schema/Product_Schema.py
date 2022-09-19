from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    productName: str
    model: str
    barcode: str
    quantity: int
    imagePath: str = "default.png"
    price: float
    identifier: str
    dimensions: str
    sold: int
    bought: float
    market: float
    earned: float
    description: str
    link: str
    reference: str
    availableColors: str
    materialLink: str
    
# Properties to receive on Product creation
class ProductCreate(ProductBase):
    pass

# Properties to receive on Product update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    productName: str
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
    link: str
    reference: str
    availableColors: str
    materialLink: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Product(ProductInDBBase):
    pass

# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
