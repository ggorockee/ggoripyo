# =================================================================
# 파일: app/db/models/user.py
# 역할: User 테이블 SQLAlchemy 모델. BaseModel 상속.
# =================================================================
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    nick_name = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    bookmarks = relationship("Bookmark", back_populates="owner", cascade="all, delete-orphan")