from app.db.base import Base
from app.db.session import engine
from app.core.logging_setup import logger

# These imports are needed so SQLAlchemy
# knows about our tables before creating them
from app.models import user, task  # noqa: F401

def init_db():
    """
    Creates all database tables.
    Runs once when server starts.
    If tables already exist, it skips them safely.
    """
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables ready ✅")