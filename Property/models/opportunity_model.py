from sqlalchemy import Column,Integer,String,Boolean,Date,DateTime,Text, BigInteger, ForeignKey, UUID
import uuid
from datetime import datetime
from App.database.config import Base
from sqlalchemy.orm import relationship

class OpportunityModel(Base):
    __tablename__ = "opportunity"
    
    id = Column(UUID, primary_key=True, default=lambda: uuid.uuid4())
    property_id = Column(UUID, ForeignKey("property.id"), nullable=False)
    property = relationship("Property", back_populates="opportunity") 
    listing_type = Column(String, nullable=False)
    base_price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    measurement_code = Column(String, nullable=True)
    currency_code = Column(String(length=10), nullable=False)
    allocatable = Column(Boolean, nullable=False)
    status = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    investment_plan = relationship("InvestmentPlan", back_populates="opportunity")
    subscription = relationship("Subscription", back_populates="opportunity")
