# =================================================================
# 파일: app/api/v1/endpoints/auth.py
# 역할: 인증(회원가입, 로그인) API 엔드포인트.
# =================================================================
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.api.v1 import schemas
from app.crud import crud_user
from app.core import security
from app.core.config import settings
from app.db.models import user as user_model
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

@router.post("/users", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이런, 이 이메일은 이미 다른 사람이 사용 중이에요.")
    return crud_user.create_user(db=db, user=user)

@router.get("/users/me", response_model=schemas.User, status_code=status.HTTP_200_OK)
def me(user: schemas.User, db: Session = Depends(get_db)):
    pass

@router.post("/token")
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud_user.get_user_by_email(db, email=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일이나 비밀번호가...흠...다시 확인해볼까요?",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> user_model.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="음... 님 누구세요? 유효한 신분증(토큰)이 필요해요!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud_user.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user