from pydantic import BaseModel
from datetime import date, datetime
import uuid

class SubscriptionSchema(BaseModel):

    referral_code:str
    opportunity_id:str
    capital: int
    tenure_months: int
    interest_rate: int
    expected_roi: int
    currency_code: str
    # activated_at: date
    # matures_at: date
    remarks: str
    status: str
    enabled: bool
    creator_user_id: int

class UpdateSubscriptionSchema(BaseModel):

    referral_code:str
    capital: int
    tenure_months: int
    interest_rate: int
    expected_roi: int
    currency_code: str
    # activated_at: date
    # matures_at: date
    remarks: str
    status: str
    enabled: bool
    creator_user_id: int


