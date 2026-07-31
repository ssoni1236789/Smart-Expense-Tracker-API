def test_update_expense_success(client):
    post_res = client.post("/expenses", json={"title": "Netflix", "amount": 15.99, "category": "Entertainment", "date": "2023-10-24"})
    expense_id = post_res.json()["id"]
    
    put_res = client.put(f"/expenses/{expense_id}", json={
        "title": "Amazon Prime",
        "amount": 7.99,
        "category": "Entertainment",
        "date": "2026-07-31"
    })
    
    assert put_res.status_code == 200
    data = put_res.json()
    assert data["title"] == "Amazon Prime"
    assert data["amount"] == 7.99
    assert data["category"] == "Entertainment"
    assert data["date"] == "2026-07-31"
    assert data["id"] == expense_id

def test_update_expense_invalid_uuid(client):
    put_res = client.put("/expenses/abc", json={
        "title": "Amazon Prime",
        "amount": 7.99,
        "category": "Entertainment",
        "date": "2026-07-31"
    })
    
    assert put_res.status_code == 422

def test_update_expense_not_found(client):
    from uuid import uuid4
    put_res = client.put(f"/expenses/{uuid4()}", json={
        "title": "Amazon Prime",
        "amount": 7.99,
        "category": "Entertainment",
        "date": "2026-07-31"
    })
    
    assert put_res.status_code == 404
