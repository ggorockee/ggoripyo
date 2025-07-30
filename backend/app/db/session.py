# =================================================================
# 파일: app/db/session.py
# 역할: SQLAlchemy 데이터베이스 세션 설정.
# =================================================================
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)