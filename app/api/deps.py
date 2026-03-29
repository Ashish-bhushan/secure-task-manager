from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import decode_access_token
from app.models.user import User, UserRole
from app.core.logging_setup import logger

# HTTPBearer reads the "Authorization: Bearer <token>" header
bearer_scheme = HTTPBearer()

def get_current_user(
    # FastAPI automatically reads the Authorization header
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Reads JWT token from request header.
    Finds the user in database.
    Returns the User object.
    Raises 401 error if token is invalid.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Get the token string from "Bearer <token>"
    token = credentials.credentials

    # Decode the JWT token
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    # Get email from inside the token
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception

    # Find this user in the database
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user     # return the user to the route

def get_admin_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Checks that current user is ADMIN.
    Raises 403 Forbidden if not admin.
    """
    if current_user.role != UserRole.ADMIN:
        logger.warning(f"Non-admin tried admin route: {current_user.email}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user