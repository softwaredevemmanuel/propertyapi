from sqlalchemy import Column,BigInteger,String,Boolean,ForeignKey, Integer, Float, UUID
import uuid
from sqlalchemy.orm import relationship
from App.database.config import Base
import uuid

class InvestmentPlan(Base):
    __tablename__ = "investment_plan"
    id = Column(UUID, primary_key=True, default=lambda: uuid.uuid4())
    opportunity_id = Column(UUID, ForeignKey("opportunity.id"), nullable=False)
    opportunity = relationship("OpportunityModel", back_populates="investment_plan") 
    tenure_months = Column(Integer, nullable=False)
    interest_rate = Column(Float, nullable=False)
    principal = Column(Integer, nullable=True)
    enabled = Column(Boolean,default=True)