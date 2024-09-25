import cv2
import mediapipe as mp
from djitellopy import Tello
import time

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Track only one hand for simplicity
mp_draw = mp.solutions.drawing_utils

# Initialize Tello drone
tello = Tello()
tello.connect()
print(f"Tello Battery: {tello.get_battery()}%")

# Start video stream from the Tello drone
tello.streamon()

# Define movement thresholds
THRESHOLD_X = 100  # Horizontal movement threshold
THRESHOLD_Y = 100  # Vertical movement threshold

# Initialize drone's state (takeoff or not)
tello.takeoff()
time.sleep(2)  # Give it time to stabilize

while True:
    # Read frame from the Tello's camera
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (640, 480))  # Resize for easier processing

    # Convert the image to RGB as Mediapipe requires RGB images
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks
    result = hands.process(img_rgb)

    # If landmarks are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks on the image
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions for the index finger (landmark 8)
            index_finger_tip = hand_landmarks.landmark[8]

            # Convert normalized coordinates to pixel coordinates
            h, w, c = img.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Draw a circle at the index finger tip
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

            # Control the Tello drone based on finger position
            # Move left or right
            if cx < w // 2 - THRESHOLD_X:
                #tello.move_left(20)
                pass
            elif cx > w // 2 + THRESHOLD_X:
                #tello.move_right(20)
                pass

            # Move up or down
            if cy < h // 2 - THRESHOLD_Y:
                tello.move_up(20)
                #pass
            elif cy > h // 2 + THRESHOLD_Y:
                tello.move_down(20)
                #pass

            # Move forward or backward
            if abs(cx - w // 2) < THRESHOLD_X and abs(cy - h // 2) < THRESHOLD_Y:
                #tello.move_forward(20)
                pass

    # Display the image with tracking
    cv2.imshow("Tello Finger Tracking", img)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Land the drone and release resources
tello.land()
cv2.destroyAllWindows()
