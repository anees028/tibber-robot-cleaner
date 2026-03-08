from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from src.database import Base


class Execution(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    commands = Column(Integer)
    result = Column(Integer)
    duration = Column(Float)
