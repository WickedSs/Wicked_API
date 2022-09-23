from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Invoice
from Schema.Invoice_Schema import InvoiceCreate, InvoiceUpdate
from typing import Type
from sqlalchemy.orm import Session

from Schema.Product_Schema import ProductCreate

class CRUDInvoice(CRUDBase[Invoice, InvoiceCreate, InvoiceUpdate]):
    def __init__(self, model: Type[Invoice]):    
        super().__init__(model)
    
    def read_by_buyer(self, db: Session, buyer : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.buyer.startswith(buyer)).all()
    
    def read_by_date(self, db: Session, date : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.opDate.contains(date)).all()
    
    def read_by_number(self, db: Session, number : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.factureNumber == number).all()
    
    def read_by_register(self, db: Session, register : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.invoiceRegister == register).all()
    
    def create(self, db: Session, invoice_in: InvoiceCreate):
        new_db_invoice = Invoice(
            buyer = invoice_in.buyer,
            opDate = invoice_in.opDate,
            amount = invoice_in.amount,
            paid = invoice_in.paid,
            remaining = invoice_in.remaining,
            identifier = invoice_in.identifier,
            bc = invoice_in.bc,
            bcdate = invoice_in.bcdate,
            bl = invoice_in.bl,
            bldate = invoice_in.bldate,
            factureNumber = invoice_in.factureNumber,
            invoiceRegister = invoice_in.invoiceRegister,
            validated = invoice_in.validated,
            validationDate = invoice_in.validationDate,
            note = invoice_in.note,
            tva = invoice_in.tva,
            factureTVA = invoice_in.factureTVA,
            address = invoice_in.address,
        )
        db.add(new_db_invoice)
        db.commit()
        return {"Success" : "Invoice Added!"}
        
        
invoice = CRUDInvoice(Invoice)