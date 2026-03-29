from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.base import Base

# This enum defines the two allowed roles
class UserRole(str, enum.Enum):
    USER  = "USER"
    ADMIN = "ADMIN"

class User(Base):
    # __tablename__ tells SQLAlchemy what the table is called in DB
    __tablename__ = "users"

    # Each Column = one column in the database table
    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(100), nullable=False)
    email      = Column(String(150), unique=True, nullable=False, index=True)
    password   = Column(String(255), nullable=False)
    role       = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # This creates the relationship between User and Task
    # One user can have MANY tasks
    # "cascade all delete" = if user deleted, their tasks are also deleted
    tasks = relationship(
        "Task",
        back_populates="user",
        cascade="all, delete-orphan"
    )