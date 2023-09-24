from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User, UserInDB  # Ensure this import is correct based on your folder structure.
from database.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserInDB).filter(UserInDB.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Convert the Pydantic model to the SQLAlchemy model
    db_user = UserInDB(**user.dict())
    
    # Add and commit to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user
