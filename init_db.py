from app.models.ride_request import Base as RequestBase
from app.models.ride_user import Base as UserBase
from app.models.ride_group import Base as GroupBase
from app.database.session import engine

# 모든 모델의 Base들을 모아서 테이블 생성
RequestBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)
GroupBase.metadata.create_all(bind=engine)

print("DB 테이블이 생성되었습니다.")

