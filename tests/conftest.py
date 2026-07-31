import pytest
from fastapi.testclient import TestClient
from src.main import app
import src.storage

@pytest.fixture(autouse=True)
def setup_test_storage(tmp_path):
    # Override the storage file path to use a temporary file for tests
    test_file = tmp_path / "test_expenses.json"
    src.storage.STORAGE_FILE = str(test_file)
    yield test_file

@pytest.fixture
def client():
    return TestClient(app)
