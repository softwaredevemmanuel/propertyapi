from pydantic import BaseModel
from datetime import date, datetime
import uuid

class InvestmentPlanSchema(BaseModel):

    opportunity_id:str
    tenure_months: int
    interest_rate: float
    principal: int
