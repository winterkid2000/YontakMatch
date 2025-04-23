from fastapi import FastAPI
from api import user, ride_request, ride_proposal
from database.session import engine
from models import user as user_models
from models import ride_request as ride_models
from models import ride_proposal as proposal_models

# DB 테이블 생성
user_models.Base.metadata.create_all(bind=engine)
ride_models.Base.metadata.create_all(bind=engine)
proposal_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 라우터 등록
app.include_router(user.router, prefix="/api/user", tags=["User"])
app.include_router(ride_request.router, prefix="/api/ride_requests", tags=["Ride Requests"])
app.include_router(ride_proposal.router, prefix="/api/ride_proposals", tags=["Ride Proposals"])
