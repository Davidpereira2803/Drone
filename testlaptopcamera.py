import cv2
from drone_controls.laptop_camera_handler import LaptopCameraHandler
from drone_controls.camera_handler import CameraHandler
from drone_controls.drone_controller import DroneController


laptopcamera = LaptopCameraHandler()

print("1 to laptop camera 2 to drone camera")
number = input()
if number == "1":
    print("laptop")

    while True:
        frame = laptopcamera.capture_frame()

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    laptopcamera.release_camera()

elif number == "2":
    drone = DroneController()
    dronecamera = CameraHandler(drone.tello)
    print("drone")
    dronecamera.start_stream()

    while True:
        frame = dronecamera.capture_frame()
        cv2.imshow('Camera Feed', frame)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    dronecamera.stop_stream()
    cv2.destroyAllWindows()



