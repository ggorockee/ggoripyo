# =================================================================
# 파일: app/crud/crud_bookmark.py
# 역할: Bookmark 모델 관련 CRUD(Repository Pattern).
# =================================================================
from sqlalchemy.orm import Session
from app.db.models import bookmark as models
from app.api.v1.schemas import bookmark as schemas

def get_bookmark(db: Session, bookmark_id: int):
    return db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()

def get_bookmarks_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Bookmark).filter(models.Bookmark.owner_id == owner_id).order_by(models.Bookmark.created_at.desc()).offset(skip).limit(limit).all()

def create_bookmark(db: Session, bookmark: schemas.BookmarkCreate, owner_id: int):
    # TODO: 여기에 BeautifulSoup, requests 등을 이용한 크롤링/아카이빙 로직 추가
    # 예: title, description이 비어있으면 url에서 가져오기
    db_bookmark = models.Bookmark(**bookmark.dict(), owner_id=owner_id)
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark