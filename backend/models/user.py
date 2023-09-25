from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from database.base import Base
from database.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
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

def get_user(username: str, db: Session = Depends(get_db)):
    db_user = db.query(UserInDB).filter(UserInDB.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user