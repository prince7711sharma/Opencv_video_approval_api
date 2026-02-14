from app.ml.clip_model import classify_frame
import numpy as np

dummy = np.zeros((224, 224, 3), dtype=np.uint8)

print(classify_frame(dummy))
