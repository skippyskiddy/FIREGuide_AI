from pydantic import BaseModel

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from ..database.base import Base

# SQLAlchemy model
class UserInDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    hashed_password = Column(String)

# Pydantic models
class User(BaseModel):
    username: str
    email: str
    full_name: str
    hashed_password: str

class UserInDBBase(User):
    id: int

    class Config:
        orm_mode = True

