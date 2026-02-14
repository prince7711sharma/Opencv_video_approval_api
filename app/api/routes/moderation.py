from fastapi import APIRouter, UploadFile, File
import shutil
import os
import uuid

from app.services.video_filter import moderate_video

router = APIRouter()

TEMP_DIR = "temp_videos"
os.makedirs(TEMP_DIR, exist_ok=True)


@router.post("/moderate-video")
async def moderate_video_api(file: UploadFile = File(...)):
    # create unique filename
    file_id = str(uuid.uuid4())
    file_ext = file.filename.split(".")[-1]
    path = os.path.join(TEMP_DIR, f"{file_id}.{file_ext}")

    # save uploaded file
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # run moderation
    approved = moderate_video(path)

    # delete temp file
    if os.path.exists(path):
        os.remove(path)

    return {
        "status": "APPROVED" if approved else "REJECTED"
    }
