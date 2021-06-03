from pydantic import BaseModel
from typing import Optional

class Business(BaseModel):
    name: str
    address: str
    reviews: int
    rating: float
    key: str
    image: str