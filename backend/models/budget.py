from pydantic import BaseModel

class BudgetItem(BaseModel):
    name: str
    monthly_cost: float

class UserBudget(BaseModel):
    user_id: str  # The unique identifier from Auth0 or other auth services
    income: float
    savings_goal: float
    expenses: list[BudgetItem]
