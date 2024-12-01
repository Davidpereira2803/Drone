from drone_controls.drone_controller import DroneController
from drone_controls.camera_handler import CameraHandler
from emotion_detection.emotion_detection import EmotionRecognition
from drone_controls.emotion_reactions import EmotionReactions

def main():
    # Initialize drone and camera
    drone = DroneController()
    camera = CameraHandler(drone.tello)
    emotion_detector = EmotionRecognition()
    reactions = EmotionReactions(drone)

    # Start drone flight
    drone.tello_takeoff()
    camera.start_stream()

    while True:
        # Capture frame and detect emotion
        frame = camera.capture_frame()
        emotion = emotion_detector.detect_emotion(frame)

        # React to detected emotion
        reactions.react_to_emotion(emotion)

        # Optional: Add a quit condition
        if 0xFF == ord('q'):
            break

    drone.tello_land()

if __name__ == '__main__':
    main()
