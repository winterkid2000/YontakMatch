from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class RideRequestCreate(BaseModel):
    email: EmailStr
    departure: str
    destination: str
    departure_time: Optional[datetime] = None  #추가

class RideRequestOut(BaseModel):
    id: int
    email: EmailStr
    departure: str
    destination: str
    departure_time: Optional[datetime]
    is_matched: bool
    created_at: datetime

    class Config:
        orm_mode = True
