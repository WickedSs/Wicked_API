from fastapi import APIRouter
from Routes.Controllers import products
from Routes.Controllers import users
from Routes.Controllers import login


api_router = APIRouter()
api_router.include_router(products.router, tags=["Products"])
api_router.include_router(users.router, tags=["Users"])
api_router.include_router(login.router, tags=["Login"])