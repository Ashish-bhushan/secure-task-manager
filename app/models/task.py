from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.base import Base

class TaskStatus(str, enum.Enum):
    TODO        = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE        = "DONE"

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status      = Column(Enum(TaskStatus), default=TaskStatus.TODO)

    # ForeignKey links this to the users table
    # Every task MUST belong to a user
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at  = Column(DateTime, default=datetime.utcnow)
    updated_at  = Column(DateTime, default=datetime.utcnow,
                         onupdate=datetime.utcnow)

    # Many tasks → one user (reverse of User.tasks)
    user = relationship("User", back_populates="tasks")