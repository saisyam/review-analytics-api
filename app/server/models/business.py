from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class BusinessSchema(BaseModel):
    name: str = Field(...)
    address: str = Field(...)
    reviews: int = Field(...)
    rating: float = Field(..., ge=0, le=5)
    key: str = Field(...)
    image: str = Field(...)

class UpdateBusinessModel(BaseModel):
    name: Optional[str]
    address: Optional[str]
    reviews: Optional[int]
    rating: Optional[float]
    key: Optional[str]
    image: Optional[str]

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}