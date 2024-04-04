from sqlalchemy import Column,String, Integer, DateTime, Text
from App.database.config import Base
from datetime import datetime


class LoginHistory(Base):
    __tablename__ = 'login_history'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    time_in = Column(DateTime, default=datetime.utcnow)
    time_out = Column(DateTime)
    ip_address = Column(String)
    access_client = Column(Text)
    longitude = Column(String)
    latitude = Column(String)