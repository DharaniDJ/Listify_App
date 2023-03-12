# use the TestClient object the same way as you do with requests
# i.e to call/hit the url
import json

def test_create_user(client):
    data = {
        "email":"testuser111@test.com",
        "password":"testuser111"
    }
    response = client.post("/users", json=data)
    assert response.status_code==200
    assert response.json()["email"]=="testuser111@test.com"
    assert response.json()["is_active"]==True
