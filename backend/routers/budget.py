from fastapi import APIRouter, HTTPException
from models.budget import UserBudget, BudgetItem

router = APIRouter()

# Simulated in-memory database
user_budgets = {}

@router.get("/budget/{user_id}", response_model=UserBudget)
def get_user_budget(user_id: str):
    budget = user_budgets.get(user_id)
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

@router.post("/budget/{user_id}", response_model=UserBudget)
def update_user_budget(user_id: str, budget: UserBudget):
    user_budgets[user_id] = budget
    return budget

@router.put("/budget/{user_id}/add_expense", response_model=UserBudget)
def add_expense(user_id: str, expense: BudgetItem):
    if user_id not in user_budgets:
        raise HTTPException(status_code=404, detail="Budget not found")
    user_budgets[user_id].expenses.append(expense)
    return user_budgets[user_id]
