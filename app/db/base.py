from sqlalchemy.orm import DeclarativeBase

# All our database models (User, Task) will inherit from this
# It's like a parent class that gives them database superpowers
class Base(DeclarativeBase):
    pass