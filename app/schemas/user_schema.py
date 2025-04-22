from pydantic import BaseModel, EmailStr

class UserSignup(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserVerify(BaseModel):
    email: EmailStr
    otp_code: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_verified: bool

    class Config:
        orm_mode = True
