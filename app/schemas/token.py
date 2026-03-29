from pydantic import BaseModel

# What we send back after successful login
class TokenResponse(BaseModel):
    access_token: str          # the JWT token
    token_type:   str = "bearer"
    name:         str
    email:        str
    role:         str