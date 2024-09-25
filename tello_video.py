from djitellopy import Tello
import cv2

# Connect to the Tello drone
tello = Tello()

# Attempt to connect
tello.connect()

# Start video stream
tello.streamon()

# Loop to continuously get frames
while True:
    # Read the frame from the drone camera
    frame = tello.get_frame_read().frame
    
    # Resize for better viewing if necessary
    frame = cv2.resize(frame, (640, 480))
    
    # Display the frame in a window
    cv2.imshow("Tello Camera Feed", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close the connection
tello.streamoff()
tello.end()
cv2.destroyAllWindows()
