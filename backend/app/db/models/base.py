# =================================================================
# 파일: app/db/models/base.py
# 역할: 모든 SQLAlchemy 모델이 상속받을 공통 BaseModel 정의.
# =================================================================
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from zoneinfo import ZoneInfo # zoneinfo 임포트

Base = declarative_base()

class BaseModel(Base):
    """
    모든 모델이 공통으로 사용할 필드를 정의한 추상 베이스 모델.
    - id: Primary Key
    - created_at: 생성일시
    - updated_at: 수정일시
    """
    __abstract__ = True # 이 모델은 DB 테이블로 생성되지 않음.

    id = Column(Integer, primary_key=True, index=True)
    # 타임존을 'Asia/Seoul'로 변경
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(ZoneInfo("Asia/Seoul")), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(ZoneInfo("Asia/Seoul")), onupdate=lambda: datetime.now(ZoneInfo("Asia/Seoul")), nullable=False)

