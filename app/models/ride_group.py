from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class RideGroup(Base):
    __tablename__ = "ride_groups"

    id = Column(Integer, primary_key=True, index=True)
    departure = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_completed = Column(Boolean, default=False)  #이동 완료 여부

    requests = relationship("RideRequestInGroup", back_populates="group")


class RideRequestInGroup(Base):
    __tablename__ = "ride_requests_in_group"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("ride_groups.id"))
    request_id = Column(Integer, ForeignKey("ride_requests.id"))
    joined_at = Column(DateTime, default=datetime.utcnow)

    group = relationship("RideGroup", back_populates="requests")

