# Smart Expense Tracker API

A REST API backend for tracking personal expenses, built with FastAPI and Python.

## Quickstart

```bash
# Clone repository
git clone <repo-url>
cd expense-tracker

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
