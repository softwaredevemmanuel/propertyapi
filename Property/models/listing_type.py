from sqlalchemy import Column,BigInteger,String,Boolean,ForeignKey

from App.database.config import Base

class ListingType(Base):
    __tablename__ = "listing_type"
    tag = Column(String, nullable=False,primary_key=True)
    label = Column(String, nullable=False)
    overview = Column(String,nullable=True)
    enabled = Column(Boolean,default=True)
