from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import Config

config = Config()
engine = create_engine(config.DATABASE_URL, pool_pre_ping=True, echo=True)

# Create the Tables
print("Creating tables...")
SQLModel.metadata.create_all(engine)

def get_db_session() -> Generator[Session, None, None]:
    """Creates a database session per request and closes it after."""
    db = Session(engine)
    try:
        yield db  # Hand over the session to whatever needs it
    finally:
        db.close()  # Guaranteed to run after the API request finishes
