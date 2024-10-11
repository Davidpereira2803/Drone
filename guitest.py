import cv2
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Initialize the detected emotion as "Happy"
most_common_label = "Happy"

# Function to update the frame and text
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert the frame to PIL format for Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        
        # Update the label with the new frame
        video_label.imgtk = imgtk
        video_label.config(image=imgtk)
        
        # Update the text label with the detected emotion
        text_label.config(text=f"Detected Emotion: {most_common_label}")
    
    # Schedule the update again after 10ms
    root.after(10, update_frame)

# Function for button action to change the emotion
def on_button_click():
    global most_common_label
    # Change the emotion from "Happy" to "Sad" when the button is pressed
    if most_common_label == "Happy":
        most_common_label = "Sad"
    else:
        most_common_label = "Happy"
    # Update the text label immediately after the button press
    text_label.config(text=f"Detected Emotion: {most_common_label}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("OpenCV with Tkinter")

# Create a frame to hold the video feed on the left
video_frame = tk.Frame(root)
video_frame.pack(side="left", padx=10, pady=10)

# Create a frame to hold the text and other elements on the right
control_frame = tk.Frame(root)
control_frame.pack(side="right", padx=10, pady=10)

# Video label to display frames
video_label = Label(video_frame)
video_label.pack()

# Add a label to display output text on the right side
text_label = Label(control_frame, text="Detected Emotion: Happy", font=("Helvetica", 16))
text_label.pack(pady=10)

# Add a button below the text on the right side
button = Button(control_frame, text="Change Emotion", command=on_button_click)
button.pack(pady=10)

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Start updating the video feed and text
update_frame()

# Start the Tkinter main loop
root.mainloop()

# Release the capture object after closing
cap.release()
