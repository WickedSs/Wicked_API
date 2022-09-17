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


@router.get("/product/{id}", response_model = Schema.Product)
def read_product(*, db: Session = Depends(Deps.get_db), id: int) -> Any:
    product_found = Database.Crud.product.read_single(db=db, id=id);
    return product_found


@router.get("/all_product", response_model = List[Schema.Product])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.product.read_all(db=db, skip=0, limit=50);
    return products_found


@router.put("/product/{id}", response_model = List[Schema.Product])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.product.update();
    return products_found


@router.delete("/product/{id}", response_model = List[Schema.Product])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.product.delete();
    return products_found