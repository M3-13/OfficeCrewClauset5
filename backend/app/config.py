import os
from dataclasses import dataclass


@dataclass
class Settings:
    JWT_SECRET: str = os.environ.get("JWT_SECRET", "")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    DATABASE_URL: str = "sqlite:///./clauset.db"
    UPLOAD_DIR: str = "uploads"


settings = Settings()
