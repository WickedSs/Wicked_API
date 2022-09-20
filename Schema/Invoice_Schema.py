from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class InvoiceBase(BaseModel):
    buyer: str
    opDate: str
    amount: float
    paid: float
    remaining: float
    identifier: str
    BC: str
    BCdate: str
    BL: str
    BLdate: str
    factureNumber: str
    invoiceRegister: str
    validated: int
    validationDate: str
    note: str
    TVA: str
    FactureTVA: float
    address: str
    
# Properties to receive on Invoice creation
class InvoiceCreate(InvoiceBase):
    pass

# Properties to receive on Invoice update
class InvoiceUpdate(InvoiceBase):
    pass


# Properties shared by models stored in DB
class InvoiceInDBBase(InvoiceBase):
    id: int
    buyer: str
    opDate: str
    amount: float
    paid: float
    remaining: float
    identifier: str
    BC: str
    BCdate: str
    BL: str
    BLdate: str
    factureNumber: str
    invoiceRegister: str
    validated: int
    validationDate: str
    note: str
    TVA: str
    FactureTVA: float
    address: str

    class Config:
        orm_mode = True

# Properties to return to client        
class Invoice(InvoiceInDBBase):
    pass

# Properties properties stored in DB
class InvoiceInDB(InvoiceInDBBase):
    pass
