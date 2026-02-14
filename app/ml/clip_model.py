# import torch
# from transformers import CLIPProcessor, CLIPModel
# from PIL import Image
#
# device = "cuda" if torch.cuda.is_available() else "cpu"
#
# print("Loading CLIP model...")
#
# model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
# processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
#
# print("CLIP model loaded")
#
# labels = [
#     "farm field",
#     "tractor",
#     "crop plants",
#     "farmer working",
#     "livestock",
#     "gaming screen",
#     "city traffic",
#     "people dancing",
#     "movie scene"
# ]
#
#
# def classify_frame(frame):
#     image = Image.fromarray(frame)
#
#     inputs = processor(
#         text=labels,
#         images=image,
#         return_tensors="pt",
#         padding=True
#     ).to(device)
#
#     outputs = model(**inputs)
#     probs = outputs.logits_per_image.softmax(dim=1)
#
#     return probs.argmax().item()

import torch
from torchvision import models, transforms
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading MobileNet model...")

model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
model.eval().to(device)

print("MobileNet loaded")

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# agriculture-related ImageNet classes
AGRI_CLASSES = [
    "tractor",
    "ox",
    "cow",
    "harvester",
    "thresher"
]


def classify_frame(frame):
    image = Image.fromarray(frame)
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        predicted = outputs.argmax(1).item()

    return predicted
