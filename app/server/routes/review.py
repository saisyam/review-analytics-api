from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_reviews,
)
from server.models.review import (
    ErrorResponseModel,
    ResponseModel,
    ReviewSchema,
)

router = APIRouter()


@router.get("/", response_description="Reviews retrieved")
async def get_reviews():
    reviews = await retrieve_reviews()
    if reviews:
        return ResponseModel(reviews, "reviews data retrieved successfully")
    return ResponseModel(reviews, "Empty list returned")