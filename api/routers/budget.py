from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database.crud, schema
import models, schema
from api import Deps
from schema.Expense import ExpenseUpdate, ExpenseCreate
from schema.Response import *



router = APIRouter()

@router.post("/expense")
def create_expense(*, db: Session = Depends(Deps.get_db), expense_in: schema.Expense) -> ResponseSuccess:
    """ Create new expense """
    result = database.crud.expense.create(db, expense_in);
    return ResponseSuccess(
        message = f"Expense [{expense_in.expense_category}] was added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/expense_id/{id}", response_model = schema.Expense)
def read_expense(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    expense_found = database.crud.expense.read_by_id(db=db, id=id);
    if not expense_found:
        raise HTTPException(status_code=400, detail="expense does not exist!")
    return expense_found


@router.get("/expense", response_model = List[schema.Expense])
def read_expense(*, db: Session = Depends(Deps.get_db)):
    expenses_found = database.crud.expense.read_all(db=db, skip=0, limit=50);
    return expenses_found


@router.put("/expense/{id}")
def update_expense(*, db: Session = Depends(Deps.get_db), id: int, expense_in: ExpenseUpdate) -> Any:
    old_expense = database.crud.expense.read_by_id(db=db, id=id)
    if not old_expense:
        return ResponseFail(
            message = "expense [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newexpense = database.crud.expense.update(db=db, db_obj=old_expense, obj_in=expense_in);
    return ResponseSuccess(
        message = "expense [ {} ] was updated successfully!".format(old_expense.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/expense/{id}", response_model = schema.Expense)
def delete_expense(*, db: Session = Depends(Deps.get_db), id: int):
    expenses_found = database.crud.expense.read_by_id(db=db, id=id);
    if not expenses_found:
        return ResponseFail(
            message = "expense [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.expense.delete(db=db, id=expenses_found.id)
    return ResponseSuccess(
        message = "expense [ {} ] was deleted successfully!".format(expenses_found.id),
        status_code=status.HTTP_200_OK
    )