from fastapi.testclient import TestClient
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app
from config import setting
from database import Base, get_db
from models import User


SQLALCHEMY_TEST_DB_URL = setting.TEST_DB_URL
engine = create_engine(SQLALCHEMY_TEST_DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base.metadata.create_all(bind=engine)

@pytest.fixture
# functions that run before each test function, and shares across all the files
#
def client():
    def override_get_db():
        try:
            db=TestingSessionLocal()
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db]=override_get_db

    client = TestClient(app) # no need to run the application for running test cases bcaz of TestClient
    yield client

@pytest.fixture
def token_header(client:TestClient):
    db=TestingSessionLocal()
    user=db.query(User).filter(User.email==setting.TEST_EMAIL).first()
    if user is None:
        user = User(email=setting.TEST_EMAIL,password=setting.TEST_PASSWORD)
        db.add(user)
        db.commit()
        db.refresh(user)
    data = {"username":setting.TEST_EMAIL,"password":setting.TEST_PASSWORD}
    response = client.post("/login/token",data=data)
    access_token = response.json().get("access_token")
    return {
        "Authorization": f'Bearer {response.get(access_token)}'
    }