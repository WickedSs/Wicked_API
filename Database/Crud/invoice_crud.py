from typing import Any, Dict, Optional, Union, List
from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Invoice
from Schema.Invoice_Schema import InvoiceCreate, InvoiceUpdate
from typing import Type
from sqlalchemy.orm import Session

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
        
        
invoice = CRUDInvoice(Invoice)