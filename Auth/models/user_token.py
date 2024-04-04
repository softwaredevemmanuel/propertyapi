from sqlalchemy import Column,String, Integer
from App.database.config import Base
from datetime import datetime

class UserToken(Base):
    __tablename__ = 'user_tokens'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    token = Column(String)