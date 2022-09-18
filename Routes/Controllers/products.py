from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Product_Schema import Product

router = APIRouter()


@router.post("/product", response_model = Schema.Product)
def create_product(*, db: Session = Depends(Deps.get_db), product_in: List[Schema.ProductCreate]) -> Any:
    """ Create new Product """
    return "Working... [New Product Create]"


@router.get("/product_id/{key}", response_model = Schema.Product)
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = Database.Crud.product.read_by_id(db=db, id=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="Product does not exist!")
    return product_found


@router.get("/product_barcode/{key}", response_model = Schema.Product)
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = Database.Crud.product.read_by_barcode(db=db, barcode=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="Product does not exist!")
    return product_found

@router.get("/product_name/{key}", response_model = List[Schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = Database.Crud.product.read_by_name(db=db, name=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="Product does not exist!")
    return product_found

@router.get("/product_key/{key}", response_model = List[Schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = Database.Crud.product.read_by_key(db=db, key=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="No product exist with name or barcode {}!".format(key))
    return product_found


@router.get("/product", response_model = List[Schema.Product])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.product.read_all(db=db, skip=0, limit=50);
    return products_found


@router.put("/product/{key}", response_model = List[Schema.Product])
def read_products(*, db: Session = Depends(Deps.get_db), key: Any):
    products_found = Database.Crud.product.update();
    return products_found


@router.delete("/product/{key}", response_model = List[Schema.Product])
def read_products(*, db: Session = Depends(Deps.get_db), key: Any):
    products_found = Database.Crud.product.delete();
    return products_found