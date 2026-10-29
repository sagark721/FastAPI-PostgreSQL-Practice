import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()


db_user = os.getenv("DB_USER")
raw_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
encoded_password = quote_plus(raw_password)

db_url=f"postgresql+psycopg2://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}"
engine= create_engine(db_url)
session= sessionmaker(autoflush=False, bind=engine, autocommit=False)