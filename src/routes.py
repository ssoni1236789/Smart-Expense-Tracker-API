from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from uuid import UUID

from .models import Expense, ExpenseCreate, ExpenseUpdate
from . import service

router = APIRouter()

@router.post("/expenses", response_model=Expense, status_code=status.HTTP_201_CREATED)
def create_expense(expense_in: ExpenseCreate):
    return service.create_expense(expense_in)

@router.get("/expenses", response_model=List[Expense])
def get_expenses(category: Optional[str] = None):
    return service.get_expenses(category)

@router.get("/expenses/total")
def get_totals():
    return service.calculate_totals()

@router.get("/expenses/summary/monthly")
def get_monthly_summary():
    return service.monthly_summary()

@router.delete("/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: UUID):
    success = service.delete_expense(expense_id)
    if not success:
        raise HTTPException(status_code=404, detail="Expense not found")
    return None

@router.put("/expenses/{expense_id}", response_model=Expense)
def update_expense(expense_id: UUID, expense: ExpenseUpdate):
    updated_expense = service.update_expense(expense_id, expense)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated_expense
