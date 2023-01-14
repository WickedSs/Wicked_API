from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Invoice
from Schema.Invoice_Schema import InvoiceCreate, InvoiceUpdate
from typing import Type
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, not_
from Schema.Product_Schema import ProductCreate

class CRUDInvoice(CRUDBase[Invoice, InvoiceCreate, InvoiceUpdate]):
    def __init__(self, model: Type[Invoice]):    
        super().__init__(model)
    
    def read_by_buyer(self, db: Session, buyer : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.buyer_name.startswith(buyer)).all()
    
    def read_by_exact_date(self, db: Session, date : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.operation_date == date).all()
    
    def read_by_date(self, db: Session, date : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.operation_date.contains(date)).all()
    
    def read_by_number(self, db: Session, number : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.invoice_number == number).all()
    
    def read_by_register(self, db: Session, registry : str) -> List[Invoice]:
        return db.query(self.model).where(self.model.trade_registry == registry).all()
    
    def read_by_identifier(self, db: Session, identifier : str) -> Invoice:
        return db.query(self.model).where(self.model.invoice_identifier == identifier).first()
    
    def read_by_buyer_and_register(self, db: Session, buyer: str, register : str) -> List[Invoice]:
        return db.query(self.model).where(and_(self.model.trade_registry == register, self.model.buyer_name.contains(buyer))).all()
    
    def create(self, db: Session, invoice_in: InvoiceCreate):
        new_db_invoice = Invoice(
            buyer_name = invoice_in.buyer_name,
            buyer_address = invoice_in.buyer_address,
            operation_date = invoice_in.operation_date,
            invoice_total = invoice_in.invoice_total,
            amount_paid = invoice_in.amount_paid,
            amount_remaining = invoice_in.amount_remaining,
            invoice_identifier = invoice_in.invoice_identifier,
            purchase_order = invoice_in.purchase_order,
            purchase_order_date = invoice_in.purchase_order_date,
            purchase_form = invoice_in.purchase_form,
            purchase_form_date = invoice_in.purchase_form_date,
            invoice_number = invoice_in.invoice_number,
            trade_registry = invoice_in.trade_registry,
            is_validated = invoice_in.is_validated,
            validation_deadline = invoice_in.validation_deadline,
            invoice_note = invoice_in.invoice_note,
            invoice_tax = invoice_in.invoice_tax,
            invoice_tax_price = invoice_in.invoice_tax_price,
            is_delivered = invoice_in.is_delivered,
            invoice_discount = invoice_in.invoice_discount,
        )
        db.add(new_db_invoice)
        db.commit()
        return {"Success" : "Invoice Added!"}
    
    def delete_by_identifier(self, db: Session, identifier : str) -> List[Invoice]:
        obj = db.query(self.model).filter(self.model.identifier == identifier).all()
        db.delete(obj)
        db.commit()
        return obj
        
        
invoice = CRUDInvoice(Invoice)