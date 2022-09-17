from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.User_Schema import User

router = APIRouter()


@router.post("/user", response_model = Schema.User)
def create_product(*, db: Session = Depends(Deps.get_db), user_in: List[Schema.UserCreate]) -> Any:
    """ Create new Product """
    return "Working... [New Product Create]"


@router.get("/user/{id}", response_model = Schema.User)
def read_product(*, db: Session = Depends(Deps.get_db), id: int) -> Any:
    product_found = Database.Crud.user.read_single(db=db, id=id);
    return product_found


@router.get("/all_users", response_model = List[Schema.User])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.user.read_all(db=db, skip=0, limit=50);
    return products_found


@router.put("/user/{id}", response_model = List[Schema.User])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.user.update();
    return products_found


@router.delete("/user/{id}", response_model = List[Schema.User])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.user.delete();
    return products_found