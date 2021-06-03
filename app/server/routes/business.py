from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_business,
    retrieve_business,
    retrieve_businesses,
    update_business,
)
from server.models.business import (
    ErrorResponseModel,
    ResponseModel,
    BusinessSchema,
    UpdateBusinessModel,
)

router = APIRouter()

@router.post("/", response_description="Business data added into the database")
async def add_business_data(business: BusinessSchema = Body(...)):
    business = jsonable_encoder(business)
    new_business = await add_business(business)
    return ResponseModel(new_business, "Business added successfully.")

@router.get("/", response_description="Businesses retrieved")
async def get_businesses():
    businesses = await retrieve_businesses()
    if businesses:
        return ResponseModel(businesses, "Businesses data retrieved successfully")
    return ResponseModel(businesses, "Empty list returned")


@router.get("/{id}", response_description="Business data retrieved")
async def get_business_data(id):
    business = await retrieve_business(id)
    if business:
        return ResponseModel(business, "Business data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Business doesn't exist.")