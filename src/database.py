from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.config.settings import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to inject DB session into routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
