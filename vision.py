from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import cv2

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def capture_and_describe():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "Webcam not found"

    ret, frame = cap.read()
    cap.release()
    if not ret:
        return "Failed to capture image"

    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

    with open("log.txt", "a") as f:
        f.write(caption + "\n")

    return caption
