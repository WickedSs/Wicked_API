from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Case_Schema import CaseUpdate, CaseCreate
from Routes.Response_models import *



router = APIRouter()

@router.post("/case")
def create_case(*, db: Session = Depends(Deps.get_db), case_in: Schema.Case) -> ResponseSuccess:
    """ Create new case """
    result = Database.Crud.case.create(db, case_in);
    return ResponseSuccess(
        message = "Cases [ " + (", ".join(inv.buyer for inv in case_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/case_id/{id}", response_model = Schema.Case)
def read_case(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    case_found = Database.Crud.case.read_by_id(db=db, id=id);
    if not case_found:
        raise HTTPException(status_code=400, detail="case does not exist!")
    return case_found


@router.get("/case", response_model = List[Schema.Case])
def read_case(*, db: Session = Depends(Deps.get_db)):
    cases_found = Database.Crud.case.read_all(db=db, skip=0, limit=50);
    return cases_found


@router.put("/case/{id}")
def update_case(*, db: Session = Depends(Deps.get_db), id: int, case_in: CaseUpdate) -> Any:
    old_case = Database.Crud.case.read_by_id(db=db, id=id)
    if not old_case:
        return ResponseFail(
            message = "case [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newcase = Database.Crud.case.update(db=db, db_obj=old_case, obj_in=case_in);
    return ResponseSuccess(
        message = "case [ {} ] was updated successfully!".format(old_case.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/case/{id}", response_model = Schema.Case)
def delete_case(*, db: Session = Depends(Deps.get_db), id: int):
    cases_found = Database.Crud.case.read_by_id(db=db, id=id);
    if not cases_found:
        return ResponseFail(
            message = "case [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.case.delete(db=db, id=cases_found.id)
    return ResponseSuccess(
        message = "case [ {} ] was deleted successfully!".format(cases_found.id),
        status_code=status.HTTP_200_OK
    )