from djitellopy import Tello
from pynput import keyboard
import time

# Initialize the Tello drone
tello = Tello()
tello.connect()

# Print battery level
print("Battery level:", tello.get_battery(), "%")

# Takeoff when the script starts
tello.takeoff()

# Speed of drone movement (can adjust)
SPEED = 50

def on_press(key):
    try:
        # Detect arrow key presses and control drone movements
        if key == keyboard.Key.up:
            tello.move_forward(SPEED)
            print("Moving forward")
        elif key == keyboard.Key.down:
            tello.move_back(SPEED)
            print("Moving backward")
        elif key == keyboard.Key.left:
            tello.move_left(SPEED)
            print("Moving left")
        elif key == keyboard.Key.right:
            tello.move_right(SPEED)
            print("Moving right")
        elif key.char == '1':
            tello.move_up(SPEED)
            print("Moving up")
        elif key.char == '2':
            tello.move_down(SPEED)
            print("Moving down")
        elif key.char == '3':
            tello.rotate_counter_clockwise(45)
            print("Rotating left")
        elif key.char == '4':
            tello.rotate_clockwise(45)
            print("Rotating right")

    except AttributeError:
        pass  # Ignore non-character keys not listed

def on_release(key):
    # Land the drone when ESC is pressed
    if key == keyboard.Key.esc:
        print("Landing the drone...")
        tello.land()
        return False  # Stop the listener

# Setup the keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Keep the script running until ESC is pressed
listener.join()

# Ensure drone lands safely if the script ends
tello.land()
