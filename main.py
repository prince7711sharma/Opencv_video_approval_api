from fastapi import FastAPI
from app.api.routes.moderation import router as moderation_router

app = FastAPI(title="Agri Video Moderation API")

app.include_router(moderation_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Agri moderation API running"}
