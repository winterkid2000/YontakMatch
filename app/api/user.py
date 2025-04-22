from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.ride_user import RideUser
from app.schemas.user_schema import UserSignup, UserLogin, UserVerify, UserOut
from app.utils.email import generate_otp, send_otp_email
from app.core.security import create_access_token
import bcrypt

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    if not (user.email.endswith("@yonsei.ac.kr") or user.email.endswith("@mirae.yonsei.ac.kr")):
        raise HTTPException(status_code=400, detail="연세 메일만 사용 가능합니다.")

    db_user = db.query(RideUser).filter(RideUser.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")

    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
    otp = generate_otp()

    new_user = RideUser(email=user.email, password=hashed_pw, otp_code=otp)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    send_otp_email(user.email, otp)

    return new_user

@router.post("/verify")
def verify(user: UserVerify, db: Session = Depends(get_db)):
    db_user = db.query(RideUser).filter(RideUser.email == user.email).first()
    if not db_user or db_user.otp_code != user.otp_code:
        raise HTTPException(status_code=400, detail="인증 실패")

    db_user.is_verified = True
    db_user.otp_code = None
    db.commit()
    return {"message": "이메일 인증 완료"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(RideUser).filter(RideUser.email == user.email).first()
    if not db_user or not bcrypt.checkpw(user.password.encode(), db_user.password.encode()):
        raise HTTPException(status_code=400, detail="잘못된 로그인 정보입니다.")

    if not db_user.is_verified:
        raise HTTPException(status_code=403, detail="이메일 인증이 필요합니다.")

    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
