from sqlalchemy import Column,String, Integer, DateTime
from App.database.config import Base
from datetime import datetime


class ResetPassword(Base):
    __tablename__ = 'reset_password'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    code = Column(Integer)
    token = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    verified_at = Column(DateTime, default=None)