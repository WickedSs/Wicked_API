from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import InvoiceItem
from Schema.InvoiceItem_Schema import InvoiceItemCreate, InvoiceItemUpdate
from typing import Type
from sqlalchemy.orm import Session

class CRUDInvoiceItem(CRUDBase[InvoiceItem, InvoiceItemCreate, InvoiceItemUpdate]):
    def __init__(self, model: Type[InvoiceItem]):    
        super().__init__(model)
    
    def read_by_buyer(self, db: Session, buyer : str) -> List[InvoiceItem]:
        return db.query(self.model).where(self.model.buyer.startswith(buyer)).all()
    
    def read_by_identifier(self, db: Session, identifier : str) -> List[InvoiceItem]:
        return db.query(self.model).where(self.model.identifier == identifier).all()
    
    def delete_by_identifier(self, db: Session, identifier : str) -> List[InvoiceItem]:
        objs = db.query(self.model).filter(self.model.identifier == identifier).all()
        for obj in objs:
            db.delete(obj)
        db.commit()
        return objs
    
    def create(self, db: Session, invoiceItems_in: List[InvoiceItemCreate]):
        for invoiceItem in invoiceItems_in:
            new_db_InvoiceItem = InvoiceItem(
                productName = invoiceItem.productName,
                imagePath = invoiceItem.imagePath,
                price = invoiceItem.price,
                quantity = invoiceItem.quantity,
                total = invoiceItem.total,
                identifier = invoiceItem.identifier,
                respectiveBarcode = invoiceItem.respectiveBarcode,
                isManual = invoiceItem.isManual,
                reference = invoiceItem.reference,
                color = invoiceItem.color,
                model = invoiceItem.model
            )
            db.add(new_db_InvoiceItem)
            db.commit()
        return {"Success" : "InvoiceItems Added!"}
        
invoiceItem = CRUDInvoiceItem(InvoiceItem)