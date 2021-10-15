# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.IN)

# loop 5 times
for i in range(5):
    
    # flash output pin 3
    GPIO.output(3, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3, GPIO.LOW)
    time.sleep(1)
    
    # read input pin 5
    if GPIO.input(5) == GPIO.HIGH:
        print("Pin 5 is on")
    else:
        print("Pin 5 is off")    