from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import database.crud, schema, models
from api import Deps
from schema import *



router = APIRouter()

@router.post("/material")
def create_material(*, db: Session = Depends(Deps.get_db), material_in: MaterialCreate) -> ResponseSuccess:
    """ Create new material """
    result = database.crud.material.create(db, material_in)
    return ResponseSuccess(
        message = "materials [ " + (", ".join(mat.materialName for mat in material_in)) + " ] were added succesfully!",
        status_code = status.HTTP_200_OK,
    )


@router.get("/material_id/{id}", response_model = schema.Material)
def read_material(*, db: Session = Depends(Deps.get_db), id: Any) -> Any:
    material_found = database.crud.material.read_by_id(db=db, id=id)
    if not material_found:
        raise HTTPException(status_code=400, detail="material does not exist!")
    return material_found

@router.get("/material", response_model = List[schema.Material])
def read_material(*, db: Session = Depends(Deps.get_db)):
    materials_found = database.crud.material.read_all(db=db, skip=0, limit=1000)
    return materials_found


@router.get("/material_link/{link}", response_model = List[schema.Material])
def read_product(*, db: Session = Depends(Deps.get_db), link: str) -> Any:
    materials_found = database.crud.material.read_by_link(db=db, materialLink=link);
    if not materials_found:
        raise HTTPException(status_code=400, detail="No materials exist with link {}!".format(link))
    return materials_found


@router.put("/material/{id}")
def update_material(*, db: Session = Depends(Deps.get_db), id: int, material_in: MaterialUpdate) -> Any:
    old_material = database.crud.material.read_by_id(db=db, id=id)
    if not old_material:
        return ResponseFail(
            message = "material [ {} ] does not exist!".format(id),
            status_code = status.HTTP_400_BAD_REQUEST
        )
    
    newmaterial = database.crud.material.update(db=db, db_obj=old_material, obj_in=material_in);
    return ResponseSuccess(
        message = "material [ {} ] was updated successfully!".format(old_material.id),
        status_code=status.HTTP_200_OK
    )

@router.delete("/material/{id}", response_model = schema.Material)
def delete_material(*, db: Session = Depends(Deps.get_db), id: int):
    materials_found = database.crud.material.read_by_id(db=db, id=id);
    if not materials_found:
        return ResponseFail(
            message = "material [ {} ] does not exist!".format(id),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    database.crud.material.delete(db=db, id=materials_found.id)
    return ResponseSuccess(
        message = "material [ {} ] was deleted successfully!".format(materials_found.id),
        status_code=status.HTTP_200_OK
    )