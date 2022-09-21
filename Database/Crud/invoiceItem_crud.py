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
        
        
invoiceItem = CRUDInvoiceItem(InvoiceItem)