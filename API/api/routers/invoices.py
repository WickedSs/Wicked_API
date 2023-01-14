from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status, Form, File, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from reporter.JasperReport import JasperReport
import database.crud, schema
from api import Deps
from schema import *
from api import Deps
import os, requests
from Settings import settings


router = APIRouter()

@router.post("/invoice")
def create_invoice(*, db: Session = Depends(Deps.get_db), invoice_in: schema.Invoice) -> ResponseSuccess:
    """ Create new invoice """
    result = database.crud.invoice.create(db, invoice_in);
    return ResponseSuccess(message = f"Invoices [{invoice_in.buyer_name}] added succesfully!", status_code = status.HTTP_200_OK)


@router.get("/invoice_request/")
def create_file(*, db: Session = Depends(Deps.get_db), id: Any = 1, filename: str = "NoName-M01") -> FileResponse:
    invoiceItem_url = "http://invoiceItem_service:3102/api/invoiceItem_identifier"

    invoice_found = database.crud.invoice.read_by_id(db=db, id=id);
    template_path = os.path.join("Reporter", "templates", f"{filename}.jrxml")
    if not os.path.exists(template_path) or not invoice_found:
        raise HTTPException(status_code=400, detail="Template or Invoice does not exist!")

    fields_response = requests.get(f"{invoiceItem_url}/{invoice_found.invoice_identifier}").json()
    template_file = f"{filename}".replace(" ", "_")
    output_file = f"{invoice_found.invoice_identifier}_{invoice_found.buyer_name}".replace(" ", "_")
    output_file_path = os.path.join("Reporter", "examples", f"{output_file}.pdf")
    
    REPORT_PARAMATERS = {
        "Buyer" : invoice_found.buyer_name,
        "OperationDate" : invoice_found.operation_date,
        "BC" : invoice_found.purchase_order,
        "DateBC" : invoice_found.purchase_order_date,
        "BL" : invoice_found.purchase_form,
        "DateBL" : invoice_found.purchase_form_date,
        "FactureNumber" : invoice_found.invoice_number,
        "PriceInWords" : "",
        "TVA" : invoice_found.invoice_tax,
        "Address" : invoice_found.buyer_address,
        "FactureTVA" : str(invoice_found.invoice_tax_price),
        "ValidationDate" : str(invoice_found.validation_deadline),
        "FactureTotal" : str(invoice_found.invoice_total),
        "ImageOne" : "",
        "ImageTwo" : "",
        "Versement" : "",
        "Timbre" : "",
        "ClientTelephone" : "",
        "sellingType" : "",
        "clientMF" : "",
        "clientAI" : "",
        "clientRC" : "",
        "clientNIS" : "",
        "clientCA" : "",
        "CompteBNA" : "",
        "NoNamePayable" : "",
        "FactureTransport" : "0.00",
        "Year" : "",
        "Number" : "",
        "Note" : "",
        "Paid" : "",
    }

    jasperReport = JasperReport(parameters=REPORT_PARAMATERS, fields=fields_response)
    jasperReport.run(template_file, output_file)
    return FileResponse(output_file_path, media_type="application/pdf", filename=f"{output_file}.pdf")



@router.get("/invoice_id/{id}", response_model = schema.Invoice)
def read_invoice(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    invoice_found = database.crud.invoice.read_by_id(db=db, id=id);
    if not invoice_found:
        raise HTTPException(status_code=400, detail="invoice does not exist!")
    return invoice_found


@router.get("/invoice_registry/{registry}", response_model = List[schema.Invoice])
def read_invoices(*, db: Session = Depends(Deps.get_db), registry: str) -> Any:
    invoice_found = database.crud.invoice.read_by_register(db=db, registry=registry.replace("_", " "));
    if not invoice_found:
        raise HTTPException(status_code=400, detail="No invoice exist with register {}!".format(registry))
    return invoice_found


@router.get("/invoice_exact_date/{date}", response_model = List[schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db), date: str) -> Any:
    invoice_found = database.crud.invoice.read_by_exact_date(db=db, date=date);
    if not invoice_found:
        raise HTTPException(status_code=400, detail="No invoice exist with operation date {}!".format(date))
    return invoice_found


@router.get("/invoice_date/{date}", response_model = List[schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db), date: str) -> Any:
    invoice_found = database.crud.invoice.read_by_date(db=db, date=date);
    if not invoice_found:
        raise HTTPException(status_code=400, detail="No invoice exist with operation date {}!".format(date))
    return invoice_found


@router.get("/invoice", response_model = List[schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db)):
    invoices_found = database.crud.invoice.read_all(db=db, skip=0, limit=50);
    return invoices_found


@router.get("/invoice_search/", response_model = List[schema.Invoice])
def read_invoice(*, db: Session = Depends(Deps.get_db), buyer: str, register: str):
    invoices_found = database.crud.invoice.read_by_buyer_and_register(db=db, buyer=buyer, register=register.replace("_", " "));
    return invoices_found


@router.put("/invoice/{id}")
def update_invoice(*, db: Session = Depends(Deps.get_db), id: int, invoice_in: InvoiceUpdate) -> Any:
    old_invoice = database.crud.invoice.read_by_id(db=db, id=id)
    if not old_invoice:
        return ResponseFail(
            message = "invoice [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newinvoice = database.crud.invoice.update(db=db, db_obj=old_invoice, obj_in=invoice_in);
    return ResponseSuccess(
        message = "invoice [ {} ] was updated successfully!".format(old_invoice.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/invoice/{id}")
def delete_invoice(*, db: Session = Depends(Deps.get_db), id: int):
    invoices_found = database.crud.invoice.read_by_id(db=db, id=id);
    if not invoices_found:
        return ResponseFail(
            message = "invoice [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    items = database.crud.invoiceItem.read_by_identifier(db=db, identifier=invoices_found.identifier)
    for item in items:
        old_product = database.crud.product.read_by_barcode(db=db, barcode=item.respectiveBarcode)
        old_product.quantity += item.quantity
        db.commit()
    database.crud.invoice.delete(db=db, id=invoices_found.id)
    return ResponseSuccess(
        message = "invoice [ {} ] was deleted successfully!".format(invoices_found.id),
        status_code=status.HTTP_200_OK
    )
    
@router.delete("/invoice_identifier/{identifier}")
def delete_invoice(*, db: Session = Depends(Deps.get_db), identifier: str):
    invoices_found = database.crud.invoice.read_by_identifier(db=db, identifier=identifier);
    print(invoices_found)
    if not invoices_found:
        return ResponseFail(
            message = "invoice [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    items = database.crud.invoiceItem.read_by_identifier(db=db, identifier=identifier)
    for item in items:
        old_product = database.crud.product.read_by_barcode(db=db, barcode=item.respectiveBarcode)
        old_product.quantity += item.quantity
        db.commit()
    database.crud.invoice.delete(db=db, id=invoices_found.id)
    return ResponseSuccess(
        message = "invoice [ {} ] was deleted successfully!".format(invoices_found.id),
        status_code=status.HTTP_200_OK
    )