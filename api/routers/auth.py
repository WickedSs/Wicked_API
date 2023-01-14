from typing import Any, List
from datetime import timedelta
from fastapi import APIRouter, Body, Depends, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database.crud, schema, models
from api import Deps, Security
from schema.Response import *
from Settings import settings

router = APIRouter()


@router.post("/auth/access-token")
def login_access_token(*, response: Response, db: Session = Depends(Deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user_found = database.crud.user.authenticate(db, username=form_data.username, password=form_data.password)
    if not user_found:
        return ResponseFail(message = "Incorrect username or password", status_code = status.HTTP_404_NOT_FOUND)

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = Security.create_access_token(role=user_found.user_role, username=user_found.user_name, scope="Basic", expires_delta=access_token_expires)
    refresh_token = Security.create_refresh_token(role=user_found.user_role, username=user_found.user_name, scope="Basic", expires_delta=refresh_token_expires)

    old_user = database.crud.user.read_by_username(db=db, username=user_found.user_name)
    user_found.user_refresh_token = refresh_token
    updated_user = { c.name: getattr(user_found, c.name) for c in models.User.__table__.columns }
    database.crud.user.update(db=db, db_obj=old_user, obj_in=updated_user)

    response.set_cookie(key="refresh", value=f"{refresh_token}", httponly=True, max_age=refresh_token_expires, path="/api/user/authorization", expires=refresh_token_expires, samesite="strict")
    return LoginSuccess(message = "Success!", status_code = status.HTTP_200_OK, access_token = access_token, token_type = "bearer")


@router.post("/auth/logout")
def delete_access_token(*, response: Response, db: Session = Depends(Deps.get_db)) -> Any:
    response.delete_cookie("refresh")
    return ResponseSuccess(message="Logged out successfully", status_code=status.HTTP_200_OK)


@router.post("/auth/authorization")
def verify_access_token(*, response : Response, request: Request, db: Session = Depends(Deps.get_db)) -> Any:
    auth_header_token = request.headers.get("Authorization").split(" ")
    if len(auth_header_token) <= 1:
        response.delete_cookie(key="refresh")
        return HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "You're not authenticated to access this page!", )
    

    decoded_access_token = Security.verify_token(access_token=auth_header_token[1], secret_key=settings.SECRET_ACCESS_KEY)
    if decoded_access_token == -1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate ACCESS token.")

    if decoded_access_token == 0:
        auth_header_refresh = request.cookies.get("refresh")
        if not auth_header_refresh or len(auth_header_refresh) <= 0:
            return HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "You're not authenticated to access this page!")

        decoded_refresh_token = Security.verify_token(access_token=auth_header_refresh, secret_key=settings.SECRET_REFRESH_KEY)
        if decoded_refresh_token == -1 or decoded_refresh_token == 0:
            response.delete_cookie("refresh")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate REFRESH token or expired. please LOGIN again")
        else:
            access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = Security.create_access_token(role=decoded_refresh_token.get("role"), username=decoded_refresh_token.get("username"), scope="Basic", expires_delta=access_token_expires)
            return LoginSuccess(message = "A new access token has been generated!", status_code = status.HTTP_201_CREATED, access_token = access_token, token_type = "bearer")

    return ResponseSuccess(message = "Authenticated!", status_code = status.HTTP_200_OK)


@router.get("/auth/refresh-token")
def verify_access_token(*, request: Request, db: Session = Depends(Deps.get_db)) -> Any:
    auth_header_refresh = request.cookies.get("refresh")
    if not auth_header_refresh or len(auth_header_refresh) <= 0:
        return HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "You're not authenticated to access this page!", )
    
    decoded_jwt_token = Security.verify_refresh_token(auth_header_refresh)
    if len(decoded_jwt_token) <= 0 or not decoded_jwt_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate refresh token.")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = Security.create_access_token(decoded_jwt_token.user_role, decoded_jwt_token.username, expires_delta=access_token_expires)
    return LoginSuccess(message = "A new access token has been generated!", status_code = status.HTTP_200_OK, access_token = access_token, token_type = "bearer")
