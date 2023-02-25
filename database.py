from config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator

SQLALCHEMY_DB_URL = setting.DB_URL
engine = create_engine(SQLALCHEMY_DB_URL)
Sessionlocal = sessionmaker(autoflush=False, autocommit=False,bind=engine)
Base = declarative_base()

# Dependency Injection
def get_db()->Generator:
    try:
        db=Sessionlocal()
        yield db
    finally:
        db.close()