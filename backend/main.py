# =================================================================
# 파일: main.py
# 역할: FastAPI 애플리케이션의 시작점. 라우터, 미들웨어 등을 설정.
# =================================================================
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import auth, bookmarks

app = FastAPI(title="나만의 우주 링크 저장소 API")

# CORS 미들웨어 설정 (프론트엔드와 통신을 위함)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 프로덕션에서는 프론트엔드 주소만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API v1 라우터 등록
app.include_router(auth.router, prefix="/api/v1", tags=["인증"])
app.include_router(bookmarks.router, prefix="/api/v1/bookmarks", tags=["북마크"])

@app.get("/", tags=["기본"])
def read_root():
    return {"message": "나만의 우주 링크 저장소에 오신 것을 환영합니다!"}