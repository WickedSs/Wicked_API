from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database.crud, schema
from api import Deps
from schema.Bank import BankUpdate, BankCreate
from schema.Response import *



router = APIRouter()

@router.post("/bank")
def create_bank(*, db: Session = Depends(Deps.get_db), case_in: schema.Bank) -> ResponseSuccess:
    """ Create new bank """
    result = database.crud.bank.create(db, case_in);
    return ResponseSuccess(
        message = f"Bank [{case_in.bank_name}] wes added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/bank_id/{id}", response_model = schema.Bank)
def read_bank(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    case_found = database.crud.bank.read_by_id(db=db, id=id);
    if not case_found:
        raise HTTPException(status_code=400, detail="Bank does not exist!")
    return case_found


@router.get("/bank", response_model = List[schema.Bank])
def read_bank(*, db: Session = Depends(Deps.get_db)):
    cases_found = database.crud.bank.read_all(db=db, skip=0, limit=50);
    return cases_found



@router.put("/bank/{id}")
def update_bank(*, db: Session = Depends(Deps.get_db), id: int, bank_in: BankUpdate) -> Any:
    old_bank = database.crud.bank.read_by_id(db=db, id=id)
    if not old_bank:
        return ResponseFail(
            message = f"Bank [{id}] does not exist!",
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newbank = database.crud.bank.update(db=db, db_obj=old_bank, obj_in=bank_in);
    return ResponseSuccess(
        message = f"Bank [{newbank.bank_name}] was updated successfully!",
        status_code=status.HTTP_200_OK
    )


@router.delete("/bank/{id}", response_model = schema.Bank)
def delete_bank(*, db: Session = Depends(Deps.get_db), id: int):
    bank_found = database.crud.bank.read_by_id(db=db, id=id);
    if not bank_found:
        return ResponseFail(
            message = "bank [{id}] does not exist!",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.bank.delete(db=db, id=bank_found.id)
    return ResponseSuccess(
        message = f"Bank [{bank_found.id}] was deleted successfully!",
        status_code=status.HTTP_200_OK
    )