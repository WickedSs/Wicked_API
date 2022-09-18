from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Product
from Schema.Product_Schema import ProductCreate, ProductUpdate
from typing import Type, Optional, List, Any
from sqlalchemy.orm import Session


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def __init__(self, model: Type[Product]):    
        super().__init__(model)
    
    def read_by_barcode(self, db: Session, barcode : str) -> Optional[Product]:
        return db.query(self.model).filter(self.model.barcode == barcode).first()
    
    def read_by_name(self, db: Session, name : str) -> List[Product]:
        return db.query(self.model).filter(self.model.productName.startswith(name)).all()
    
    def read_by_key(self, db: Session, key : Any) -> List[Product]:
        return db.query(self.model).where((self.model.productName.startswith(str(key))) | (self.model.barcode == str(key))).all()
    
    def __call__(self) -> str:
        return Product.id + " " + Product.productName + " " + Product.price + " " + Product.barcode
        

product = CRUDProduct(Product)
