def test_create_expense_success(client):
    response = client.post("/expenses", json={
        "title": "Netflix",
        "amount": 15.99,
        "category": "Entertainment",
        "date": "2023-10-24"
    })
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "Netflix"
    assert data["amount"] == 15.99
    assert data["category"] == "Entertainment"
    assert data["date"] == "2023-10-24"

def test_create_expense_invalid_amount(client):
    response = client.post("/expenses", json={
        "title": "Netflix",
        "amount": -5,
        "category": "Entertainment",
        "date": "2023-10-24"
    })
    assert response.status_code == 422

def test_create_expense_missing_field(client):
    response = client.post("/expenses", json={
        "title": "Netflix",
        "amount": 15.99,
        "date": "2023-10-24"
    })
    assert response.status_code == 422
