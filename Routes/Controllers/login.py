from datetime import timedelta
from typing import Any
from pydantic import BaseModel


from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import Database.Crud, Models, Schema
from Settings import settings
from Routes import Deps, Security

router = APIRouter()

class ResponseSuccess(BaseModel):
    message: str
    status_code: Any
    access_token: str
    token_type: str
    
class ResponseFail(BaseModel):
    message: str
    status_code: Any


@router.post("/login/access-token")
def login_access_token(db: Session = Depends(Deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """ OAuth2 compatible token login, get an access token for future requests """
    print("Form:", form_data.username)
    user_found = Database.Crud.user.authenticate(db, username=form_data.username, password=form_data.password)
    if not user_found:
        return ResponseFail(
            message = "Incorrect username or password",
            status_code = status.HTTP_400_BAD_REQUEST,
        )
    # elif not Database.Crud.user.is_active(user_found):
    #     raise HTTPException(status_code=400, detail="Inactive user")
    else:
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return ResponseSuccess(
            message = "Success!",
            status_code = status.HTTP_200_OK,
            access_token = Security.create_access_token(user_found.userRole, user_found.username, expires_delta=access_token_expires),
            token_type = "bearer"
        )