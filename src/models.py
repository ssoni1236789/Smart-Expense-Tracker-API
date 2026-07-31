from datetime import date
from typing import Annotated
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1)
    date: date

class ExpenseUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1)
    date: date

class Expense(ExpenseCreate):
    id: UUID = Field(default_factory=uuid4)

