import cv2

class LaptopCameraHandler:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise Exception("Error: Could not open camera.")

    def capture_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            raise Exception("Failed to grab frame")

        return frame

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()
