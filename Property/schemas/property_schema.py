from pydantic import BaseModel
from datetime import datetime

class PropertySchema(BaseModel):
    label: str
    overview: str
    # neighborhood_id: int
    # category_id: int
    available_quantity: int
    total_quantity: int
    measurement_code: str
    status: str

