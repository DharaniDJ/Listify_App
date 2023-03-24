# use the TestClient object the same way as you do with requests
# i.e to call/hit the url
import json

def test_create_item(client, token_header):
    data = {
        "title":"Item3",
        "description":"This is item3"
    }
    response = client.post("/item", json=data, headers=token_header)
    assert response.status_code==200

def test_retrieve_item_by_id(client):
    response = client.get("/item/5")
    assert response.status_code==200
    assert response.json()["title"]=="Item2"