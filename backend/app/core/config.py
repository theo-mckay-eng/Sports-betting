from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/sports_betting"
    REDIS_URL: str = "redis://localhost:6379"
    ODDS_API_KEY: str = ""
    DEBUG: bool = True
    SECRET_KEY: str = "change-me"
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    ODDS_API_TIMEOUT: int = 8
    ODDS_CACHE_TTL: int = 300
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
