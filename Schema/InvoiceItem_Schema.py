from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class InvoiceItemBase(BaseModel):
    productName: str
    imagePath: str
    price: float
    quantity: int
    total: float
    identifier: str
    respectiveBarcode: str
    isManual: int
    reference: str
    color: str
    model: str
    
# Properties to receive on InvoiceItem creation
class InvoiceItemCreate(InvoiceItemBase):
    pass

# Properties to receive on InvoiceItem update
class InvoiceItemUpdate(InvoiceItemBase):
    pass


# Properties shared by models stored in DB
class InvoiceItemInDBBase(InvoiceItemBase):
    id: int
    productName: str
    imagePath: str
    price: float
    quantity: int
    total: float
    identifier: str
    respectiveBarcode: str
    isManual: int
    reference: str
    color: str
    model: str

    class Config:
        orm_mode = True

# Properties to return to client        
class InvoiceItem(InvoiceItemInDBBase):
    pass

# Properties properties stored in DB
class InvoiceItemInDB(InvoiceItemInDBBase):
    pass
