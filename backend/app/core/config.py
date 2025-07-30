# =================================================================
# 파일: app/core/config.py
# 역할: 환경변수를 Pydantic 모델로 관리.
# =================================================================
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 # 24시간

    class Config:
        env_file = ".env"

settings = Settings()