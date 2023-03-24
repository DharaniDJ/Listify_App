# use the TestClient object the same way as you do with requests
# i.e to call/hit the url
import json
from config import setting

def test_create_user(client):
    data = {
        "email":setting.TEST_EMAIL,
        "password":setting.TEST_PASSWORD
    }
    response = client.post("/users", json=data)
    assert response.status_code==200
    assert response.json()["email"]==setting.TEST_EMAIL
    assert response.json()["is_active"]==True
