from typing import Any, List, TypeVar, Generic, Type
from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Database.Crud, Schema, Models
import Models, Schema, random
from Routes import Deps
from Database.Base import Base
from Schema.Product_Schema import Product, ProductUpdate
from Routes.Response_models import *


Model = TypeVar("Model", bound=Base)
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


""" Some syupid idea to try later! """
class ControllerBASE(Generic[Model, CreateSchema, UpdateSchema]):
    def __init__(self, route_prefix: str, model: Type[Model], createModel: Type[CreateSchema], updateModel: Type[UpdateSchema]):
        self.model = model
        self.createModel = createModel
        self.updateModel = updateModel
        self.prefix = route_prefix
        self.router = APIRouter()
        
    