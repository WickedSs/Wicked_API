from typing import Any, List
import requests
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
import database.crud, schema
from api import Deps
from schema.Response import *


router = APIRouter()
reduce_product_url = "http://product_service:3103/api/product/reduce_quantity"



@router.post("/invoiceItem")
def create_invoiceItem(*, request: Request, db: Session = Depends(Deps.get_db), invoiceItem_in: List[schema.InvoiceItem]) -> ResponseSuccess:
    print(request.cookies)
    for item in invoiceItem_in:
        if not item.is_manual:
            response = requests.put(f"{reduce_product_url}/{item.item_barcode}?sold_quantity={item.item_quantity}")
    database.crud.invoiceItem.create(db, invoiceItem_in);
    return ResponseSuccess(
        message = "invoiceItems [ " + (", ".join(inv.item_name for inv in invoiceItem_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/invoiceItem_id/{id}", response_model = schema.InvoiceItem)
def read_invoiceItem(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    invoiceItem_found = database.crud.invoiceItem.read_by_id(db=db, id=id);
    if not invoiceItem_found:
        raise HTTPException(status_code=400, detail="invoiceItem does not exist!")
    return invoiceItem_found


@router.get("/invoiceItem", response_model = List[schema.InvoiceItem])
def read_invoiceItem(*, db: Session = Depends(Deps.get_db)):
    invoiceItems_found = database.crud.invoiceItem.read_all(db=db, skip=0, limit=50);
    return invoiceItems_found


@router.get("/invoiceItem_identifier/{identifier}", response_model = List[schema.InvoiceItem])
def read_invoiceItem(*, db: Session = Depends(Deps.get_db), identifier: str):
    invoiceItems_found = database.crud.invoiceItem.read_by_identifier(db=db, identifier=identifier)
    if not invoiceItems_found:
        raise HTTPException(status_code=400, detail="invoiceItem does not exist!")
    return invoiceItems_found


@router.put("/invoiceItem_id/{id}")
def update_invoiceItem(*, db: Session = Depends(Deps.get_db), id: int, invoiceItem_in: schema.InvoiceItemUpdate) -> Any:
    old_invoiceItem = database.crud.invoiceItem.read_by_id(db=db, id=id)
    if not old_invoiceItem:
        return ResponseFail(
            message = "invoiceItem [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newinvoiceItem = database.crud.invoiceItem.update(db=db, db_obj=old_invoiceItem, obj_in=invoiceItem_in)
    return ResponseSuccess(
        message = "invoiceItem [ {} ] was updated successfully!".format(old_invoiceItem.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/invoiceItem_id/{id}")
def delete_invoiceItem(*, db: Session = Depends(Deps.get_db), id: int):
    invoiceItems_found = database.crud.invoiceItem.read_by_id(db=db, id=id);
    if not invoiceItems_found:
        return ResponseFail(
            message = "invoiceItem [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.invoiceItem.delete(db=db, id=invoiceItems_found.id)
    return ResponseSuccess(
        message = "invoiceItem [ {} ] was deleted successfully!".format(invoiceItems_found.id),
        status_code=status.HTTP_200_OK
    )
    
    
@router.delete("/invoiceItem_identifier/{identifier}")
def delete_invoiceItem(*, db: Session = Depends(Deps.get_db), identifier: str):
    invoiceItems_found = database.crud.invoiceItem.read_by_identifier(db=db, identifier=identifier);
    if not invoiceItems_found:
        return ResponseFail(
            message = "invoiceItems do not exist!",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.invoiceItem.delete_by_link(db=db, id=invoiceItems_found.id)
    return ResponseSuccess(
        message = "invoiceItems were deleted successfully!",
        status_code=status.HTTP_200_OK
    )