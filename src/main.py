import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from src.database import engine, Base
from src.routers import robot

# Robust Database Startup (Retry Logic)
for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        print("Database connected and tables created!")
        break
    except OperationalError:
        print(f"Database not ready yet, retrying in 2 seconds... (Attempt {i+1}/5)")
        time.sleep(2)

app = FastAPI()

# Include the endpoints from the router
app.include_router(robot.router)
