# =================================================================
# 파일: app/api/v1/endpoints/bookmarks.py
# 역할: 북마크 CRUD 및 QR 생성 API 엔드포인트.
# =================================================================
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import qrcode
from io import BytesIO
from starlette.responses import StreamingResponse

from app.api.v1 import schemas
from app.crud import crud_bookmark
from app.db.models import user as user_model
from .auth import get_current_user, get_db

router = APIRouter()

@router.post("/", response_model=schemas.Bookmark, status_code=status.HTTP_201_CREATED)
def create_bookmark(
    *,
    db: Session = Depends(get_db),
    bookmark_in: schemas.BookmarkCreate,
    current_user: user_model.User = Depends(get_current_user)
):
    return crud_bookmark.create_bookmark(db=db, bookmark=bookmark_in, owner_id=current_user.id)

@router.get("/", response_model=list[schemas.Bookmark])
def read_my_bookmarks(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: user_model.User = Depends(get_current_user)
):
    return crud_bookmark.get_bookmarks_by_owner(db, owner_id=current_user.id, skip=skip, limit=limit)

@router.get("/{bookmark_id}/qr", response_class=StreamingResponse)
def get_bookmark_qr(
    bookmark_id: int, 
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user)
):
    db_bookmark = crud_bookmark.get_bookmark(db, bookmark_id=bookmark_id)
    if not db_bookmark:
        raise HTTPException(status_code=404, detail="앗, 찾으시는 북마크가 우주 저편으로 사라졌나봐요.")
    if db_bookmark.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="이건 비밀인데... 남의 북마크는 훔쳐볼 수 없어요!")

    img = qrcode.make(db_bookmark.url)
    buf = BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")