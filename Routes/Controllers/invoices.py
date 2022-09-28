from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Invoice_Schema import InvoiceUpdate, InvoiceCreate
from Routes.Response_models import *



router = APIRouter()

@router.post("/invoice")
def create_invoice(*, db: Session = Depends(Deps.get_db), invoice_in: Schema.Invoice) -> ResponseSuccess:
    """ Create new invoice """
    result = Database.Crud.invoice.create(db, invoice_in);
    return ResponseSuccess(
        message = "Invoices [ {} ] added succesfully!".format(invoice_in.buyer),
        status_code = status.HTTP_200_OK,
    )


@router.get("/invoice_id/{id}", response_model = Schema.Invoice)
def read_invoice(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    invoice_found = Database.Crud.invoice.read_by_id(db=db, id=id);
    if not invoice_found:
        raise HTTPException(status_code=400, detail="invoice does not exist!")
    return invoice_found


@router.get("/invoice_register/{register}", response_model = List[Schema.Invoice])
def read_invoices(*, db: Session = Depends(Deps.get_db), register: str) -> Any:
    invoice_found = Database.Crud.invoice.read_by_register(db=db, register=register.replace("_", " "));
    if not invoice_found:
        raise HTTPException(status_code=400, detail="No invoice exist with register {}!".format(register))
    return invoice_found


@router.get("/invoice_exact_date/{date}", response_model = List[Schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db), date: str) -> Any:
    invoice_found = Database.Crud.invoice.read_by_exact_date(db=db, date=date);
    if not invoice_found:
        raise HTTPException(status_code=400, detail="No invoice exist with operation date {}!".format(date))
    return invoice_found


@router.get("/invoice_date/{date}", response_model = List[Schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db), date: str) -> Any:
    invoice_found = Database.Crud.invoice.read_by_date(db=db, date=date);
    if not invoice_found:
        raise HTTPException(status_code=400, detail="No invoice exist with operation date {}!".format(date))
    return invoice_found


@router.get("/invoice", response_model = List[Schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db)):
    invoices_found = Database.Crud.invoice.read_all(db=db, skip=0, limit=50);
    return invoices_found


@router.get("/invoice_search/", response_model = List[Schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db), buyer: str, register: str):
    invoices_found = Database.Crud.invoice.read_by_buyer_and_register(db=db, buyer=buyer, register=register.replace("_", " "));
    return invoices_found


@router.put("/invoice/{id}")
def update_invoice(*, db: Session = Depends(Deps.get_db), id: int, invoice_in: InvoiceUpdate) -> Any:
    old_invoice = Database.Crud.invoice.read_by_id(db=db, id=id)
    if not old_invoice:
        return ResponseFail(
            message = "invoice [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newinvoice = Database.Crud.invoice.update(db=db, db_obj=old_invoice, obj_in=invoice_in);
    return ResponseSuccess(
        message = "invoice [ {} ] was updated successfully!".format(old_invoice.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/invoice/{id}")
def delete_invoice(*, db: Session = Depends(Deps.get_db), id: int):
    invoices_found = Database.Crud.invoice.read_by_id(db=db, id=id);
    if not invoices_found:
        return ResponseFail(
            message = "invoice [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    items = Database.Crud.invoiceItem.read_by_identifier(db=db, identifier=invoices_found.identifier)
    for item in items:
        old_product = Database.Crud.product.read_by_barcode(db=db, barcode=item.respectiveBarcode)
        old_product.quantity += item.quantity
        db.commit()
    Database.Crud.invoice.delete(db=db, id=invoices_found.id)
    return ResponseSuccess(
        message = "invoice [ {} ] was deleted successfully!".format(invoices_found.id),
        status_code=status.HTTP_200_OK
    )
    
@router.delete("/invoice_identifier/{identifier}")
def delete_invoice(*, db: Session = Depends(Deps.get_db), identifier: str):
    invoices_found = Database.Crud.invoice.read_by_identifier(db=db, identifier=identifier);
    print(invoices_found)
    if not invoices_found:
        return ResponseFail(
            message = "invoice [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    items = Database.Crud.invoiceItem.read_by_identifier(db=db, identifier=identifier)
    for item in items:
        old_product = Database.Crud.product.read_by_barcode(db=db, barcode=item.respectiveBarcode)
        old_product.quantity += item.quantity
        db.commit()
    Database.Crud.invoice.delete(db=db, id=invoices_found.id)
    return ResponseSuccess(
        message = "invoice [ {} ] was deleted successfully!".format(invoices_found.id),
        status_code=status.HTTP_200_OK
    )