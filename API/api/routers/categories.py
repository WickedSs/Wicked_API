from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database.crud, schema, models
from api import Deps
from schema.Category import CategoryUpdate, CategoryCreate
from schema.Response import *



router = APIRouter()

@router.post("/category")
def create_category(*, db: Session = Depends(Deps.get_db), category_in: schema.Category) -> ResponseSuccess:
    """ Create new category """
    result = database.crud.category.create(db, category_in);
    return ResponseSuccess(
        message = f"Category [{category_in.category_name}] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/category_id/{id}", response_model = schema.Category)
def read_category(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    category_found = database.crud.category.read_by_id(db=db, id=id);
    if not category_found:
        raise HTTPException(status_code=400, detail="Category does not exist!")
    return category_found


@router.get("/category", response_model = List[schema.Category])
def read_category(*, db: Session = Depends(Deps.get_db)):
    categorys_found = database.crud.category.read_all(db=db, skip=0, limit=50);
    return categorys_found


@router.put("/category/{id}")
def update_category(*, db: Session = Depends(Deps.get_db), id: int, category_in: CategoryUpdate) -> Any:
    old_category = database.crud.category.read_by_id(db=db, id=id)
    if not old_category:
        return ResponseFail(
            message = f"Category [{id}] does not exist!",
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newcategory = database.crud.category.update(db=db, db_obj=old_category, obj_in=category_in);
    return ResponseSuccess(
        message = f"Category [{old_category.id}] was updated successfully!",
        status_code=status.HTTP_200_OK
    )

@router.delete("/category/{id}", response_model = schema.Category)
def delete_category(*, db: Session = Depends(Deps.get_db), id: int):
    categorys_found = database.crud.category.read_by_id(db=db, id=id);
    if not categorys_found:
        return ResponseFail(
            message = f"Category [{id}] does not exist!",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.category.delete(db=db, id=categorys_found.id)
    return ResponseSuccess(
        message = f"Category [{categorys_found.id}] was deleted successfully!",
        status_code=status.HTTP_200_OK
    )