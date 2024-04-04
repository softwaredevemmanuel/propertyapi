from typing import Optional, Union

from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    id: Optional[int]
    neighbourhood_id: Optional[int] = None
    profile_id: Optional[int]
    email: str
    phone: Optional[Union[int, str]]  # Allow both int and str for phone number
    created_at: Optional[datetime] = None
    login_blocked: bool = False  
    status: Optional[str] = None  
    enabled: Optional[bool] = False  
    is_verified: Optional[bool] = False  

    class Config:
        from_attributes=True
        orm_mode=True