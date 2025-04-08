from ultralytics import YOLO
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Load the models
#model_best = YOLO("weights/best.pt")  # Replace with the path to your best.pt file
model_last = YOLO("weights/last.pt")  # Replace with the path to your last.pt file

# Function to test the model on the uploaded image
def test_model_on_image(model, image_source, output_path):
    print(f"\nTesting model: {model}")  # Print model details

    # Read the image
    image = cv2.imread(image_source)
    if image is None:
        print("Error: Could not read image.")
        messagebox.showerror("Error", "Could not read the image file.")
        return

    # Run predictions on the image
    results = model.predict(source=image_source, save=True, save_txt=True, save_dir=output_path)

    # Process and display the results
    annotated_image = results[0].plot()  # Annotate the image with detections

    # Convert OpenCV image to PIL format for Tkinter
    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    annotated_image = Image.fromarray(annotated_image)
    annotated_image = ImageTk.PhotoImage(annotated_image)

    # Display the annotated image in the GUI
    result_label.config(image=annotated_image)
    result_label.image = annotated_image
    messagebox.showinfo("Success", "Detection completed!")

# Function to handle file selection and run detection
def upload_and_detect(model):
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp"), ("All Files", "*.*")]
    )
    if file_path:
        output_path = os.path.join(os.getcwd(), "runs/test_image")
        test_model_on_image(model, file_path, output_path)

# Initialize the GUI
root = tk.Tk()
root.title("Medical Instrument Detection Through Image")
root.geometry("1500x900")
image2 = Image.open('med.webp')
image2 = image2.resize((1500, 900), Image.LANCZOS )
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Title label
title_label = tk.Label(root, text="Medical Instrument Detection Through Image", font=("Arial", 24, "bold"),bg="powder blue")
title_label.pack(pady=10)

# Buttons for selecting models
# button_best = tk.Button(root, text="Run Detection with Best Model", font=("Arial", 14), bg="green", fg="white",
#                         command=lambda: upload_and_detect(model_best))
# button_best.pack(pady=10)

button_last = tk.Button(root, text="Upload Image For Detection", font=("Arial", 14), bg="blue", fg="white",
                        command=lambda: upload_and_detect(model_last))
button_last.pack(pady=60)

# Label to display results
result_label = tk.Label(root)
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
