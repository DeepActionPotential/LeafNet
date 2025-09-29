import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# Load class names
class_names = [
    "Anthracnose", "algal leaf", "bird eye spot",
    "brown blight", "gray light", "healthy",
    "red leaf spot", "white spot"
]

# Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model (assumes you used torch.save(model, "model.pth"))
model = torch.load("models/tea_leaves_model.pth", map_location=device, weights_only=False)
model.eval()

# Image preprocessing
transform  = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict_image(image: Image.Image) -> str:
    """
    Run inference on a single PIL image and return class label.
    """
    img_t = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(img_t)
        _, preds = torch.max(outputs, 1)
        pred_class = class_names[preds.item()]

    return pred_class
