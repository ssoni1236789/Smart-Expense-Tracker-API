import logging
from typing import List, Optional
from uuid import UUID
from .models import Expense, ExpenseCreate, ExpenseUpdate
from . import storage

logger = logging.getLogger(__name__)

def create_expense(expense_in: ExpenseCreate) -> Expense:
    expenses = storage.load_expenses()
    expense = Expense(**expense_in.model_dump())
    expenses.append(expense)
    storage.save_expenses(expenses)
    logger.info(f"Expense created: {expense.id}")
    return expense

def get_expenses(category: Optional[str] = None) -> List[Expense]:
    expenses = storage.load_expenses()
    if category:
        result = [e for e in expenses if e.category.lower() == category.lower()]
        logger.info(f"Retrieved {len(result)} expenses for category '{category}'")
        return result
    logger.info(f"Retrieved all expenses (total: {len(expenses)})")
    return expenses

def calculate_totals() -> dict:
    expenses = storage.load_expenses()
    overall = sum(e.amount for e in expenses)
    by_category = {}
    for e in expenses:
        by_category[e.category] = by_category.get(e.category, 0) + e.amount
    logger.info(f"Calculated totals for {len(expenses)} expenses")
    return {"overall": overall, "by_category": by_category}

def monthly_summary() -> dict:
    expenses = storage.load_expenses()
    by_month = {}
    for e in expenses:
        month = e.date.strftime("%Y-%m")
        by_month[month] = by_month.get(month, 0) + e.amount
    logger.info(f"Calculated monthly summary for {len(expenses)} expenses")
    return {"by_month": by_month}

def delete_expense(expense_id: UUID) -> bool:
    expenses = storage.load_expenses()
    initial_length = len(expenses)
    expenses = [e for e in expenses if e.id != expense_id]
    if len(expenses) < initial_length:
        storage.save_expenses(expenses)
        logger.info(f"Deleted expense {expense_id}")
        return True
    logger.warning(f"Expense {expense_id} not found for deletion")
    return False

def update_expense(expense_id: UUID, expense: ExpenseUpdate) -> Optional[Expense]:
    expenses = storage.load_expenses()
    for item in expenses:
        if item.id == expense_id:
            item.title = expense.title
            item.amount = expense.amount
            item.category = expense.category
            item.date = expense.date
            storage.save_expenses(expenses)
            logger.info(f"Updated expense {expense_id}")
            return item
    logger.warning(f"Expense {expense_id} not found for update")
    return None
