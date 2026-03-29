from pydantic import BaseModel, Field
from datetime import datetime
from app.models.task import TaskStatus
from typing import Optional

# ── Create Task ───────────────────────────────────────────────────
class TaskCreateRequest(BaseModel):
    title:       str           = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status:      TaskStatus    = TaskStatus.TODO   # default is TODO

# ── Update Task (all fields optional) ────────────────────────────
class TaskUpdateRequest(BaseModel):
    title:       Optional[str]        = None
    description: Optional[str]        = None
    status:      Optional[TaskStatus] = None

# ── Response (what we send back) ─────────────────────────────────
class TaskResponse(BaseModel):
    id:          int
    title:       str
    description: Optional[str]
    status:      TaskStatus
    user_id:     int
    created_at:  datetime
    updated_at:  datetime

    model_config = {"from_attributes": True}