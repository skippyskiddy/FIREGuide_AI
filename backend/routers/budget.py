from models.budget import UserBudget, BudgetItem, UserBudgetInDB, BudgetItemInDB
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}", response_model=UserBudget)
def get_user_budget(user_id: int, db: Session = Depends(get_db)):
    budget = db.query(UserBudgetInDB).filter(UserBudgetInDB.user_id == user_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

@router.post("/{user_id}", response_model=UserBudget)
def update_user_budget(user_id: int, budget: UserBudget, db: Session = Depends(get_db)):
    db_budget = db.query(UserBudgetInDB).filter(UserBudgetInDB.user_id == user_id).first()
    if not db_budget:
        db_budget = UserBudgetInDB(user_id=user_id)
        db.add(db_budget)

    db_budget.income = budget.income

    existing_expenses = {expense.name.lower() for expense in db.query(BudgetItemInDB.name).filter(BudgetItemInDB.owner_id == user_id).all()}

    # Add expenses
    for expense in budget.expenses:
        # Check if this expense type/name exists (case-insensitive check)
        if expense.name.lower() not in existing_expenses:
            db_expense = BudgetItemInDB(**expense.model_dump(), owner_id=user_id)
            db.add(db_expense)

    db.commit()
    db.refresh(db_budget)
    return db_budget



@router.put("/{user_id}/add_expense", response_model=UserBudget)
def add_expense(user_id: int, expense: BudgetItem, db: Session = Depends(get_db)):
    db_budget = db.query(UserBudgetInDB).filter(UserBudgetInDB.user_id == user_id).first()
    if not db_budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    db_expense = BudgetItemInDB(**expense.dict(), owner_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db.query(UserBudgetInDB).filter(UserBudgetInDB.user_id == user_id).first()
