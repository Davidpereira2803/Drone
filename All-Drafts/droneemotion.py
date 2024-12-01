from djitellopy import Tello
import cv2
from fer import FER
import time
import numpy as np

class EmotionalDrone:
    def __init__(self):
        # Initialize Tello drone
        self.tello = Tello()
        self.tello.connect()
        
        # Check battery level
        print(f"Battery Level: {self.tello.get_battery()}%")
        
        # Initialize facial emotion detector
        self.emotion_detector = FER(mtcnn=True)
        
        # Define emotion-based movements
        self.emotion_actions = {
            'happy': self.happy_dance,
            'sad': self.sympathetic_movement,
            'angry': self.cautious_backup,
            'neutral': self.stable_hover,
            'surprised': self.surprised_jump
        }
    
    def start_mission(self):
        """Start the drone and begin emotion detection loop"""
        try:
            # Take off
            self.tello.takeoff()
            self.tello.streamon()
            
            while True:
                # Get frame from drone
                frame = self.tello.get_frame_read().frame
                if frame is None:
                    continue
                
                # Detect emotions in frame
                emotions = self.emotion_detector.detect_emotions(frame)
                
                if emotions:
                    # Get dominant emotion
                    dominant_emotion = max(emotions[0]['emotions'].items(), 
                                        key=lambda x: x[1])[0]
                    print(f"Detected emotion: {dominant_emotion}")
                    
                    # Execute corresponding movement
                    if dominant_emotion in self.emotion_actions:
                        self.emotion_actions[dominant_emotion]()
                
                # Display frame with emotion detection
                cv2.imshow("Drone View", frame)
                
                # Break loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
        finally:
            # Clean landing and shutdown
            self.tello.land()
            self.tello.streamoff()
            cv2.destroyAllWindows()
    
    def happy_dance(self):
        """Perform a happy dance pattern"""
        try:
            self.tello.rotate_clockwise(360)  # Spin around
            self.tello.move_up(30)
            self.tello.move_down(30)
        except:
            self.stable_hover()
    
    def sympathetic_movement(self):
        """Gentle, sympathetic movement pattern"""
        try:
            self.tello.move_forward(30)
            self.tello.move_back(30)
            time.sleep(1)
        except:
            self.stable_hover()
    
    def cautious_backup(self):
        """Move back slowly when anger is detected"""
        try:
            self.tello.move_back(50)
            time.sleep(2)
        except:
            self.stable_hover()
    
    def stable_hover(self):
        """Maintain stable hover"""
        try:
            self.tello.send_rc_control(0, 0, 0, 0)
            time.sleep(1)
        except:
            pass
    
    def surprised_jump(self):
        """Quick up and down movement"""
        try:
            self.tello.move_up(40)
            time.sleep(0.5)
            self.tello.move_down(40)
        except:
            self.stable_hover()

if __name__ == "__main__":
    # Create and start emotional drone
    drone = EmotionalDrone()
    drone.start_mission()