from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import RegisterRequest, LoginRequest
from app.schemas.token import TokenResponse
from app.core.security import hash_password, verify_password, create_access_token
from app.core.logging_setup import logger

def register_user(request: RegisterRequest, db: Session) -> dict:
    """
    Handles user registration.
    Steps:
    1. Check if email already exists
    2. Hash the password
    3. Save user to database
    """
    # Check if email already used
    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This email is already registered"
        )

    # Create User object
    new_user = User(
        name=request.name,
        email=request.email,
        password=hash_password(request.password)  # HASH before saving!
    )

    # Save to database
    db.add(new_user)       # add to session
    db.commit()            # save to database
    db.refresh(new_user)   # refresh to get the generated ID

    logger.info(f"New user registered: {request.email}")

    return {
        "message": "Registration successful! Please login.",
        "user_id": new_user.id
    }

def login_user(request: LoginRequest, db: Session) -> TokenResponse:
    """
    Handles user login.
    Steps:
    1. Find user by email
    2. Verify password
    3. Create JWT token
    4. Return token
    """
    # Find user
    user = db.query(User).filter(User.email == request.email).first()

    # If user not found OR password wrong → same error (security)
    # Don't reveal WHICH one was wrong!
    if not user or not verify_password(request.password, user.password):
        logger.warning(f"Failed login: {request.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create JWT token with user info inside
    token = create_access_token(data={
        "sub":  user.email,     # "sub" is standard JWT field for subject
        "role": user.role.value
    })

    logger.info(f"User logged in: {user.email}")

    return TokenResponse(
        access_token=token,
        token_type="bearer",
        name=user.name,
        email=user.email,
        role=user.role.value
    )