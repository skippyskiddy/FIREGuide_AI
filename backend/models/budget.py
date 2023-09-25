
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database.base import Base

from typing import List
from pydantic import BaseModel

class BudgetItem(BaseModel):
    name: str
    amount: float

class UserBudget(BaseModel):
    income: float
    expenses: List[BudgetItem]


class UserBudgetInDB(Base):
    __tablename__ = "user_budgets"

    user_id = Column(Integer, primary_key=True, index=True)
    income = Column(Float, index=True, default=0)
    expenses = relationship("BudgetItemInDB", back_populates="owner")

class BudgetItemInDB(Base):
    __tablename__ = "budget_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Float)
    owner_id = Column(Integer, ForeignKey("user_budgets.user_id"))
    owner = relationship("UserBudgetInDB", back_populates="expenses")

