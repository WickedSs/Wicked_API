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



[
  {
    "productName": "Protein C4 v5",
    "model": "Model-01",
    "barcode": "1526482",
    "quantity": 10,
    "imagePath": "default.png",
    "price": 12000.00,
    "identifier": "dlkjjijlml^zed",
    "dimensions": "10D 25W 15H",
    "sold": 0,
    "bought": 9800.00,
    "market": 12500.00,
    "earned": 0,
    "description": "Loading ...",
    "link": "dzqeq224ze",
    "reference": "dzz",
    "availableColors": "White",
    "materialLink": "dddzz5555"
  }
]