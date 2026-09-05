from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_connection = os.getenv("DB_CONNECTION")

engine = create_engine(db_connection)

SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)
