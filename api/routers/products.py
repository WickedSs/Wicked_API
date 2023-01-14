from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database.crud, schema, models
from api import Deps
from schema import *

router = APIRouter()

@router.post("/product")
def create_product(*, db: Session = Depends(Deps.get_db), product_in: List[schema.ProductCreate]) -> ResponseSuccess:
    """ Create new Product """
    result = database.crud.product.create(db, product_in);
    return ResponseSuccess(
        message = f"Products [{', '.join(prod.productName for prod in product_in)}] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.put("/product/reduce_quantity/{barcode}")
def reduce_quantity(*, db: Session = Depends(Deps.get_db), barcode: str, sold_quantity: int) -> ResponseSuccess:
    """ update product with the new quantity """
    old_product = database.crud.product.read_by_barcode(db=db, barcode=barcode)
    if not old_product:
        return ResponseFail(message = f"Product [{barcode}] does not exist!", status_code = status.HTTP_400_BAD_REQUEST)
    old_product.quantity -= sold_quantity
    db.commit()
    return ResponseSuccess(
        message = f"Product [{old_product.product_name}] quantity was updated succesfully!",
        status_code = status.HTTP_200_OK,
    )

@router.get("/product_id/{key}", response_model = schema.Product)
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = database.crud.product.read_by_id(db=db, id=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="Product does not exist!")
    return product_found


@router.get("/product_barcode/{key}", response_model = schema.Product)
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = database.crud.product.read_by_barcode(db=db, barcode=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="Product does not exist!")
    return product_found

@router.get("/product_name/{key}", response_model = List[schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = database.crud.product.read_by_name(db=db, name=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="Product does not exist!")
    return product_found

@router.get("/product_key/{key}", response_model = List[schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db), key: Any) -> Any:
    product_found = database.crud.product.read_by_key(db=db, key=key);
    if not product_found:
        raise HTTPException(status_code=400, detail="No product exist with name or barcode {}!".format(key))
    return product_found


@router.get("/product_quantity/{quantity}", response_model = List[schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db), quantity: int) -> Any:
    product_found = database.crud.product.read_by_quantity(db=db, quantity=quantity);
    if not product_found:
        raise HTTPException(status_code=400, detail="No product exist with with a quantity less or equal to {}!".format(quantity))
    return product_found


@router.get("/product_link/{link}", response_model = List[schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db), link: str) -> Any:
    product_found = database.crud.product.read_by_link(db=db, link=link);
    if not product_found:
        raise HTTPException(status_code=400, detail="No product exist with name or barcode {}!".format(link))
    return product_found


@router.get("/product_default", response_model = schema.Product)
def read_product(*, db: Session = Depends(Deps.get_db)) -> Any:
    product_found = database.crud.product.read_by_barcode(db=db, barcode="0000001");
    if not product_found:
        raise HTTPException(status_code=400, detail="Product does not exist!")
    return product_found


@router.get("/product_sold", response_model = List[schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db)) -> Any:
    product_found = database.crud.product.read_by_sold(db=db);
    if not product_found:
        raise HTTPException(status_code=400, detail="No products exist!")
    return product_found


@router.get("/product", response_model = List[schema.Product])
def read_product(*, db: Session = Depends(Deps.get_db)):
    products_found = database.crud.product.read_all(db=db, skip=0, limit=1000);
    return products_found


@router.put("/product/{key}")
def update_product(*, db: Session = Depends(Deps.get_db), key: Any, product_in: ProductUpdate) -> Any:
    old_product = database.crud.product.read_by_id(db=db, id=key)
    if not old_product:
        return ResponseFail(
            message = "Product [ {} ] does not exist!".format(key),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newProduct = database.crud.product.update(db=db, db_obj=old_product, obj_in=product_in);
    return ResponseSuccess(
        message = "Product [ {} -> {} ] was updated successfully!".format(old_product.identifier, newProduct.identifier),
        status_code=status.HTTP_200_OK
    )

@router.delete("/product/{key}", response_model = schema.Product)
def delete_product(*, db: Session = Depends(Deps.get_db), key: Any):
    products_found = database.crud.product.read_by_key(db=db, key=key);
    if not products_found:
        return ResponseFail(
            message = "Product [ {} ] does not exist!".format(key),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.product.delete(db=db, id=products_found.id)
    return ResponseSuccess(
        message = "Product [ {} ] was deleted successfully!".format(products_found.productName),
        status_code=status.HTTP_200_OK
    )