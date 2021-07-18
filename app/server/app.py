from fastapi import FastAPI
from server.routes.review import router as ReviewRouter

app = FastAPI()
app.include_router(ReviewRouter, tags=["Review"], prefix="/reviews")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
