import tensorflow
from tensorflow import keras
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import os
import cv2
import numpy as np
from djitellopy import Tello
from drone_video import *
import csv

face_classifier = cv2.CascadeClassifier(r'/home/david/Projects/Drone/drone_controls/haarcascade_frontalface_default.xml')
classifier =load_model(r'/home/david/Projects/Drone/drone_controls/model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

tello = Tello()

def main():
    print("To start the video feed from the drone press 1.")

    number = input()

    if number == "1": 
        print("Connecting to the drone!")
        connect_to_drone(tello)
        print("Turning stream feed on!")
        turn_streamon(tello)
        print("Starting emotion recognition!")
        start_emotion_cv2()

def start_emotion_cv2():
    while True: 
        frame = tello.get_frame_read().frame
        labels = []
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

                prediction = classifier.predict(roi)[0]
                label=emotion_labels[prediction.argmax()]
                label_position = (x,y)
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                append_to_csv('/home/david/Projects/Drone/drone_controls/output.csv', label)
            else:
                cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Emotion Detector',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    turn_streamoff(tello)
    cv2.destroyAllWindows()

def append_to_csv(filename, input_string):
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow([input_string])

        print(f"'{input_string}' successfully added to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")





if __name__ == "__main__":
    main()