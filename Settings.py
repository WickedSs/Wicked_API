from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, Field, HttpUrl, PostgresDsn, validator





class Settings(BaseSettings):
    API_V1_STR = "/api"
    PROJECT_NAME: str = "Wicked API"
    ALGORITHM = "HS256"
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    SECRET_KEY: str

    MYSQL_SERVER: str = Field(..., env="MYSQL_HOST")
    MYSQL_USER: str = Field(..., env="MYSQL_USERNAME")
    MYSQL_PASSWORD: str = Field(..., env="MYSQL_PASSWORD")
    MYSQL_DB: str = Field(..., env="MYSQL_DATABASE")
    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    
    
    
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return "mysql+pymysql://" + values.get("MYSQL_USER") + ":" + values.get("MYSQL_PASSWORD") + "@" + values.get("MYSQL_SERVER") + "/" + values.get('MYSQL_DB')

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8' 
    

settings = Settings()