# use the TestClient object the same way as you do with requests
# i.e to call/hit the url
from fastapi.testclient import TestClient
import json

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_create_user():
    data = {
        "email":"testuser1@test.com",
        "password":"testuser1"
    }
    response = client.post("/users", json=data)
    assert response.status_code==200
    assert response.json()["email"]=="testuser1@test.com"
    assert response.json()["is_active"]==True
