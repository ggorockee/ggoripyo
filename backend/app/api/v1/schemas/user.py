# =================================================================
# 파일: app/api/v1/schemas/user.py
# 역할: User 관련 Pydantic 스키마 (데이터 유효성 검사).
# =================================================================
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    nick_name: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True