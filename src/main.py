import time
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from . import models, database, robot

# Create tables
database.Base.metadata.create_all(bind=database.engine)
for i in range(5):
    try:
        database.Base.metadata.create_all(bind=database.engine)
        print("Database connected and tables created!")
        break
    except OperationalError:
        print(f"Database not ready yet, retrying in 2 seconds... (Attempt {i+1}/5)")
        time.sleep(2)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Request method: POST [cite: 14]
# Request path: /tibber-developer-test/enter-path [cite: 15]
@app.post("/tibber-developer-test/enter-path", response_model=models.ExecutionResponse)
def enter_path(payload: models.RobotPathRequest, db: Session = Depends(get_db)):
    start_time = time.time()

    # Calculate unique places
    unique_places = robot.calculate_unique_places(
        start_x=payload.start.x, start_y=payload.start.y, commands=payload.commands
    )

    # Calculate duration of the calculation in seconds
    duration = time.time() - start_time

    # Store the results into the database [cite: 12]
    db_execution = database.Execution(
        commands=len(payload.commands), result=unique_places, duration=duration
    )
    db.add(db_execution)
    db.commit()
    db.refresh(db_execution)

    # Return the created record in JSON format [cite: 12]
    return db_execution
