from sqlalchemy import Column,BigInteger,String,Boolean,ForeignKey, Integer, Float, UUID, DateTime
import uuid
from sqlalchemy.orm import relationship
from App.database.config import Base
import uuid
from datetime import datetime


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    phone = Column(BigInteger)
    reference = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    other_name = Column(String)
    gender = Column(String)
    birthday = Column(String)
    organization_id = Column(Integer)
    email = Column(String)
    display_image = Column(String)
    bio = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    # user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="profile") 

