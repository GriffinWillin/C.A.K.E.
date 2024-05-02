import pineworkslabs.RPi as GPIO
import time
from periphery import PWM

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

p = PWM(16, 500)

p.frequency = 1e3
p.duty_cycle = .75

p.enable()

p.duty_cycle = .5

p.close()

def SpinMotor(direction, num_steps):
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(0.01)
        num_steps -= 1
    p.stop()
    GPIO.cleanup()
    return True

direction_import = input("Please enter O or C for Open or Close:")
num_steps = input("Please enter the number of steps:")
if direction_input == "C":
    SpinMotor(False, num_steps)
else:
    SpinMotor(True, num_steps)

