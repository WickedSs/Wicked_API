from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class InvoiceItemBase(BaseModel):
    item_name: str
    item_image: str
    item_price: float
    item_quantity: int
    item_identifier: str
    item_barcode: str
    is_manual: int
    reference: str
    item_size: str
    item_model: str
    
# Properties to receive on InvoiceItem creation
class InvoiceItemCreate(InvoiceItemBase):
    pass

# Properties to receive on InvoiceItem update
class InvoiceItemUpdate(InvoiceItemBase):
    pass


# Properties shared by models stored in DB
class InvoiceItemInDBBase(InvoiceItemBase):
    # id: int
    item_name: str
    item_image: str
    item_price: float
    item_quantity: int
    item_identifier: str
    item_barcode: str
    is_manual: int
    reference: str
    item_size: str
    item_model: str

    class Config:
        orm_mode = True

# Properties to return to client        
class InvoiceItem(InvoiceItemInDBBase):
    pass

# Properties properties stored in DB
class InvoiceItemInDB(InvoiceItemInDBBase):
    id: int
    pass
