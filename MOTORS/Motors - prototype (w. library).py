import pineworkslabs.RPi as GPIO
import time

from time import sleep

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
IN1 = 19
IN2 = 20
IN3 = 21
IN4 = 22
ENA = 23

GPIO.cleanup()

# ~ GPIO.output(ENA, GPIO.LOW)

# Go back and forth
def back_n_forth():
	try:
		while(True):
			GPIO.output(IN1, GPIO.HIGH)
			GPIO.output(IN2, GPIO.LOW)
			GPIO.output(IN3, GPIO.LOW)
			GPIO.output(IN4, GPIO.HIGH)
			sleep(.0025)
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.HIGH)
			GPIO.output(IN3, GPIO.LOW)
			GPIO.output(IN4, GPIO.HIGH)
			sleep(.1)
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.HIGH)
			GPIO.output(IN3, GPIO.HIGH)
			GPIO.output(IN4, GPIO.LOW)
			sleep(.0025)
			GPIO.output(IN1, GPIO.HIGH)
			GPIO.output(IN2, GPIO.LOW)
			GPIO.output(IN3, GPIO.HIGH)
			GPIO.output(IN4, GPIO.LOW)
			sleep(.1)
	except KeyboardInterrupt:
		GPIO.cleanup()
		
def clockwise():
	try:
		while(True):
			GPIO.output(IN1, GPIO.HIGH)
			GPIO.output(IN2, GPIO.LOW)
			GPIO.output(IN3, GPIO.HIGH)
			GPIO.output(IN4, GPIO.LOW)
			sleep(.5)
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.LOW)
			GPIO.output(IN3, GPIO.HIGH)
			GPIO.output(IN4, GPIO.LOW)
			sleep(.5)
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.HIGH)
			GPIO.output(IN3, GPIO.HIGH)
			GPIO.output(IN4, GPIO.LOW)
			sleep(.5)
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.LOW)
			GPIO.output(IN3, GPIO.HIGH)
			GPIO.output(IN4, GPIO.LOW)
			sleep(.5)

	except KeyboardInterrupt:
		GPIO.cleanup()

back_n_forth()
