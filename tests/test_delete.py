def test_delete_expense_success(client):
    post_res = client.post("/expenses", json={"title": "Netflix", "amount": 15.99, "category": "Entertainment", "date": "2023-10-24"})
    expense_id = post_res.json()["id"]
    
    del_res = client.delete(f"/expenses/{expense_id}")
    assert del_res.status_code == 204
    
    get_res = client.get("/expenses")
    assert len(get_res.json()) == 0

def test_delete_expense_not_found(client):
    from uuid import uuid4
    del_res = client.delete(f"/expenses/{uuid4()}")
    assert del_res.status_code == 404
