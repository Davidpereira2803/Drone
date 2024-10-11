import cv2
from djitellopy import Tello

class CameraHandler:
    def __init__(self, tello):
        self.tello = tello

    def start_stream(self):
        self.tello.streamon()

    def stop_stream(self):
        self.tello.streamoff()

    def capture_frame(self):
        frame_read = self.tello.get_frame_read()
        frame = frame_read.frame
        return frame
