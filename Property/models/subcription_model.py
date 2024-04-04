from sqlalchemy import Column,BigInteger,String,Boolean,ForeignKey, Integer, Date, DateTime, UUID
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship

from App.database.config import Base

class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(UUID, primary_key=True, default=lambda: uuid.uuid4())
    referral_code = Column(String, nullable=True, default="Admin")

    #profile_id = Column(BigInteger, ForeignKey("profile.id"), nullable=False)
    opportunity_id = Column(UUID, ForeignKey("opportunity.id"), nullable=False)
    opportunity = relationship("OpportunityModel", back_populates="subscription")

    capital = Column(Integer, nullable=False)
    tenure_months = Column(Integer, nullable=False)
    interest_rate = Column(Integer, nullable=False)
    expected_roi = Column(Integer, nullable=False)
    currency_code = Column(String, nullable=False, default='NGN')
    activated_at = Column(Date, nullable=True)
    matures_at = Column(Date, nullable=True)
    remarks = Column(String, nullable=True)
    status = Column(String, nullable=False)
    enabled = Column(Boolean,default=True)
    creator_user_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=None)


