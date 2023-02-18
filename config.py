import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

class Settings:
    TITLE="Title from config file"
    VERSION="0.0.1"
    DESCRIPTION="""
    THIS IS TEST DESCRIPTION
    THIS IS COMING FROM CONFIG FILE
    """
    NAME="Dharani Chinta"
    EMAIL="dharani56525@gmail.com"
    POSTGRES_USER=os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER=os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT=os.getenv("POSTGRES_PORT")
    POSTGRES_DB=os.getenv("POSTGRES_DB")
    DB_URL=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


setting = Settings()
