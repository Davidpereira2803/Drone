from drone_controls.drone_controller import DroneController
from drone_controls.camera_handler import CameraHandler
import cv2

def main():
    # Initialize drone and camera
    drone = DroneController()
    camera = CameraHandler(drone.tello)

    # Start drone flight
    #drone.tello_takeoff()

    camera.start_stream()

    #drone.tello_land()

    while True:
        frame = camera.capture_frame()
        
        cv2.imshow("Tello Video Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.streamoff()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
