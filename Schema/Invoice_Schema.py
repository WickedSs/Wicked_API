from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class InvoiceBase(BaseModel):
    buyer_name : str
    buyer_address : str
    operation_date : str
    invoice_total : float
    amount_paid : float
    amount_remaining : float
    invoice_identifier : str
    purchase_order : str
    purchase_order_date : str
    purchase_form : str
    purchase_form_date : str
    invoice_number : str
    trade_registry : str
    is_validated : bool
    validation_deadline : str
    invoice_note : str
    invoice_tax : str
    invoice_tax_price : float
    is_delivered : bool
    invoice_discount : int
    
# Properties to receive on Invoice creation
class InvoiceCreate(InvoiceBase):
    pass

# Properties to receive on Invoice update
class InvoiceUpdate(InvoiceBase):
    pass


# Properties shared by models stored in DB
class InvoiceInDBBase(InvoiceBase):
    # id: int
    buyer_name : str
    buyer_address : str
    operation_date : str
    invoice_total : float
    amount_paid : float
    amount_remaining : float
    invoice_identifier : str
    purchase_order : str
    purchase_order_date : str
    purchase_form : str
    purchase_form_date : str
    invoice_number : str
    trade_registry : str
    is_validated : bool
    validation_deadline : str
    invoice_note : str
    invoice_tax : str
    invoice_tax_price : float
    is_delivered : bool
    invoice_discount : int

    class Config:
        orm_mode = True

# Properties to return to client        
class Invoice(InvoiceInDBBase):
    pass

# Properties properties stored in DB
class InvoiceInDB(InvoiceInDBBase):
    id: int
    pass
