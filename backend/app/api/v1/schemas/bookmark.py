# =================================================================
# 파일: app/api/v1/schemas/bookmark.py
# 역할: Bookmark 관련 Pydantic 스키마.
# =================================================================
from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime

class BookmarkCreate(BaseModel):
    url: HttpUrl = Field(..., description="저장할 링크, 인터넷 바다의 주소죠!")
    title: Optional[str] = Field(None, description="이 링크, 나중에 뭐라고 기억할까요? (없으면 저희가 찾아볼게요!)")
    description: Optional[str] = Field(None, description="메모가 필요하다면? 여기에 끄적여보세요.")

class BookmarkBase(BaseModel):
    id: int
    url: HttpUrl
    title: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Bookmark(BookmarkBase):
    owner_id: int