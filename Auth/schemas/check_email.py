from pydantic import BaseModel

class EmailCheckRequest(BaseModel):
    email: str