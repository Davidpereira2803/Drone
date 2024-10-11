import cv2
from deepface import DeepFace  # Emotion detection library

class EmotionRecognition:
    def __init__(self):
        pass

    def detect_emotion(self, frame):
        emotions = DeepFace.analyze(frame, actions=['emotion'])
        return emotions['dominant_emotion']
