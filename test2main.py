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
from drone_controls.emotion_reactions import EmotionReactions
from collections import deque, Counter


face_classifier = cv2.CascadeClassifier(r'/home/david/Projects/Drone/emotion_detection/haarcascade_frontalface_default.xml')
classifier =load_model(r'/home/david/Projects/Drone/emotion_detection/model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

drone = DroneController()
camera = CameraHandler(drone.tello)
reactions = EmotionReactions(drone.tello)

last_30_strings = deque(maxlen=10)

most_common_label = None

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

    most_common_label = None

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

        # Every 5 seconds, update the deque and print the most common emotion
        if time.time() - last_emotion_time >= 3 and labels_in_frame:
            for label in labels_in_frame:
                update(label)
            most_common_label = get_most_frequent()
            print(f"Most common emotion in last 30 frames: {most_common_label}")
            reactions.react_to_emotion(most_common_label)
            # Reset the timer for the next check
            last_emotion_time = time.time()

        if most_common_label is not None:
            cv2.putText(frame, most_common_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255) , 1)
        else:
            cv2.putText(frame, "", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255) , 1)
        
        # Continuously show the video feed with detected emotions
        cv2.imshow('Emotion Detector', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.stop_stream()
    cv2.destroyAllWindows()

def update(new_string):
    last_30_strings.append(new_string)
    if len(last_30_strings) > 6: # after put greater tham 7 with 15 frames
        last_30_strings.popleft()

    print(last_30_strings)

def get_most_frequent():
    frequency = Counter(last_30_strings)

    if len(frequency) > 1:
        most_frequent_string, _ = frequency.most_common(1)[0]
        return most_frequent_string
    else:
        return None    

if __name__ == "__main__":
    main()