import time
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models import schemas, domain
from src.services import robot_service
from src.database import get_db

router = APIRouter()


@router.post(
    "/tibber-developer-test/enter-path", response_model=schemas.ExecutionResponse
)
def enter_path(payload: schemas.RobotPathRequest, db: Session = Depends(get_db)):
    start_time = time.time()

    unique_places = robot_service.calculate_unique_places(
        start_x=payload.start.x, start_y=payload.start.y, commands=payload.commands
    )

    duration = time.time() - start_time

    db_execution = domain.Execution(
        commands=len(payload.commands), result=unique_places, duration=duration
    )
    db.add(db_execution)
    db.commit()
    db.refresh(db_execution)

    return db_execution
