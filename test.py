import cv2

# Open Tello's video stream directly via OpenCV
cap = cv2.VideoCapture('udp://0.0.0.0:11111')

if not cap.isOpened():
    print("Failed to open video stream from Tello")
else:
    print("Video stream opened successfully")

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Display the frame
            cv2.imshow('Tello Stream', frame)
        else:
            print("Failed to receive frame")

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
