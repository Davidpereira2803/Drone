import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    if frame_count % 5 == 0:  # Process every 5th frame
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

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    if frame_count % 5 == 0:  # Process every 5th frame
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

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
