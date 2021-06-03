from fastapi import FastAPI
from server.routes.business import router as BusinessRouter

app = FastAPI()
app.include_router(BusinessRouter, tags=["Business"], prefix="/business")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
