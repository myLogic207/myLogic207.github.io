# imports
import RPi.GPIO as GPIO                     # import GPIO lib
import time                                 # import cmos time, useless

# define pin-sets
leds = [22, 24, 26, 28]                     # define all led pins
sensors = [27, 29, 31, 33]                  # define all sensor pins

# setup pins
GPIO.setmode(GPIO.BOARD)                    # set pin layout to Pi-Board
for pin in leds:                            # loop over led pins
    GPIO.setup(int(pin), GPIO.OUT)          # set led pin to output
for pin in sensors:                         # loop over sensor pins
    GPIO.setup(int(pin), GPIO.IN)           # set sensor pin to input
# random infinit loop
while True:                                 # infinit loop for execution
    # loop 5 times                          # generic loop, 5 times
    for i in range(4):                      # "connect" sensor to specific led
        # Check sensor
        state = GPIO.input(sensors[i])      # save sensor state i.e. High/Low
        # just a second
        time.sleep(1)                       # wait a second
        # set state of LED
        GPIO.output(leds[i], state)         # set led pin to sensor state