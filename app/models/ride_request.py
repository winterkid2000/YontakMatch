from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class RideRequest(Base):
    __tablename__ = "ride_requests"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, nullable=False)
    departure = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    is_matched = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

