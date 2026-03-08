from pydantic import BaseModel
from typing import List
from datetime import datetime


class StartPosition(BaseModel):
    x: int
    y: int


class Command(BaseModel):
    direction: str
    steps: int


class RobotPathRequest(BaseModel):
    start: StartPosition
    commands: List[Command]


class ExecutionResponse(BaseModel):
    id: int
    timestamp: datetime
    commands: int
    result: int
    duration: float

    class Config:
        orm_mode = True
