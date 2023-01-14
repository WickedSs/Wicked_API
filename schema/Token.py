from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenPayload(BaseModel):
    username: str
    scope : str = "Basic"
    iat: datetime
    exp: datetime

    class Config:
        orm_mode = True