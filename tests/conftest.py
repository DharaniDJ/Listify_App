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