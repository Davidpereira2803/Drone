from djitellopy import Tello
import cv2

# Initialize the Tello drone
tello = Tello()

# Connect to the drone
tello.connect()

# Start video stream
tello.streamon()

# Infinite loop to continuously display the video feed
while True:
    # Get the frame from the drone's video feed
    frame = tello.get_frame_read().frame
    
    # Display the video feed
    cv2.imshow("Tello Video Feed", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
tello.streamoff()
cv2.destroyAllWindows()


'''

face_classifier = cv2.CascadeClassifier(r'/home/david/Projects/facialemotionrecognizerinrealtime/haarcascade_frontalface_default.xml')
classifier =load_model(r'/home/david/Projects/facialemotionrecognizerinrealtime/model.h5')

'''
