from pydantic import BaseModel
from typing import Optional, Generic, TypeVar, Union

class ListingTypeSchema(BaseModel):
    tag: str
    label: str
    overview: str
    enabled: bool = True


class ListingTypeUpdate(BaseModel):
    tag: Optional[str]
    label: Optional[str]
    overview: Optional[str]

