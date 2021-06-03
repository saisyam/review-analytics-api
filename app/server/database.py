import motor.motor_asyncio

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