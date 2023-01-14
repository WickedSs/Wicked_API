from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext
from Settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(role: Union[str, Any], username: Union[str, Any], expires_delta: timedelta = settings.ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    generated_at = datetime.utcnow()
    expire = datetime.utcnow() + expires_delta
    to_encode = { "iat" : generated_at, "exp": expire, "username": str(username), "role": str(role) }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)