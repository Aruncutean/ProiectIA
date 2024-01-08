import torch
from PIL import Image

# Path to your custom trained weights file (e.g., 'best.pt')
weights_path = 'C:\\Users\\Aruncutean\\Desktop\Proiect AI\\best.pt'

# Load your custom trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path)

# Load an image
img_path = 'C:\\Users\\Aruncutean\\Desktop\\Proiect AI\\images\c4.jpg'  # Replace with your image path
img = Image.open(img_path)

# Inference
results = model(img)

# Results
results.print()  # Print results to console
results.show()  # Show the image with bounding boxes
results.save('path_where_to_save')  # Save the image with detections