from os import link
from pyexpat import model
from xml.dom.minidom import Identified
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
    
    def read_by_link(self, db: Session, link : Any) -> List[Product]:
        return db.query(self.model).filter(self.model.link == link).all()
    
    def create(self, db: Session, product_in: List[ProductCreate]) -> str:
        for product in product_in:
            new_db_product = Product(
                productName = product.productName,
                model = product.model,
                barcode = product.barcode,
                quantity = product.quantity,
                imagePath = product.imagePath,
                price = product.price,
                identifier = product.identifier,
                sold = product.sold,
                bought = product.bought,
                market = product.market,
                earned = 0,
                description = "",
                link = product.link,
                reference = product.reference,
                availableColors = product.availableColors,
                materialLink = product.materialLink   
            )
            db.add(new_db_product)
            db.commit()
        return {"Success" : "Products Added!"}
    
    def __call__(self) -> str:
        return Product.id + " " + Product.productName + " " + Product.price + " " + Product.barcode
        

product = CRUDProduct(Product)
