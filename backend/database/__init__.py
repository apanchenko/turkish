# backend/database/__init__.py
from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "postgresql://username:password@localhost/db_name"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
database = Database(DATABASE_URL)