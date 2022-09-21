from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Category_Schema import CategoryUpdate, CategoryCreate
from Routes.Response_models import *



router = APIRouter()

@router.post("/category")
def create_category(*, db: Session = Depends(Deps.get_db), category_in: Schema.Category) -> ResponseSuccess:
    """ Create new category """
    result = Database.Crud.category.create(db, category_in);
    return ResponseSuccess(
        message = "Categorys [ " + (", ".join(inv.buyer for inv in category_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/category_id/{id}", response_model = Schema.Category)
def read_category(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    category_found = Database.Crud.category.read_by_id(db=db, id=id);
    if not category_found:
        raise HTTPException(status_code=400, detail="category does not exist!")
    return category_found


@router.get("/category", response_model = List[Schema.Category])
def read_category(*, db: Session = Depends(Deps.get_db)):
    categorys_found = Database.Crud.category.read_all(db=db, skip=0, limit=50);
    return categorys_found


@router.put("/category/{id}")
def update_category(*, db: Session = Depends(Deps.get_db), id: int, category_in: CategoryUpdate) -> Any:
    old_category = Database.Crud.category.read_by_id(db=db, id=id)
    if not old_category:
        return ResponseFail(
            message = "category [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newcategory = Database.Crud.category.update(db=db, db_obj=old_category, obj_in=category_in);
    return ResponseSuccess(
        message = "category [ {} ] was updated successfully!".format(old_category.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/category/{id}", response_model = Schema.Category)
def delete_category(*, db: Session = Depends(Deps.get_db), id: int):
    categorys_found = Database.Crud.category.read_by_id(db=db, id=id);
    if not categorys_found:
        return ResponseFail(
            message = "category [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.category.delete(db=db, id=categorys_found.id)
    return ResponseSuccess(
        message = "category [ {} ] was deleted successfully!".format(categorys_found.id),
        status_code=status.HTTP_200_OK
    )