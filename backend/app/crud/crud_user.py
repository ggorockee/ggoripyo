# =================================================================
# 파일: app/crud/crud_user.py
# 역할: User 모델 관련 CRUD(Repository Pattern).
# =================================================================
from sqlalchemy.orm import Session
from app.core.security import get_password_hash
from app.db.models import user as models
from app.api.v1.schemas import user as schemas
from fastapi import HTTPException

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    """
    새로운 사용자를 생성하고 데이터베이스에 저장합니다.

    - 요청 본문에 nickName이 없으면 이메일에서 @ 앞부분을 사용합니다.
    - 닉네임이 이미 존재하는지 확인하고, 중복 시 오류를 발생시킵니다.
    """
    hashed_password = get_password_hash(user.password)

    # requestBody에 nickName이 없으면 email에서 @앞에 id를 가져옴
    # 입력값이 있으면 그걸로 사용
    if user.nick_name and user.nick_name.strip():
        nick_name_to_use = user.nick_name.strip()
    else:
        nick_name_to_use = user.email.split("@")[0]

    # 2. 닉네임 중복 확인
    existing_user = db.query(models.User).filter(models.User.nick_name == nick_name_to_use).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            # 배달의 민족 스타일 멘트
            detail=f"앗! '{nick_name_to_use}' 닉네임은 이미 누군가 사용 중이에요. 더 멋진 닉네임을 고민해 볼까요?",
        )
    
    # 3. 이메일 중복 확인
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            # 카카오 스타일 멘트
            detail="혹시 쌍둥이신가요? 이 이메일은 이미 저희와 함께하고 있어요. 로그인을 시도해 보세요!",
        )

    
    # 4. 사용자 생성
    hashed_password = get_password_hash(user.password)
    
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        nick_name=nick_name_to_use,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user