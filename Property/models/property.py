from sqlalchemy import Column,BigInteger,String,Boolean,ForeignKey, Integer, DateTime, UUID
from datetime import datetime
import uuid
from App.database.config import Base
from sqlalchemy.orm import relationship


class Property(Base):
    __tablename__ = "property"
    id = Column(UUID, primary_key=True, default=lambda: uuid.uuid4())
    slug = Column(String, nullable=True, default="None")  # Default value will be set in __init__ method
    label = Column(String, nullable=False)
    overview = Column(String, nullable=True)
    #neighborhood_id = Column(Integer, ForeignKey('neighborhood.id'), nullable=False)
    #category_id = Column(Integer, ForeignKey('category.id'), nullable=False)    
    available_quantity = Column(Integer, nullable=False)
    total_quantity = Column(Integer, nullable=False)
    measurement_code = Column(String, nullable=False)
    status = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=None)
    opportunity = relationship("OpportunityModel", back_populates="property") 

    def __init__(self, label, **kwargs):
        super(Property, self).__init__(**kwargs)
        self.label = label
        self.slug = label

