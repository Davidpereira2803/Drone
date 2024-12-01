from djitellopy import Tello

def tello_take_off(tello):
    tello.takeoff()

def tello_land(tello):
    tello.land()

def tello_up(tello, x):
    tello.up(x)

def tello_down(tello, x):
    tello.down(x)

def tello_forward(tello, x):
    tello.forward(x)

def tello_backwards(tello, x):
    tello.back(x)

def tello_left(tello, x):
    tello.left(x)

def tello_right(tello, x):
    tello.right(x)

def tello_rotate_clockwise(tello, x):
    tello.cw(x)

def tello_rotate_counterclockwise(tello, x):
    tello.ccw(x)

def tello_flip(tello, d):
    """
    d is [l,r,f,b]
    """
    tello.flip(d)

def tello_set_speed(tello, x):
    """
    x is in cm/s
    """
    tello.speed(x)

def tello_get_battery(tello):
    tello.battery()

