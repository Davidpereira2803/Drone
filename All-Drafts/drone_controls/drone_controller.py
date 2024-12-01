from djitellopy import Tello

class DroneController:
    def __init__(self):
        self.tello = Tello()
        self.tello.connect()

    def tello_takeoff(self):
        self.tello.takeoff()
    
    def tello_land(self):
        self.tello.land()

    def tello_up(self, x):
        self.tello.move_up(x)

    def tello_down(self, x):
        self.tello.move_down(x)

    def tello_forward(self, x):
        self.tello.move_forward(x)

    def tello_backwards(self, x):
        self.tello.move_back(x)

    def tello_left(self, x):
        self.tello.move_left(x)

    def tello_right(self, x):
        self.tello.move_right(x)

    def tello_rotate_clockwise(self, x):
        self.tello.rotate_clockwise(x)

    def tello_rotate_counterclockwise(self, x):
        self.tello.rotate_counter_clockwise(x)

    def tello_flip(self, d):
        """
        d is [l,r,f,b]
        """
        self.tello.flip(d)

    def tello_set_speed(self, x):
        """
        x is in cm/s
        """
        self.tello.set_speed(x)

    def tello_get_battery(self):
        self.tello.get_battery()
    
    def tello_emotion_reaction(self, emotion):
        if emotion == 'Happy':
            self.tello.flip_back()
        elif emotion == 'Neutral':
            self.tello.rotate_clockwise(360)