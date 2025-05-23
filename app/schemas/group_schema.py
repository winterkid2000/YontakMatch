from pydantic import BaseModel
from datetime import datetime
from typing import List

class GroupCreate(BaseModel):
    departure: str
    destination: str
    request_ids: List[int]

class GroupOut(BaseModel):
    id: int
    departure: str
    destination: str
    created_at: datetime
    request_ids: List[int]
    is_completed: bool  #응답에 포함

    class Config:
        orm_mode = True
