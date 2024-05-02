# import the required libraries
import pineworkslabs.RPi as GPIO
import time

# Define GPIO pins connected to the A4988 driver
STEP_PIN = 20  # GPIO pin for Step signal
DIR_PIN = 21   # GPIO pin for Direction signal
ENA = 22       # GPIO pin for the Enable signal

# Debug variable
DEBUG = False

# setup for second motor
STEP_PIN1 = 24
DIR_PIN1 = 25
ENA1 = 26

# Set up GPIO
GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

# Set up GPIO Pins
pins = [STEP_PIN, DIR_PIN, ENA, STEP_PIN1, DIR_PIN1, ENA1]

for i in pins:
    GPIO.setup(i, GPIO.OUT)

#################### FUNCTIONS  ###############################


# Function to step the motor
def step_motor(steps, delay, pin):

    # Step the motor
    for i in range(steps):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
        if DEBUG:
            print(f"process complete {i} : {pin}")

##############################################################

# 200 steps is a full 360' rotation

for i in range(8):
    
    # Pie cut 180
    GPIO.output(ENA1, GPIO.HIGH) # Stop motor 2
    GPIO.output(ENA, GPIO.LOW) # start motor 1
    GPIO.output(DIR_PIN, GPIO.HIGH) # Clockwise
    step_motor(steps=100, delay=0.0004, pin=STEP_PIN) # do the stepping 
    GPIO.output(DIR_PIN, GPIO.LOW) # Counterclockwise
    step_motor(steps=100, delay=0.0004, pin=STEP_PIN)
    
    # Pan turn 90
    GPIO.output(ENA1, GPIO.LOW) # start motor 2
    GPIO.output(ENA, GPIO.HIGH) # stop motor 1
    GPIO.output(DIR_PIN1, GPIO.HIGH) # Clockwise
    step_motor(steps=50, delay=0.0004, pin=STEP_PIN1)  



# Older code:

# ~ try:
    # ~ # Step the motor 200 steps (full revolution)
    # ~ GPIO.output(DIR_PIN, GPIO.HIGH) # Clockwise
    # ~ step_motor(steps=100, delay=0.005, pin=STEP_PIN)  # Adjust delay for speed controlf
    # ~ time.sleep(1)
    # ~ GPIO.output(DIR_PIN, GPIO.LOW)
    # ~ step_motor(steps=100, delay=0.005, pin=STEP_PIN)  # Adjust delay for speed controlf
    # ~ time.sleep(1)

# ~ except KeyboardInterrupt:
    # ~ # Clean up GPIO
    # ~ GPIO.cleanup()
