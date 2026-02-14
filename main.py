from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.moderation import router as moderation_router

app = FastAPI(title="Agri Video Moderation API")

# Enable CORS (important for UI + teammate usage)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(moderation_router, prefix="/api")


@app.get("/")
def home():
    return {"message": "Agri moderation API running"}


@app.get("/health")
def health():
    return {"status": "ok"}
