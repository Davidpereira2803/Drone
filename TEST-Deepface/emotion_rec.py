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
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to RGB (DeepFace expects RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect emotions
    try:
        # Use DeepFace to analyze the frame for emotions
        predictions = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
        
        # Check if predictions is a list (multiple faces detected)
        if isinstance(predictions, list):
            predictions = predictions[0]  # Take the first result
        
        # Extract the dominant emotion
        emotion = predictions['dominant_emotion']
        
        # Get color for the detected emotion
        color = emotion_colors.get(emotion, (255, 255, 255))  # Default to white if emotion not in dictionary
        
        # Display the emotion on the frame
        cv2.putText(frame, f"Emotion: {emotion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    except Exception as e:
        print("Error in emotion detection:", e)
    
    # Display the frame
    cv2.imshow("Emotion Detection", frame)
    
    # Press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
