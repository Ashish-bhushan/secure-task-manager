from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt              # for JWT tokens
from passlib.context import CryptContext    # for password hashing
from app.core.config import settings

# pwd_context knows HOW to hash passwords using bcrypt
# bcrypt = super secure one-way hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ─────────────────────────────────────────────────────────────────
# PASSWORD FUNCTIONS
# ─────────────────────────────────────────────────────────────────

def hash_password(plain_password: str) -> str:
    """
    Converts plain text to hash.
    Example:
        "mypassword123"  →  "$2b$12$abc...xyz"
    The hash CANNOT be reversed back to plain text.
    """
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Checks if plain password matches hash.
    Example:
        verify_password("mypassword123", "$2b$12$abc...xyz")  → True
        verify_password("wrongpassword", "$2b$12$abc...xyz")  → False
    """
    return pwd_context.verify(plain_password, hashed_password)

# ─────────────────────────────────────────────────────────────────
# JWT FUNCTIONS
# ─────────────────────────────────────────────────────────────────

def create_access_token(data: dict) -> str:
    """
    Creates a JWT token.
    data = {"sub": "user@email.com", "role": "USER"}

    JWT = 3 parts joined by dots:
    eyHeader.eyPayload.eySignature
    """
    to_encode = data.copy()

    # Set expiry time
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    # Sign and create the token
    token = jwt.encode(
        to_encode,
        settings.SECRET_KEY,       # our secret key signs it
        algorithm=settings.ALGORITHM
    )
    return token

def decode_access_token(token: str) -> Optional[dict]:
    """
    Reads the data inside a JWT token.
    Returns None if token is expired or invalid.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload      # returns dict like {"sub": "user@email.com"}
    except JWTError:
        return None         # invalid or expired token