from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.task import Task
from app.models.user import User, UserRole
from app.schemas.task import TaskCreateRequest, TaskUpdateRequest
from app.core.logging_setup import logger
from datetime import datetime
from typing import List

def create_task(request: TaskCreateRequest, user: User, db: Session) -> Task:
    """Creates a new task and links it to the current user."""
    task = Task(
        title=request.title,
        description=request.description,
        status=request.status,
        user_id=user.id             # link to current user
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    logger.info(f"Task created: '{task.title}' by {user.email}")
    return task

def get_my_tasks(user: User, db: Session) -> List[Task]:
    """Returns only tasks that belong to current user."""
    tasks = db.query(Task).filter(Task.user_id == user.id).all()
    return tasks

def get_all_tasks(db: Session) -> List[Task]:
    """Returns ALL tasks — for admin use only."""
    return db.query(Task).all()

def update_task(
    task_id: int,
    request: TaskUpdateRequest,
    user: User,
    db: Session
) -> Task:
    """Updates a task. Only owner or admin can update."""

    # Find the task
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    # Check if user owns this task OR is admin
    if task.user_id != user.id and user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own tasks"
        )

    # Update only fields that were provided
    if request.title is not None:
        task.title = request.title
    if request.description is not None:
        task.description = request.description
    if request.status is not None:
        task.status = request.status

    task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(task)
    logger.info(f"Task {task_id} updated by {user.email}")
    return task

def delete_task(task_id: int, user: User, db: Session) -> dict:
    """Deletes a task. Only owner or admin can delete."""

    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    if task.user_id != user.id and user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own tasks"
        )

    db.delete(task)
    db.commit()
    logger.info(f"Task {task_id} deleted by {user.email}")
    return {"message": "Task deleted successfully"}