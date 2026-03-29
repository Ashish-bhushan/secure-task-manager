from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# create_engine = creates the actual connection to PostgreSQL
# pool_pre_ping = checks connection is alive before using it
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

# sessionmaker = a factory that creates database sessions
# Think of a session like a "conversation" with the database
SessionLocal = sessionmaker(
    autocommit=False,   # don't auto-save changes
    autoflush=False,    # don't auto-send queries
    bind=engine         # use our engine
)

def get_db():
    """
    This is a FastAPI dependency.
    It gives a DB session to each API route.
    It automatically closes the session when the request is done.

    How it works:
    1. Route calls get_db()
    2. get_db creates a session
    3. yield gives session to the route
    4. Route does its work
    5. finally: closes the session
    """
    db = SessionLocal()
    try:
        yield db        # give db session to route
    finally:
        db.close()      # always close when done