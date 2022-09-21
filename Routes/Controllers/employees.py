from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Employee_Schema import EmployeeUpdate, EmployeeCreate
from Routes.Response_models import *



router = APIRouter()

@router.post("/employee")
def create_employee(*, db: Session = Depends(Deps.get_db), employee_in: Schema.Employee) -> ResponseSuccess:
    """ Create new employee """
    result = Database.Crud.employee.create(db, employee_in);
    return ResponseSuccess(
        message = "Employees [ " + (", ".join(inv.buyer for inv in employee_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/employee_id/{id}", response_model = Schema.Employee)
def read_employee(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    employee_found = Database.Crud.employee.read_by_id(db=db, id=id);
    if not employee_found:
        raise HTTPException(status_code=400, detail="employee does not exist!")
    return employee_found


@router.get("/employee", response_model = List[Schema.Employee])
def read_employee(*, db: Session = Depends(Deps.get_db)):
    employees_found = Database.Crud.employee.read_all(db=db, skip=0, limit=50);
    return employees_found


@router.put("/employee/{id}")
def update_employee(*, db: Session = Depends(Deps.get_db), id: int, employee_in: EmployeeUpdate) -> Any:
    old_employee = Database.Crud.employee.read_by_id(db=db, id=id)
    if not old_employee:
        return ResponseFail(
            message = "employee [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newemployee = Database.Crud.employee.update(db=db, db_obj=old_employee, obj_in=employee_in);
    return ResponseSuccess(
        message = "employee [ {} ] was updated successfully!".format(old_employee.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/employee/{id}", response_model = Schema.Employee)
def delete_employee(*, db: Session = Depends(Deps.get_db), id: int):
    employees_found = Database.Crud.employee.read_by_id(db=db, id=id);
    if not employees_found:
        return ResponseFail(
            message = "employee [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.employee.delete(db=db, id=employees_found.id)
    return ResponseSuccess(
        message = "employee [ {} ] was deleted successfully!".format(employees_found.id),
        status_code=status.HTTP_200_OK
    )