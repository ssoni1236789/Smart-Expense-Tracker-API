def test_get_expenses_empty(client):
    response = client.get("/expenses")
    assert response.status_code == 200
    assert response.json() == []

def test_get_expenses_with_data(client):
    client.post("/expenses", json={"title": "Netflix", "amount": 15.99, "category": "Entertainment", "date": "2023-10-24"})
    client.post("/expenses", json={"title": "AWS", "amount": 100.0, "category": "Infrastructure", "date": "2023-10-25"})
    
    response = client.get("/expenses")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

def test_get_expenses_by_category(client):
    client.post("/expenses", json={"title": "Netflix", "amount": 15.99, "category": "Entertainment", "date": "2023-10-24"})
    client.post("/expenses", json={"title": "AWS", "amount": 100.0, "category": "Infrastructure", "date": "2023-10-25"})
    
    response = client.get("/expenses?category=Entertainment")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["category"] == "Entertainment"
