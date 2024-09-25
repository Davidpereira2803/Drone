import cv2
import mediapipe as mp

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Track only one hand for simplicity
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

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

            # Print finger tip coordinates (optional)
            print(f"Index Finger Tip coordinates: {cx}, {cy}")

    # Display the image with tracking
    cv2.imshow("Finger Tracking", img)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
