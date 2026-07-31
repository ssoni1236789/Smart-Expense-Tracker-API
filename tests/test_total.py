def test_get_totals(client):
    client.post("/expenses", json={"title": "Netflix", "amount": 15.0, "category": "Entertainment", "date": "2023-10-24"})
    client.post("/expenses", json={"title": "AWS", "amount": 100.0, "category": "Infrastructure", "date": "2023-10-25"})
    
    response = client.get("/expenses/total")
    assert response.status_code == 200
    data = response.json()
    assert data["overall"] == 115.0
    assert data["by_category"]["Entertainment"] == 15.0
    assert data["by_category"]["Infrastructure"] == 100.0

def test_get_monthly_summary(client):
    client.post("/expenses", json={"title": "Netflix", "amount": 15.0, "category": "Entertainment", "date": "2023-10-24"})
    client.post("/expenses", json={"title": "AWS", "amount": 100.0, "category": "Infrastructure", "date": "2023-11-25"})
    
    response = client.get("/expenses/summary/monthly")
    assert response.status_code == 200
    data = response.json()
    assert "2023-10" in data["by_month"]
    assert "2023-11" in data["by_month"]
    assert data["by_month"]["2023-10"] == 15.0
    assert data["by_month"]["2023-11"] == 100.0
