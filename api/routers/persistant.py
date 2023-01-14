from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database.crud, schema
from api import Deps
from schema import *



router = APIRouter()

@router.post("/persistant")
def create_persistant(*, db: Session = Depends(Deps.get_db), persistant_in: schema.Persistant) -> ResponseSuccess:
    """ Create new persistant """
    # result = Database.database.crud.persistant.create(db, persistant_in);
    return ResponseSuccess(
        message = "Sorry! such operation is not possibl-e at the moment!!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/persistant_id/{id}", response_model = schema.Persistant)
def read_persistant(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    persistant_found = database.crud.persistant.read_by_id(db=db, id=id);
    if not persistant_found:
        raise HTTPException(status_code=400, detail="persistant does not exist!")
    return persistant_found


@router.put("/persistant/{id}")
def update_persistant(*, db: Session = Depends(Deps.get_db), id: int, persistant_in: PersistantUpdate) -> Any:
    old_persistant = database.crud.persistant.read_by_id(db=db, id=id)
    if not old_persistant:
        return ResponseFail(
            message = "persistant [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newpersistant = database.crud.persistant.update(db=db, db_obj=old_persistant, obj_in=persistant_in);
    return ResponseSuccess(
        message = "persistant [ {} ] was updated successfully!".format(old_persistant.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/persistant/{id}", response_model = schema.Persistant)
def delete_persistant(*, db: Session = Depends(Deps.get_db), id: int):
    persistants_found = database.crud.persistant.read_by_id(db=db, id=id);
    if not persistants_found:
        return ResponseFail(
            message = "persistant [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.persistant.delete(db=db, id=persistants_found.id)
    return ResponseSuccess(
        message = "persistant [ {} ] was deleted successfully!".format(persistants_found.id),
        status_code=status.HTTP_200_OK
    )