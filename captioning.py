# captioning.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from io import BytesIO

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)
model.eval()

def generate_caption(image_bytes: bytes) -> str:
    """Generate caption from image bytes using BLIP model."""
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=40)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption.strip()
