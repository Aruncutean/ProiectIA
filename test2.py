from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("C:\\Users\\Aruncutean\\Desktop\\Proiect AI\\best.pt")

# from PIL
im1 = Image.open("C:\\Users\\Aruncutean\\Desktop\\Proiect AI\\images\\c2.jpg")
results = model.predict(source=im1, save=True)  # save plotted images

# from ndarray
im2 = cv2.imread("C:\\Users\\Aruncutean\\Desktop\\Proiect AI\\images\\c2.jpg")
results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels

# from list of PIL/ndarray
results = model.predict(source=[im1, im2])