# =================================================================
# 파일: app/core/security.py
# 역할: 비밀번호 해싱 및 JWT 생성/검증 로직.
# =================================================================
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config import settings

# 비밀번호 해싱을 위한 컨텍스트
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # 입력된 비밀번호와 해시된 비밀번호 비교
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    # 비밀번호를 해시하여 반환
    return pwd_context.hash(password)

def create_access_token(data: dict) -> str:
    # JWT 액세스 토큰 생성
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt