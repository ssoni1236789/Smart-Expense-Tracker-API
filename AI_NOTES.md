# Architectural Decisions

- **FastAPI**: Selected for its excellent validation (via Pydantic), async support, and auto-generated OpenAPI documentation (`/docs`), fulfilling the bonus requirement.
- **Data Models**: Split into `ExpenseCreate` (for incoming requests) and `Expense` (with server-generated `id`) to enforce strict input schemas and prevent clients from passing custom IDs.
- **Date Validation**: Utilized Python's `datetime.date` inside Pydantic models to automatically enforce strict `YYYY-MM-DD` ISO validation, eliminating the need for custom string regex parsing.
- **Service Layer**: Decoupled core business logic and storage handling (`src/service.py`) from API routing (`src/routes.py`). This keeps routes thin and testable.
- **JSON Storage**: For simplicity and adherence to requirements, `storage.py` writes to a local `expenses.json` file.
- **Test Pollution**: To prevent tests from polluting the production data, a `pytest` fixture (`tests/conftest.py`) patches `src.storage.STORAGE_FILE` to use a temporary JSON file via `tmp_path`. This ensures every test suite run starts with a clean slate.
