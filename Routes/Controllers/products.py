from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Product_Schema import Product, ProductUpdate
from Routes.Response_models import *



router = APIRouter()

@router.post("/product")
def create_product(*, db: Session = Depends(Deps.get_db), product_in: List[Schema.ProductCreate]) -> ResponseSuccess:
    """ Create new Product """
    result = Database.Crud.product.create(db, product_in);
    return ResponseSuccess(
        message = "Products [ " + (", ".join(prod.productName for prod in product_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


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
def read_products(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = Database.Crud.product.read_by_key(db=db, key=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="No product exist with name or barcode {}!".format(key))
    return product_found


@router.get("/product_quantity/{quantity}", response_model = List[Schema.Product])
def read_products(*, db: Session = Depends(Deps.get_db), quantity: int) -> Any:
    product_found = Database.Crud.product.read_by_quantity(db=db, quantity=quantity);
    if not product_found:
        raise HTTPException(status_code=400, detail="No product exist with with a quantity less or equal to {}!".format(quantity))
    return product_found


@router.get("/product_link/{link}", response_model = List[Schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db), link: str) -> Any:
    product_found = Database.Crud.product.read_by_link(db=db, link=link);
    if not product_found:
        raise HTTPException(status_code=400, detail="No product exist with name or barcode {}!".format(link))
    return product_found


@router.get("/product", response_model = List[Schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.product.read_all(db=db, skip=0, limit=50);
    return products_found


@router.put("/product/{key}")
def update_product(*, db: Session = Depends(Deps.get_db), key: Any, product_in: ProductUpdate) -> Any:
    old_product = Database.Crud.product.read_by_id(db=db, id=key)
    print("ObjectIn: ", product_in.productName, "OldObject: ", old_product.productName)
    if not old_product:
        return ResponseFail(
            message = "Product [ {} ] does not exist!".format(key),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newProduct = Database.Crud.product.update(db=db, db_obj=old_product, obj_in=product_in);
    return ResponseSuccess(
        message = "Product [ {} -> {} ] was updated successfully!".format(old_product.identifier, newProduct.identifier),
        status_code=status.HTTP_200_OK
    )

@router.delete("/product/{key}", response_model = Schema.Product)
def delete_product(*, db: Session = Depends(Deps.get_db), key: Any):
    products_found = Database.Crud.product.read_by_key(db=db, key=key);
    if not products_found:
        return ResponseFail(
            message = "Product [ {} ] does not exist!".format(key),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.product.delete(db=db, id=products_found.id)
    return ResponseSuccess(
        message = "Product [ {} ] was deleted successfully!".format(products_found.productName),
        status_code=status.HTTP_200_OK
    )