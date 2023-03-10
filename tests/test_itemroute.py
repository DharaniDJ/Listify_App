# use the TestClient object the same way as you do with requests
# i.e to call/hit the url
from fastapi.testclient import TestClient
import json
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app
from config import setting
from database import Base, get_db

SQLALCHEMY_TEST_DB_URL = setting.TEST_DB_URL
engine = create_engine(SQLALCHEMY_TEST_DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def override_get_db():
    try:
        db=TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db]=override_get_db

def test_create_item():
    data = {
        "title":"Item3",
        "description":"This is item3"
    }
    response = client.post("/item", json=data)
    assert response.status_code==200
