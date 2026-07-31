# AI Usage Notes

## AI Usage Summary

AI tools (ChatGPT, Claude, Gemini) were used to assist with brainstorming, project structure, and implementation guidance. All generated code was reviewed, modified, tested, and validated manually before being used.

## 1. AI-Assisted Components

The following aspects were initially generated or assisted by AI:

- FastAPI project structure and folder organization.
- Initial Pydantic models for request and response validation.
- Basic CRUD endpoint scaffolding.
- JSON file storage approach.
- Initial pytest test case templates.
- Logging setup using Python's built-in `logging` module.
- README and documentation suggestions.

## 2. Manual Development and Validation

I manually reviewed, modified, and validated all AI-generated code before using it, and researched across different resources to improve the code and implement additional features. Changes made include:

- Refactored the project into separate `routes`, `service`, and `storage` layers to improve maintainability.
- Split models into `ExpenseCreate` and `Expense` so clients cannot provide custom IDs.
- Used `datetime.date` in Pydantic models for strict ISO date validation.
- Added proper HTTP status codes (`201`, `204`, `404`, `422`).
- Implemented JSON persistence with separate storage logic.
- Added an `Update Expense (PUT)` endpoint as an additional enhancement.
- Added structured logging (INFO, WARNING, ERROR) for important operations and failures.
- Wrote and expanded the automated pytest test suite.
- Verified every endpoint manually using FastAPI's Swagger UI (`/docs`).
- Fixed issues found during testing until all automated tests passed.

## 3. AI Suggestions Not Used

Some AI suggestions were intentionally not implemented because they were outside the assignment scope:

- SQLite/PostgreSQL database integration.
- User authentication (JWT).
- React frontend.
- Docker containerization.
- Redis caching.

These were excluded because the assignment explicitly called for JSON file storage and focused on building a REST API, not a full-stack or production-hardened system.

## 4. Validation Performed

**Automated testing:**
- All endpoint tests were executed using pytest.
- Final result: **13 tests passed**.

**Manual testing:**
- Verified all endpoints through FastAPI's Swagger UI.
- Tested successful and invalid requests.
- Verified category filtering.
- Verified total and monthly summary calculations.
- Verified update and delete operations.
- Verified invalid UUID and invalid date handling.
- Confirmed logging output for INFO, WARNING, and ERROR scenarios.

##5. Architectural Decisions

- FastAPI was selected for automatic validation and OpenAPI documentation.
- Business logic was separated into a dedicated service layer.
- JSON storage was used to satisfy the assignment requirements.
- Tests use a temporary JSON file to prevent modifying production data.
- Pydantic models enforce strict validation for all incoming requests.
