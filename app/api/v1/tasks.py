from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.task import TaskCreateRequest, TaskUpdateRequest, TaskResponse
from app.services import task_service
from app.api.deps import get_current_user, get_admin_user
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(
    request: TaskCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # JWT required
):
    return task_service.create_task(request, current_user, db)

@router.get("/my", response_model=List[TaskResponse])
def get_my_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.get_my_tasks(current_user, db)

@router.get("/all", response_model=List[TaskResponse])
def get_all_tasks(
    db: Session = Depends(get_db),
    admin_user: User = Depends(get_admin_user)  # ADMIN only
):
    return task_service.get_all_tasks(db)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    request: TaskUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.update_task(task_id, request, current_user, db)

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_service.delete_task(task_id, current_user, db)