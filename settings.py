
from os import getenv
from dotenv import load_dotenv

load_dotenv()

NOSQL_DATABASE_URL = getenv("NOSQL_DATABASE_URL")
SQLALCHEMY_DATABASE_URL = getenv("SQLALCHEMY_DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

