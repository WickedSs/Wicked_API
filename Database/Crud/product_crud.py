from Routes.Security import get_password_hash, verify_password
from Database.Crud.base_crud import CRUDBase
from Models.Base_Models import Product
from Schema.Product_Schema import ProductCreate, ProductUpdate
from typing import Type


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def __init__(self, model: Type[Product]):    
        super().__init__(model)
        
    def __call__(self) -> str:
        return Product.id + " " + Product.productName + " " + Product.price + " " + Product.barcode
        

product = CRUDProduct(Product)
