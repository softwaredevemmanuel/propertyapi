import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

#Depends on which database we're using
DATABASE_URL ='postgresql://property_pbvt_user:g1taPbD0ileDWhectfBvNcWd5OV0wYFR@dpg-co789j7109ks73840p1g-a.oregon-postgres.render.com/property_pbvt'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()