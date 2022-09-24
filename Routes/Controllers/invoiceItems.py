from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.InvoiceItem_Schema import InvoiceItemUpdate, InvoiceItemCreate
from Routes.Response_models import *



router = APIRouter()

@router.post("/invoiceItem")
def create_invoiceItem(*, db: Session = Depends(Deps.get_db), invoiceItem_in: List[Schema.InvoiceItem]) -> ResponseSuccess:
    """ Create new invoiceItem """
    result = Database.Crud.invoiceItem.create(db, invoiceItem_in);
    return ResponseSuccess(
        message = "invoiceItems [ " + (", ".join(inv.productName for inv in invoiceItem_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/invoiceItem_id/{id}", response_model = Schema.InvoiceItem)
def read_invoiceItem(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    invoiceItem_found = Database.Crud.invoiceItem.read_by_id(db=db, id=id);
    if not invoiceItem_found:
        raise HTTPException(status_code=400, detail="invoiceItem does not exist!")
    return invoiceItem_found


@router.get("/invoiceItem", response_model = List[Schema.InvoiceItem])
def read_invoiceItem(*, db: Session = Depends(Deps.get_db)):
    invoiceItems_found = Database.Crud.invoiceItem.read_all(db=db, skip=0, limit=50);
    return invoiceItems_found


@router.get("/invoiceItem/{identifier}", response_model = List[Schema.InvoiceItem])
def read_invoiceItem(*, db: Session = Depends(Deps.get_db), identifier: str):
    invoiceItems_found = Database.Crud.invoiceItem.read_by_identifier(db=db, identifier=identifier);
    return invoiceItems_found


@router.put("/invoiceItem/{id}")
def update_invoiceItem(*, db: Session = Depends(Deps.get_db), id: int, invoiceItem_in: InvoiceItemUpdate) -> Any:
    old_invoiceItem = Database.Crud.invoiceItem.read_by_id(db=db, id=id)
    if not old_invoiceItem:
        return ResponseFail(
            message = "invoiceItem [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newinvoiceItem = Database.Crud.invoiceItem.update(db=db, db_obj=old_invoiceItem, obj_in=invoiceItem_in);
    return ResponseSuccess(
        message = "invoiceItem [ {} ] was updated successfully!".format(old_invoiceItem.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/invoiceItem/{id}", response_model = Schema.InvoiceItem)
def delete_invoiceItem(*, db: Session = Depends(Deps.get_db), id: int):
    invoiceItems_found = Database.Crud.invoiceItem.delete_by_id(db=db, id=id);
    if not invoiceItems_found:
        return ResponseFail(
            message = "invoiceItem [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.invoiceItem.delete(db=db, id=invoiceItems_found.id)
    return ResponseSuccess(
        message = "invoiceItem [ {} ] was deleted successfully!".format(invoiceItems_found.id),
        status_code=status.HTTP_200_OK
    )
    
    
@router.delete("/invoiceItem/{link}", response_model = Schema.InvoiceItem)
def delete_invoiceItem(*, db: Session = Depends(Deps.get_db), link: str):
    invoiceItems_found = Database.Crud.invoiceItem.delete_by_link(db=db, link=link);
    if not invoiceItems_found:
        return ResponseFail(
            message = "invoiceItems do not exist!",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.invoiceItem.delete(db=db, id=invoiceItems_found.id)
    return ResponseSuccess(
        message = "invoiceItems were deleted successfully!",
        status_code=status.HTTP_200_OK
    )