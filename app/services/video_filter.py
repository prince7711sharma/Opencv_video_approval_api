# from app.services.frame_extractor import extract_frames
# from app.ml.clip_model import classify_frame
#
#
# def moderate_video(video_path):
#     frames = extract_frames(video_path)
#
#     agri_score = 0
#
#     for frame in frames:
#         idx = classify_frame(frame)
#
#         if idx <= 4:
#             agri_score += 1
#
#     return agri_score >= 2

import cv2
import numpy as np
from app.services.frame_extractor import extract_frames


def is_farm_frame(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # green color range
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    green_ratio = np.sum(mask > 0) / (frame.shape[0] * frame.shape[1])

    print("Green ratio:", green_ratio)

    return green_ratio > 0.15


def moderate_video(video_path):
    frames = extract_frames(video_path)

    farm_frames = 0

    for frame in frames:
        if is_farm_frame(frame):
            farm_frames += 1

    print("Farm frames:", farm_frames)

    return farm_frames >= 1
