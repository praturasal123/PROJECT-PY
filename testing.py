from ultralytics import YOLO
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import os

root = tk.Tk()
root.state('zoomed')
root.title("medical instrument detection")

current_path = str(os.path.dirname(os.path.realpath('__file__')))
basepath = current_path + "/"

# ==============================================================================
# Background Image Setup
image2 = Image.open('med.webp')
image2 = image2.resize((1530, 900), Image.LANCZOS )
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Title Label
label_l1 = tk.Label(root, text="Medical Instument Detection", font=("Times New Roman", 35, 'bold'),
                    background="powder blue", fg="black", width=30, height=1)
label_l1.place(x=340, y=20)

def pathole():
    # Load the YOLO model
    model_best = YOLO("weights/best.pt")  # Update the path to your 'best.pt'

    # Test function for a single model on a video with key control
    def test_model_on_video(model, video_source, output_path):
        print(f"\nTesting model: {model}")  # Print model details

        # Run predictions on video
        results = model.predict(source=video_source, save=True, save_txt=True, save_dir=output_path, stream=True)

        # Open the video source
        cap = cv2.VideoCapture(video_source)
        if not cap.isOpened():
            print("Error: Could not open video.")
            return

        for result in results:  # Process each frame
            frame = result.plot()  # Plot the detections on the frame
            cv2.imshow("YOLO Detection", frame)

            # Wait for a key press (e.g., 'q' to quit)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):  # Press 'q' to quit
                print("Exiting video playback...")
                break

        # Release the video capture and close the display window
        cap.release()
        cv2.destroyAllWindows()

    # Prompt user to select a video file
    video_path = askopenfilename(
        title="Select Video File",
        filetypes=(("MP4 files", "*.mp4"), ("All files", "*C:/Users/COMPUTER/Downloads/road potholes and cracks.v1i.yolov8/YOLOv8_outputs/YOLOv8_training*"))
    )

    if not video_path:
        print("No video selected.")
        return

    # Define output path for results
    output_best = "runs/test_best_video"  # Directory for 'best.pt' results

    # Test the 'best.pt' model on the selected video
    print("Running detection with best.pt...")
    test_model_on_video(model_best, video_path, output_best)

# Button to Trigger Pathole Functionality
btn_pathole = tk.Button(root, text="Run YOLO on Video", command=pathole, font=("Times New Roman", 20, 'bold'),
                        background="green", fg="white", width=20, height=2)
btn_pathole.place(x=600, y=200)

# Main GUI Loop
root.mainloop()
