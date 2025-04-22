from pydantic import BaseModel, EmailStr
from datetime import datetime

class RideRequestCreate(BaseModel):
    email: EmailStr
    departure: str
    destination: str

class RideRequestOut(BaseModel):
    id: int
    email: EmailStr
    departure: str
    destination: str
    is_matched: bool
    created_at: datetime

    class Config:
        orm_mode = True

