from typing import Any, List
from datetime import timedelta
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import database.crud, schema
from api import Deps
from schema.Response import *
from Settings import settings

router = APIRouter()


@router.post("/user", response_model = schema.User)
def create_product(*, db: Session = Depends(Deps.get_db), user_in: List[schema.UserCreate]):
    """ Create new Product """
    return "Working... [New User Created]"


@router.get("/user/{username}", response_model = schema.User)
def read_product(*, db: Session = Depends(Deps.get_db), username: str):
    product_found = database.crud.user.read_by_username(db=db, username=username)
    return product_found


@router.get("/user", response_model = List[schema.User])
def read_products(*, db: Session = Depends(Deps.get_db)):
    products_found = database.crud.user.read_all(db=db, skip=0, limit=100)
    return products_found


@router.put("/user/{username}", response_model = List[schema.User])
def update_products(*, db: Session = Depends(Deps.get_db), username: str, user_in: schema.UserUpdate):
    old_user = database.crud.user.read_by_username(db=db, username=username)
    if not old_user:
        return ResponseFail(message = "invoice [ {} ] does not exist!".format(id), status_code = status.HTTP_404_NOT_FOUND)
    updated_user = database.crud.user.update(db=db, db_obj=old_user, obj_in=user_in)
    return ResponseSuccess(message = f"User [{updated_user.user_name}] Refresh Token was updated successfully!", status_code=status.HTTP_200_OK)


@router.delete("/user/{username}", response_model = List[schema.User])
def read_products(*, db: Session = Depends(Deps.get_db), username: str):
    products_found = database.crud.user.delete()
    return products_found



# docker exec -it ec65fd8e5a7a439cff7e368c544c2368cde2d08ef3d5def303ef75db143c7135 sh -c "PGPASSWORD=postgresPW psql --username postgres postgres" < E:\Projects\TouatGYM-Gradle\data.sql
# docker cp E:\\Projects\\TouatGYM-Gradle\\data.sql ec65fd8e5a7a439cff7e368c544c2368cde2d08ef3d5def303ef75db143c7135:/pgadmin4
# pg_restore -U username -d dbname -1 data.sql
# psql -U postgres -d postgres -1 -f data-psql.sql