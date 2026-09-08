from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import Config

config = Config()
engine = create_engine(config.DATABASE_URL, pool_pre_ping=True)

# Create the Tables
SQLModel.metadata.create_all(engine)

SessionLocal = Session(bind=engine, autoflush=False, expire_on_commit=False)

def get_db_session() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session
