import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from typing import Generator


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:root@localhost:3306/sdtm_db"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # avoids stale connections
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db() -> Generator[Session, None, None]:
    """
    Create and close database session.
    """
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()