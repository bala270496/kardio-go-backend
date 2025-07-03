from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings"""
    
    PROJECT_NAME: str = "FastAPI Backend"
    PROJECT_DESCRIPTION: str = "A fast and modern API built with FastAPI for Cloud Run"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # CORS settings
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()