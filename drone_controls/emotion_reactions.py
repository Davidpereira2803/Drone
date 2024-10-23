class EmotionReactions:
    def __init__(self, drone_controller):
        self.drone = drone_controller

    def react_to_emotion(self, emotion):
        if emotion == 'Happy':
            self.drone.tello_flip('b')
            print("Happy, flip back")
            return True
        elif emotion == 'Sad':
            #self.drone.tello_backwards(50)
            print("Sad, move back")
        elif emotion == 'Angry':
            #self.drone.tello_rotate_clockwise(180)
            print("Angry, rotate 180")
        elif emotion == 'Neutral':
            print("Neutral, up down")

