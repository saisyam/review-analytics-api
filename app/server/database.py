import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.analytics
business_collection = database.get_collection("business")

def business_helper(business) -> dict:
    return {
        "id": str(business["_id"]),
        "name": business["name"],
        "address": business["address"],
        "reviews": business["reviews"],
        "rating": business["rating"],
        "key": business["key"],
        "image": business["image"],
    }

# Retrieve all businesses present in the database
async def retrieve_businesses():
    businesses = []
    async for business in business_collection.find():
        businesses.append(business_helper(business))
    return businesses

# Add a new business into to the database
async def add_business(business_data: dict) -> dict:
    business = await business_collection.insert_one(business_data)
    new_business = await business_collection.find_one({"_id": business.inserted_id})
    return business_helper(new_business)


# Retrieve a business with a matching ID
async def retrieve_business(id: str) -> dict:
    business = await business_collection.find_one({"_id": ObjectId(id)})
    if business:
        return business_helper(business)


# Update a business with a matching ID
async def update_business(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    business = await business_collection.find_one({"_id": ObjectId(id)})
    if business:
        updated_business = await business_collection.update_one (
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_business:
            return True
        return False
