from sqlalchemy import Column,String, Integer, DateTime
import uuid
from sqlalchemy.orm import relationship
from App.database.config import Base
import uuid
from datetime import datetime




class VerificationToken(Base):
    __tablename__ = 'verification_token'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    code = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


