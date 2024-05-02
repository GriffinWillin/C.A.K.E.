import pineworkslabs.RPi as GPIO
import time

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)

# Define GPIO pins connected to L298 module
IN1 = 19
IN2 = 20
IN3 = 21
IN4 = 22
# ~ ENA = 13

# Set up GPIO mode and pins
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
# ~ GPIO.setup(ENA, GPIO.OUT)


def stepper_backward(delay, steps):
	for i in range(0,steps):
		print(i)

		# ~ GPIO.output(IN1, GPIO.LOW)
		# ~ GPIO.output(IN2, GPIO.HIGH)
		# ~ GPIO.output(IN3, GPIO.LOW)
		# ~ GPIO.output(IN4, GPIO.HIGH)
		# ~ time.sleep(delay)
		GPIO.output(IN1, GPIO.HIGH)
		GPIO.output(IN2, GPIO.LOW)
		GPIO.output(IN3, GPIO.HIGH)
		GPIO.output(IN4, GPIO.LOW)
		time.sleep(delay)
		# ~ GPIO.output(IN1, GPIO.HIGH)
		# ~ GPIO.output(IN2, GPIO.LOW)
		# ~ GPIO.output(IN3, GPIO.LOW)
		# ~ GPIO.output(IN4, GPIO.HIGH)
		# ~ time.sleep(delay)
		# ~ GPIO.output(IN1, GPIO.LOW)
		# ~ GPIO.output(IN2, GPIO.HIGH)
		# ~ GPIO.output(IN3, GPIO.HIGH)
		# ~ GPIO.output(IN4, GPIO.LOW)
		# ~ time.sleep(delay)

# Main program
try:
	while True:
		# Move stepper motor forward for 200 steps with a delay of 0.005 seconds between steps
		# ~ stepper_forward(1000, 200)
		# ~ time.sleep(.05)
		# Move stepper motor backward for 200 steps with a delay of 0.005 seconds between steps
		stepper_backward(5, 5)
		time.sleep(.0025)
		

except KeyboardInterrupt:
	print("Program stopped by user")
	GPIO.cleanup()
