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

# emergency stop
STOP = 19

# Set up GPIO
GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

pins = [STEP_PIN, DIR_PIN, ENA, STEP_PIN1, DIR_PIN1, ENA1]

for i in pins:
    GPIO.setup(i, GPIO.OUT)

GPIO.setup(STOP, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

##########################################################

# Function to step the motor
def step_motor(steps, delay, pin):

    # Step the motor
    for _ in range(steps):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
        #print(f"process complete {_} : {pin}")

##############################################################
theBug = True
runnin = True
in_opr = False
h_tick = 0

def estop(): # disable both motors, turn off operation
    global in_opr
    global h_tick
    in_opr = False
    
    GPIO.cleanup()
    GPIO.output(ENA, GPIO.HIGH) # stop 1
    GPIO.output(DIR_PIN1, GPIO.LOW) # clockwise/up
    step_motor(steps=h_tick, delay = .005, pin = STEP_PIN1)
    h_tick = 0
    GPIO.output(ENA1, GPIO.HIGH) # stop motor 2
    GPIO.output(ENA, GPIO.HIGH) # stop 1
    print("ESTOPPPP!!!")
    

def rotate_tray(degrees, speed): # motor 1
    global in_opr
    GPIO.output(ENA, GPIO.LOW) # start motor 1
    GPIO.output(DIR_PIN, GPIO.HIGH) # Clockwise
    rel_ang = 0
    while(rel_ang < degrees):
        if (in_opr == True):
            if GPIO.input(STOP) == 1:
                estop()
                return
            step_motor(steps=1, delay = speed, pin = STEP_PIN)
            rel_ang += 1.8
            rel_ang = round(rel_ang,5)
            if (theBug):
                print(f"ANGLE {rel_ang}, {in_opr}")
                #print(GPIO.input(STOP))
    GPIO.output(ENA, GPIO.HIGH) # stop motor 1
    
def cut(depth, speed): # motor 2
    global in_opr
    global h_tick
    GPIO.output(ENA1, GPIO.LOW) # start motor 2
    GPIO.output(DIR_PIN1, GPIO.HIGH) # anticlockwise/down
    rel_len = 0
    while(rel_len < depth):
        if(in_opr):
            if GPIO.input(STOP) == 1:
                estop()
                break
            step_motor(steps=1, delay = speed, pin = STEP_PIN1)
            h_tick += 1 # 1 tick = 2/5 mm
            rel_len += .4
            rel_len = round(rel_len,5)
            if (theBug):
                print(f"LEN {rel_len}, ")
                #print(GPIO.input(STOP))
                
    GPIO.output(DIR_PIN1, GPIO.LOW) # clockwise/up
    step_motor(steps=h_tick, delay = speed, pin = STEP_PIN1)
    h_tick = 0
    GPIO.output(ENA1, GPIO.HIGH) # stop motor 1
    

    
    
def cut_cycle(slices, wait, speed = 50, depth = None): # change default depth
    global in_opr
    act_speed = (.0625*(speed/100))
    in_opr = True
    i = 0
    while (i < slices/2):
        if(in_opr):
            rotate_tray((360/slices),act_speed) # rotate tray
            time.sleep(.5)
            cut(depth, .00125)
            i += 1                          # raise cut counter
            if(theBug):
                print(f"{i} out of {round(slices/2)}")
            time.sleep(wait)
        

##############################################################

# MAIN

while(runnin):
    try:  
        #gui stuff
        cut_cycle(2,1,30,50)
        runnin = False
    
    except KeyboardInterrupt:
        runnin = False
        in_opr = False
        GPIO.cleanup()
        GPIO.output(ENA, GPIO.HIGH) # stop motor 1
        GPIO.output(ENA1, GPIO.HIGH) # stop motor 2
        
GPIO.cleanup()
GPIO.output(ENA, GPIO.HIGH) # stop motor 1
GPIO.output(ENA1, GPIO.HIGH) # stop motor 2
