from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.Material_Schema import MaterialUpdate, MaterialCreate
from Routes.Response_models import *



router = APIRouter()

@router.post("/material")
def create_material(*, db: Session = Depends(Deps.get_db), material_in: MaterialCreate) -> ResponseSuccess:
    """ Create new material """
    result = Database.Crud.material.create(db, material_in);
    return ResponseSuccess(
        message = "materials [ " + (", ".join(mat.materialName for mat in material_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/material_id/{id}", response_model = Schema.Material)
def read_material(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    material_found = Database.Crud.material.read_by_id(db=db, id=id);
    if not material_found:
        raise HTTPException(status_code=400, detail="material does not exist!")
    return material_found

@router.get("/material", response_model = List[Schema.Material])
def read_material(*, db: Session = Depends(Deps.get_db)):
    materials_found = Database.Crud.material.read_all(db=db, skip=0, limit=1000)
    return materials_found


@router.put("/material/{id}")
def update_material(*, db: Session = Depends(Deps.get_db), id: int, material_in: MaterialUpdate) -> Any:
    old_material = Database.Crud.material.read_by_id(db=db, id=id)
    if not old_material:
        return ResponseFail(
            message = "material [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newmaterial = Database.Crud.material.update(db=db, db_obj=old_material, obj_in=material_in);
    return ResponseSuccess(
        message = "material [ {} ] was updated successfully!".format(old_material.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/material/{id}", response_model = Schema.Material)
def delete_material(*, db: Session = Depends(Deps.get_db), id: int):
    materials_found = Database.Crud.material.read_by_id(db=db, id=id);
    if not materials_found:
        return ResponseFail(
            message = "material [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    Database.Crud.material.delete(db=db, id=materials_found.id)
    return ResponseSuccess(
        message = "material [ {} ] was deleted successfully!".format(materials_found.id),
        status_code=status.HTTP_200_OK
    )