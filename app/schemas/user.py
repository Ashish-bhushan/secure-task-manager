from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from app.models.user import UserRole

# ── What frontend SENDS to register ──────────────────────────────
class RegisterRequest(BaseModel):
    name: str = Field(
        ...,                    # ... means REQUIRED
        min_length=2,
        max_length=100,
        description="Your full name"
    )
    email: EmailStr = Field(
        ...,
        description="Valid email like john@example.com"
    )
    password: str = Field(
        ...,
        min_length=6,
        description="Minimum 6 characters"
    )

# ── What frontend SENDS to login ──────────────────────────────────
class LoginRequest(BaseModel):
    email:    EmailStr
    password: str

# ── What we SEND BACK about a user ───────────────────────────────
class UserResponse(BaseModel):
    id:         int
    name:       str
    email:      EmailStr
    role:       UserRole
    created_at: datetime

    # This allows pydantic to read SQLAlchemy model objects
    model_config = {"from_attributes": True}