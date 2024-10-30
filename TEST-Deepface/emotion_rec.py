import cv2
from deepface import DeepFace

# Initialize the webcam feed
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define emotion colors for display
emotion_colors = {
    'happy': (0, 255, 0),
    'sad': (255, 0, 0),
    'neutral': (255, 255, 255),
    'angry': (0, 0, 255),
    'surprise': (0, 255, 255),
    'fear': (128, 0, 128),
    'disgust': (0, 128, 0)
}

print("Press 'q' to exit the program.")

# Loop through each frame from the webcam
frame_count = 0  # Initialize a frame counter

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    
    # Process every 5th frame for emotion detection
    if frame_count % 5 == 0:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        small_frame = cv2.resize(rgb_frame, (0, 0), fx=0.5, fy=0.5)
        
        try:
            predictions = DeepFace.analyze(small_frame, actions=['emotion'], enforce_detection=False)
            if isinstance(predictions, list):
                predictions = predictions[0]
            emotion = predictions['dominant_emotion']
            color = emotion_colors.get(emotion, (255, 255, 255))
            cv2.putText(frame, f"Emotion: {emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        except Exception as e:
            print("Error in emotion detection:", e)

    # Display the frame (regardless of processing it for emotion detection)
    cv2.imshow("Emotion Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
