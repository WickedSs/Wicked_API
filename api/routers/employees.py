from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schema, database.crud
from api import Deps
from schema.Employee import EmployeeUpdate, EmployeeCreate
from schema.Response import *



router = APIRouter()

@router.post("/employee")
def create_employee(*, db: Session = Depends(Deps.get_db), employee_in: schema.Employee) -> ResponseSuccess:
    """ Create new employee """
    result = database.crud.employee.create(db, employee_in);
    return ResponseSuccess(
        message = f"Employees [{employee_in.fullname}] wes added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/employee_id/{id}", response_model = schema.Employee)
def read_employee(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    employee_found = database.crud.employee.read_by_id(db=db, id=id);
    if not employee_found:
        raise HTTPException(status_code=400, detail="Employee does not exist!")
    return employee_found


@router.get("/employee", response_model = List[schema.Employee])
def read_employee(*, db: Session = Depends(Deps.get_db)):
    employees_found = database.crud.employee.read_all(db=db, skip=0, limit=10000);
    return employees_found


@router.put("/employee/{id}")
def update_employee(*, db: Session = Depends(Deps.get_db), id: int, employee_in: EmployeeUpdate) -> Any:
    old_employee = database.crud.employee.read_by_id(db=db, id=id)
    if not old_employee:
        return ResponseFail(
            message = f"Employee [{id}] does not exist!",
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newemployee = database.crud.employee.update(db=db, db_obj=old_employee, obj_in=employee_in);
    return ResponseSuccess(
        message = f"Employee [{old_employee.id}] was updated successfully!",
        status_code=status.HTTP_200_OK
    )

@router.delete("/employee/{id}", response_model = schema.Employee)
def delete_employee(*, db: Session = Depends(Deps.get_db), id: int):
    employees_found = database.crud.employee.read_by_id(db=db, id=id);
    if not employees_found:
        return ResponseFail(
            message = f"Employee [{id}] does not exist!",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.employee.delete(db=db, id=employees_found.id)
    return ResponseSuccess(
        message = f"Employee [{employees_found.id}] was deleted successfully!",
        status_code=status.HTTP_200_OK
    )