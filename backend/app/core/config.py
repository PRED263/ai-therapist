from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AI Therapist"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback-secret-key")
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # LLM Configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-pro")
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Crisis Detection
    CRISIS_THRESHOLD: float = float(os.getenv("CRISIS_THRESHOLD", "0.8"))
    
    class Config:
        case_sensitive = True

settings = Settings()