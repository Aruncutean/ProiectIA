import torch
from matplotlib import pyplot as plt
from PIL import Image

# Path to your custom trained weights file (e.g., 'best.pt')
weights_path = 'C:\\Users\\Aruncutean\\Desktop\\Proiect AI\\best.pt'
# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, source='local')

# Load an image
img_path = 'C:\\Users\\Aruncutean\\Desktop\\Proiect AI\\images\\c1.jpg'  # replace with your image path
img = Image.open(img_path)

# Inference
results = model(img)

# Results
results.print()  # Print results to console
results.show()  # Show the image with bounding boxes

# To save the image with detections
results.save('path_where_to_save')  # provide the path where to save

# Alternatively, if you want to process the results:
for img in results.imgs:  # for each image
    plt.imshow(img)  # plot
    plt.show()