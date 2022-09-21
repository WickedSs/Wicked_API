from fastapi import APIRouter
from Database.Crud import employee_crud
from Routes.Controllers import (products, users, login, invoices, invoiceItems, materials, persistant, employees, cases, categories, expenses)


api_router = APIRouter()
api_router.include_router(materials.router, tags=["Materials"])
api_router.include_router(cases.router, tags=["Cases"])
api_router.include_router(categories.router, tags=["Categories"])
api_router.include_router(invoices.router, tags=["Invoices"])
api_router.include_router(invoiceItems.router, tags=["InvoiceItems"])
api_router.include_router(products.router, tags=["Products"])
api_router.include_router(persistant.router, tags=["Persistant"])
api_router.include_router(employees.router, tags=["Employees"])
api_router.include_router(expenses.router, tags=["Expenses"])
api_router.include_router(users.router, tags=["Users"])
api_router.include_router(login.router, tags=["Login"])