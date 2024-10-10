from djitellopy import Tello
import cv2

def connect_to_drone(drone):
    drone.connect()

def turn_streamon(drone):
    drone.streamon()
    
def turn_streamoff(drone):
    drone.streamoff()

