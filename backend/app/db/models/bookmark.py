# =================================================================
# 파일: app/db/models/bookmark.py
# 역할: Bookmark 테이블 SQLAlchemy 모델. BaseModel 상속.
# =================================================================
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Bookmark(BaseModel):
    __tablename__ = "bookmarks"

    url = Column(String, index=True, nullable=False)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    archived_content = Column(Text, nullable=True) # 아카이빙된 텍스트
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="bookmarks")
