from fastapi import APIRouter
from Routes.Controllers import products
from Routes.Controllers import users


api_router = APIRouter()
api_router.include_router(products.router, tags=["products"])
api_router.include_router(users.router, tags=["users"])