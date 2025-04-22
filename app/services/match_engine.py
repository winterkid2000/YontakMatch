from app.models.ride_request import RideRequest
from typing import List
from sqlalchemy.orm import Session

def find_matchable_requests(
    db: Session,
    min_group_size: int = 2,
    max_group_size: int = 4,
) -> List[List[RideRequest]]:
    """
    출발지+도착지가 같은 요청끼리 그룹핑.
    최소 min_group_size 이상일 때만 그룹 후보로 반환.
    """
    all_requests = db.query(RideRequest).filter(RideRequest.is_matched == False).all()

    groups = []
    grouped = set()

    for req in all_requests:
        if req.id in grouped:
            continue

        similar = [
            r for r in all_requests
            if r.id != req.id and
               r.departure == req.departure and
               r.destination == req.destination and
               r.id not in grouped
        ]

        if len(similar) + 1 >= min_group_size:
            group = [req] + similar[:max_group_size - 1]
            for r in group:
                grouped.add(r.id)
            groups.append(group)

    return groups

