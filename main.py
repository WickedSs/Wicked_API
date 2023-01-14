from typing import Union
from fastapi import FastAPI
from Routes.api import api_router
from starlette.middleware.cors import CORSMiddleware

# from api.api import api_router
from Settings import settings
app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/aboutMe")
def who_is_wicked():
    return "Self-learning Software engineering through research & development | Python developer"


@app.get("/ping", description="Wicked was here!")
def ping_wicked():
    return "Hello, Friend!"