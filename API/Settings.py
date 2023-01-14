from typing import Any, Dict, List, Optional
from pydantic import AnyHttpUrl, BaseSettings, Field, PostgresDsn, validator





class Settings(BaseSettings):
    API_V1_STR = "/api"
    PROJECT_NAME: str = "Wicked API -- Developed by Souleymane Guerida"
    ALGORITHM = "HS256"
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1 # 60 * 4
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 10 # 60 * 24
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    SECRET_ACCESS_KEY: str
    SECRET_REFRESH_KEY: str

    # MYSQL_SERVER: str = Field(..., env="MYSQL_HOST")
    # MYSQL_USER: str = Field(..., env="MYSQL_USERNAME")
    # MYSQL_PASSWORD: str = Field(..., env="MYSQL_PASSWORD")
    # MYSQL_DB: str = Field(..., env="MYSQL_DATABASE")

    POSTGRES_SERVER: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_USER: str = Field(..., env="POSTGRES_USERNAME")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field(..., env="POSTGRES_DATABASE")
    POSTGRES_PORT: str = Field(..., env="POSTGRES_PORT")

    SQLALCHEMY_MYSQL_DATABASE_URI: Optional[str] = None
    SQLALCHEMY_POSTGRES_DATABASE_URI: Optional[str] = None
    
    
    # @validator("SQLALCHEMY_MYSQL_DATABASE_URI", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
    #     if isinstance(v, str):
    #         return v
    #     return "mysql+pymysql://" + values.get("MYSQL_USER") + ":" + values.get("MYSQL_PASSWORD") + "@" + values.get("MYSQL_SERVER") + "/" + values.get('MYSQL_DB')


    @validator("SQLALCHEMY_POSTGRES_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
            port=values.get('POSTGRES_PORT'),
        )

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8' 
    

settings = Settings()