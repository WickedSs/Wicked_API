from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Schema.User_Schema import User

router = APIRouter()


@router.post("/user", response_model = Schema.User)
def create_product(*, db: Session = Depends(Deps.get_db), user_in: List[Schema.UserCreate]):
    """ Create new Product """
    return "Working... [New Product Create]"


@router.get("/user/{username}", response_model = Schema.User)
def read_product(*, db: Session = Depends(Deps.get_db), username: str):
    product_found = Database.Crud.user.read_by_username(db=db, username=username);
    return product_found


@router.get("/all_users", response_model = List[Schema.User])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = Database.Crud.user.read_all(db=db, skip=0, limit=50);
    return products_found


@router.put("/user/{username}", response_model = List[Schema.User])
def read_products(*, db: Session = Depends(Deps.get_db), username: str):
    products_found = Database.Crud.user.update();
    return products_found


@router.delete("/user/{username}", response_model = List[Schema.User])
def read_products(*, db: Session = Depends(Deps.get_db), username: str):
    products_found = Database.Crud.user.delete();
    return products_found