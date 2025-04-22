from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.ride_group import RideGroup, RideRequestInGroup
from app.models.ride_request import RideRequest
from app.schemas.group_schema import GroupOut
from app.services.match_engine import find_matchable_requests
from typing import List

router = APIRouter()

@router.post("/group/match", response_model=List[GroupOut])
def auto_match_groups(db: Session = Depends(get_db)):
    matched_groups = find_matchable_requests(db)
    result = []

    for group_requests in matched_groups:
        if len(group_requests) < 2:
            continue

        departure = group_requests[0].departure
        destination = group_requests[0].destination

        new_group = RideGroup(departure=departure, destination=destination)
        db.add(new_group)
        db.commit()
        db.refresh(new_group)

        for req in group_requests:
            req.is_matched = True
            mapping = RideRequestInGroup(group_id=new_group.id, request_id=req.id)
            db.add(mapping)

        db.commit()

        result.append(GroupOut(
            id=new_group.id,
            departure=new_group.departure,
            destination=new_group.destination,
            created_at=new_group.created_at,
            request_ids=[r.id for r in group_requests],
            is_completed=new_group.is_completed
        ))

    return result


@router.get("/group", response_model=List[GroupOut])
def list_groups(db: Session = Depends(get_db)):
    groups = db.query(RideGroup).filter(RideGroup.is_completed == False).all()
    result = []

    for group in groups:
        mappings = db.query(RideRequestInGroup).filter(RideRequestInGroup.group_id == group.id).all()
        request_ids = [m.request_id for m in mappings]

        result.append(GroupOut(
            id=group.id,
            departure=group.departure,
            destination=group.destination,
            created_at=group.created_at,
            request_ids=request_ids,
            is_completed=group.is_completed
        ))

    return result


#이동 완료 처리 API 추가
@router.post("/group/{group_id}/complete")
def complete_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(RideGroup).filter(RideGroup.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="그룹이 존재하지 않습니다.")

    group.is_completed = True
    db.commit()
    return {"message": "그룹 이동이 완료되었습니다."}

        ))

    return result

