import tensorflow
from tensorflow import keras
from keras.models import load_model
from time import sleep
import time
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import os
import cv2
import numpy as np
from djitellopy import Tello
import csv
from drone_controls.drone_controller import DroneController
from drone_controls.camera_handler import CameraHandler
from collections import deque, Counter


face_classifier = cv2.CascadeClassifier(r'/home/david/Projects/Drone/emotion_detection/haarcascade_frontalface_default.xml')
classifier =load_model(r'/home/david/Projects/Drone/emotion_detection/model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

drone = DroneController()
camera = CameraHandler(drone.tello)

last_30_strings = deque(maxlen=30)

def main():
    print("To start the video feed from the drone press 1.")

    number = input()

    if number == "1": 
        print("Connecting to the drone!")
        print("Turning stream feed on!")
        camera.start_stream()
        print("Starting emotion recognition!")
        start_emotion_cv2()

def start_emotion_cv2():
    last_emotion_time = time.time()

    while True:
        frame = camera.capture_frame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)
        
        labels_in_frame = []  # Track labels for the current frame

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # Add the label to the deque for long-term analysis
                labels_in_frame.append(label)

        # Continuously show the video feed with detected emotions
        cv2.imshow('Emotion Detector', frame)

        # Every 5 seconds, update the deque and print the most common emotion
        if time.time() - last_emotion_time >= 5 and labels_in_frame:
            for label in labels_in_frame:
                update_and_get_most_frequent(label)
            most_common_label = update_and_get_most_frequent(None)
            print(f"Most common emotion in last 30 frames: {most_common_label}")
            
            # Reset the timer for the next check
            last_emotion_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.stop_stream()
    cv2.destroyAllWindows()

def append_to_csv(filename, input_string, num1, num2):
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow([input_string, num1, num2])

        print(f"Row '{input_string}, {num1}, {num2}' successfully added to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def update_and_get_most_frequent(new_string):
    last_30_strings.append(new_string)
    
    frequency = Counter(last_30_strings)
    
    most_frequent_string, _ = frequency.most_common(1)[0]
    
    return most_frequent_string


if __name__ == "__main__":
    main()