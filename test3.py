import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import cv2

# Your YOLO import and model loading here
from ultralytics import YOLO
model = YOLO("C:\\Users\\Aruncutean\\Desktop\\Proiect AI\\best.pt")

# Initialize Tkinter window
root = tk.Tk()
root.title("YOLO Image Viewer")

# Function to update the image on the canvas
def update_image(path):
    img = Image.open(path)
    results = model.predict(source=path)

    # Draw bounding boxes and labels on the image
    draw = ImageDraw.Draw(img)
    for det in results.xywhn:  # Assuming results.xywhn contains normalized bbox coords
        # Convert normalized coords to pixel values (assuming results are normalized)
        x, y, w, h = det[:4]
        x *= img.width
        y *= img.height
        w *= img.width
        h *= img.height
        left, top, right, bottom = x - w / 2, y - h / 2, x + w / 2, y + h / 2
        draw.rectangle([left, top, right, bottom], outline="red", width=2)

    img = img.resize((500, 500))  # Resize the image to fit the canvas
    img = ImageTk.PhotoImage(img)

    # Update canvas
    canvas.image = img
    canvas.create_image(0, 0, anchor='nw', image=img)

# Function to handle "Next" button
def load_next_image():
    path = filedialog.askopenfilename()  # Open file dialog to select image
    if path:
        update_image(path)

# Canvas for image display
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Button to load next image
btn_next = tk.Button(root, text="Next Image", command=load_next_image)
btn_next.pack(side="bottom")

root.mainloop()