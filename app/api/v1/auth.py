from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import RegisterRequest, LoginRequest
from app.schemas.token import TokenResponse
from app.services import auth_service

# APIRouter = groups related routes together
# prefix    = all routes here start with /auth
# tags      = groups them in Swagger docs
router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", status_code=201)
def register(
    request: RegisterRequest,     # Pydantic validates this automatically
    db: Session = Depends(get_db) # FastAPI injects DB session
):
    """Register a new user account."""
    return auth_service.register_user(request, db)

@router.post("/login", response_model=TokenResponse)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    """Login and receive JWT token."""
    return auth_service.login_user(request, db)