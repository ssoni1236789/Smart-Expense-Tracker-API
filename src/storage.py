import json
import os
import logging
from typing import List
from .models import Expense

logger = logging.getLogger(__name__)

STORAGE_FILE = os.path.join(os.path.dirname(__file__), "expenses.json")

def load_expenses() -> List[Expense]:
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return [Expense.model_validate(item) for item in data]
        except json.JSONDecodeError as e:
            logger.error(f"Failed to read {STORAGE_FILE}: {e}")
            return []

def save_expenses(expenses: List[Expense]) -> None:
    try:
        with open(STORAGE_FILE, "w", encoding="utf-8") as f:
            json.dump([exp.model_dump(mode="json") for exp in expenses], f, indent=4)
    except Exception as e:
        logger.error(f"Failed to write to {STORAGE_FILE}: {e}")
