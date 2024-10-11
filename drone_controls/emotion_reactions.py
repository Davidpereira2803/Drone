class EmotionReactions:
    def __init__(self, drone):
        self.drone = drone

    def react_to_emotion(self, emotion):
        if emotion == 'happy':
            self.drone.flip_left()
        elif emotion == 'sad':
            self.drone.move_back(50)
        # Add more reactions for other emotions
