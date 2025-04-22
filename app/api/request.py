from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.ride_request import RideRequest
from app.schemas.request_schema import RideRequestCreate, RideRequestOut
from typing import List

router = APIRouter()

@router.post("/request", response_model=RideRequestOut)
def create_ride_request(request: RideRequestCreate, db: Session = Depends(get_db)):
    valid_places = {"연세대", "롯데마트", "원주역", "터미널", "롯데시네마"}
    if request.departure not in valid_places or request.destination not in valid_places:
        raise HTTPException(status_code=400, detail="출발지 또는 도착지가 유효하지 않습니다.")

    new_request = RideRequest(
        email=request.email,
        departure=request.departure,
        destination=request.destination
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

@router.get("/request", response_model=List[RideRequestOut])
def list_ride_requests(
    db: Session = Depends(get_db),
    departure: str = Query(None),
    destination: str = Query(None)
):
    query = db.query(RideRequest)
    if departure:
        query = query.filter(RideRequest.departure == departure)
    if destination:
        query = query.filter(RideRequest.destination == destination)
    return query.order_by(RideRequest.created_at.desc()).all()

