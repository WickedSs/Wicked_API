from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Expense_Schema import ExpenseUpdate, ExpenseCreate
from Routes.Response_models import *



router = APIRouter()

@router.post("/expense")
def create_expense(*, db: Session = Depends(Deps.get_db), expense_in: Schema.Expense) -> ResponseSuccess:
    """ Create new expense """
    result = Database.Crud.expense.create(db, expense_in);
    return ResponseSuccess(
        message = "Expenses [ " + (", ".join(inv.buyer for inv in expense_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/expense_id/{id}", response_model = Schema.Expense)
def read_expense(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    expense_found = Database.Crud.expense.read_by_id(db=db, id=id);
    if not expense_found:
        raise HTTPException(status_code=400, detail="expense does not exist!")
    return expense_found


@router.get("/expense", response_model = List[Schema.Expense])
def read_expense(*, db: Session = Depends(Deps.get_db)):
    expenses_found = Database.Crud.expense.read_all(db=db, skip=0, limit=50);
    return expenses_found


@router.put("/expense/{id}")
def update_expense(*, db: Session = Depends(Deps.get_db), id: int, expense_in: ExpenseUpdate) -> Any:
    old_expense = Database.Crud.expense.read_by_id(db=db, id=id)
    print("ObjectIn: ", expense_in.expenseName, "OldObject: ", old_expense.expenseName)
    if not old_expense:
        return ResponseFail(
            message = "expense [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newexpense = Database.Crud.expense.update(db=db, db_obj=old_expense, obj_in=expense_in);
    return ResponseSuccess(
        message = "expense [ {} ] was updated successfully!".format(old_expense.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/expense/{id}", response_model = Schema.Expense)
def delete_expense(*, db: Session = Depends(Deps.get_db), id: int):
    expenses_found = Database.Crud.expense.read_by_id(db=db, id=id);
    if not expenses_found:
        return ResponseFail(
            message = "expense [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.expense.delete(db=db, id=expenses_found.id)
    return ResponseSuccess(
        message = "expense [ {} ] was deleted successfully!".format(expenses_found.id),
        status_code=status.HTTP_200_OK
    )