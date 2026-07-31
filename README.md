# Smart Expense Tracker API

A REST API backend for tracking personal expenses, built with FastAPI and Python.

## Quickstart

```bash
# Clone repository
git clone https://github.com/ssoni1236789/Smart-Expense-Tracker-API.git
cd Smart-Expense-Tracker-API

# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.\.venv\Scripts\activate

# Or on macOS/Linux:
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn src.main:app --reload

# Run tests
python -m pytest
```

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can access:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Example Requests

```bash
# Add an expense
curl -X POST http://127.0.0.1:8000/expenses \
  -H "Content-Type: application/json" \
  -d '{"title": "Groceries", "amount": 45.50, "category": "Food", "date": "2026-07-15"}'

# View all expenses
curl http://127.0.0.1:8000/expenses

# Filter expenses by category
curl "http://127.0.0.1:8000/expenses?category=Food"

# Get totals (overall + by category)
curl http://127.0.0.1:8000/expenses/total

# Get monthly summary
curl http://127.0.0.1:8000/expenses/summary/monthly

# Delete an expense (replace with a real id from the list response)
curl -X DELETE http://127.0.0.1:8000/expenses/<expense_id>

# Update an expense
curl -X PUT http://127.0.0.1:8000/expenses/<expense_id> \
  -H "Content-Type: application/json" \
  -d '{"title": "Groceries (updated)", "amount": 50.00, "category": "Food", "date": "2026-07-15"}'
```

## Notes

- `amount` must be greater than 0 — the API returns a 422 error otherwise.
- `date` must be in `YYYY-MM-DD` format.
- `expense_id` is a UUID assigned by the server, not a sequential integer. Fetch a real id from `GET /expenses` before testing update/delete.
