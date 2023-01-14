from pydantic import BaseModel
from typing import Any



class ResponseSuccess(BaseModel):
    message: str
    status_code: int

class LoginSuccess(BaseModel):
    message: str
    status_code: Any
    access_token: str
    token_type: str
    
class ResponseFail(BaseModel):
    message: str
    status_code: Any