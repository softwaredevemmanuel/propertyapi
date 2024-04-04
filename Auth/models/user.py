from sqlalchemy import Column,String, Integer, DateTime, ForeignKey, BigInteger, Boolean, UUID
import uuid
from sqlalchemy.orm import relationship
from App.database.config import Base
import uuid
from datetime import datetime

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    neighborhood_id = Column(Integer)
    profile_id = Column(Integer, ForeignKey('profile.id'))
    profile = relationship("Profile", back_populates="user")
    email = Column(String)
    password = Column(String)
    phone = Column(BigInteger)
    created_at = Column(DateTime, default=datetime.utcnow)
    login_blocked = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    status = Column(String, default="pending")
    enabled = Column(Boolean, default=False)  
    is_verified = Column(Boolean, default=False) 
    verified_at = Column(DateTime, default = None)