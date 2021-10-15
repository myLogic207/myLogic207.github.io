# imports
import RPi.GPIO as GPIO                     
import time                                 

# setup pins
GPIO.setmode(GPIO.BOARD)                   
for pin in range(27, 34, 2):       
    GPIO.setup(pin, GPIO.IN)         
    GPIO.setup(pin-5, GPIO.OUT)    
# random infinit loop
while True:                        
    # loop 5 times                 
    for i in range(27, 34, 2):     
        # Check sensor
        state = GPIO.input(i)      
        # just a second
        time.sleep(1)              
        # set state of LED
        GPIO.output(i-5, state) 