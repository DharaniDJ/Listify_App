from config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DB_URL = setting.DB_URL
engine = create_engine(SQLALCHEMY_DB_URL)
Sessionlocal = sessionmaker(autoflush=False, autocommit=False,bind=engine)
Base = declarative_base()
