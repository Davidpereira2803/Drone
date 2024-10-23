from djitellopy import Tello
from time import sleep

# Initialize and connect to the drone
drone = Tello()

drone.connect()

# Check battery level (just to confirm communication is working)
battery = drone.get_battery()
print(f"Battery level: {battery}%")

# Enable stream (if needed)
drone.streamon()

# Takeoff
drone.takeoff()

# Give some time before issuing movement commands
sleep(2)

# Move up 50 cm
drone.move_up(50)

# Land the drone
drone.land()

# End connection
drone.end()
