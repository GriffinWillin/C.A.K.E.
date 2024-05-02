
# import the required libraries
import pineworkslabs.RPi as GPIO
import time
from random import randint

# Define GPIO pins connected to the A4988 driver
DIR_PIN = 20 # GPIO pin for STEP signal
STEP_PIN = 21   # GPIO pin for DIR signal
ENA = 22       # GPIO pin for the ENA signal

# setup for second motor
DIR_PIN1 = 24
STEP_PIN1 = 25
ENA1 = 26

# Set up GPIO
GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

pins = [STEP_PIN, DIR_PIN, ENA, STEP_PIN1, DIR_PIN1, ENA1]

for i in pins:
    GPIO.setup(i, GPIO.OUT)

##########################################################


# Function to step the motor
def step_motor(steps, delay, pin):

    # Step the motor
    for _ in range(steps):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
        print(f"process complete {_} : {pin}")

##############################################################

increment = 0.005

try:
    for i in range(4):
        
        # Pie cut 180
        GPIO.output(ENA1, GPIO.HIGH) # Stop motor 2
        GPIO.output(ENA, GPIO.LOW) # start motor 1
        GPIO.output(DIR_PIN, GPIO.HIGH) # Clockwise
        step_motor(steps=100, delay=increment, pin=STEP_PIN)  
        GPIO.output(DIR_PIN, GPIO.LOW)
        step_motor(steps=100, delay=increment, pin=STEP_PIN)
        
        # Pan turn 90
        GPIO.output(ENA1, GPIO.LOW) # start motor 2
        GPIO.output(ENA, GPIO.HIGH) # stop motor 1
        GPIO.output(DIR_PIN1, GPIO.HIGH) # Clockwise
        step_motor(steps=50, delay=increment, pin=STEP_PIN1)  

except KeyboardInterrupt:
    GPIO.cleanup()
