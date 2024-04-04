from pydantic import BaseModel
from datetime import date, datetime

class OpportunitySchema(BaseModel):

    property_id:str
    listing_type: str
    base_price: int
    quantity: int
    measurement_code: str
    currency_code: str
    allocatable: bool
    status: str