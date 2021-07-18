import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.review_db
review_collection = database.get_collection("reviews")

def review_helper(review) -> dict:
    return {
        "id": str(review["review_id"]),
        "name": review["business"],
        "user": review["user"],
        "text": review["text"],
        "rating": review["rating"],
        "sentiment": review["sentiment"],
        "date": review["date"],
    }

# Retrieve all businesses present in the database
async def retrieve_reviews():
    reviews = []
    async for review in review_collection.find():
        reviews.append(review_helper(review))
    return reviews
