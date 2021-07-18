from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class ReviewSchema(BaseModel):
    review_id: str = Field(...)
    user: str = Field(...)
    text: int = Field(...)
    rating: float = Field(..., ge=0, le=5)
    sentiment: str = Field(...)
    date: str = Field(...)
    business: str = Field(...)

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}