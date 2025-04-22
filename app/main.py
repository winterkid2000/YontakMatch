from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import request, user, group

app = FastAPI()

# 프론트엔드 개발용 CORS 설정 (나중에 도메인 제한 가능)
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(request.router, prefix="/api", tags=["Ride Request"])
app.include_router(user.router, prefix="/api", tags=["User"])
app.include_router(group.router, prefix="/api", tags=["Group"])

# 헬스 체크용 루트 엔드포인트
@app.get("/")
def root():
    return {"message": "YontakMatch backend is running"}

