import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/crud_app"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

