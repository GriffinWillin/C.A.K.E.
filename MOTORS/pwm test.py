import pineworkslabs.RPi as GPIO
import time

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

IN1 = 19
IN2 = 20
IN3 = 21
IN4 = 22
ENA = 13

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)


import time

duty_cycle = 50

try:
    while True:
        print("GPIO High")
        GPIO.output(IN1, GPIO.HIGH)
        time.sleep(duty_cycle / 100.0)

        print("GPIO Low")
        GPIO.output(IN1, GPIO.LOW)
        time.sleep((100 - duty_cycle) / 100)

except KeyboardInterrupt:
    pass