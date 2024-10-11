class EmotionReactions:
    def __init__(self, drone):
        self.drone = drone

    def react_to_emotion(self, emotion):
        if emotion == 'Happy':
            #self.drone.tello_flip('b')
            print("Happy, flip back")
        elif emotion == 'Sad':
            #self.drone.tello_backwards(50)
            print("Sad, move back")
        elif emotion == 'Angry':
            #self.drone.tello_rotate_clockwise(180)
            print("Angry, rotate 180")
        elif emotion == 'Neutral':
            #self.drone.tello_up(20)
            #self.drone.tello_down(20)
            print("Neutral, up down")

