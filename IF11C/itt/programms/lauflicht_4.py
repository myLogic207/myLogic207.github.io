import RPi.GPIO as GPIO   #Importiere Modul und vergebe Alias
import time               

GPIO.setmode(GPIO.BOARD)  #Modus BCM oder Board je nach Bedarf

Outputs = [8, 10, 16, 18, 22, 24, 26, 32]
Inputs = [3, 5, 7]
Dauer = 1
Richtung = 1
pin = 0
extra = 12

GPIO.setup(12, GPIO.OUT)

for i in Outputs:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
for i in Inputs:
    GPIO.setup(i, GPIO.IN)

def lauflicht(led):
    GPIO.output(Outputs[led], GPIO.HIGH)
    time.sleep(Dauer)
    GPIO.output(Outputs[led], GPIO.LOW)

while GPIO.input(3) == GPIO.LOW:
    if GPIO.input(5) == GPIO.HIGH and Richtung == 1:
        Richtung = -1
        GPIO.output(12, GPIO.HIGH)
    elif GPIO.input(5) == GPIO.HIGH and Richtung == -1:
        Richtung = 1
        GPIO.output(12, GPIO.LOW)
    
    lauflicht(pin)
    
    pin += Richtung
    
    if pin < 0:
        pin = len(Outputs) - 1
    elif pin > len(Outputs)-1:
        pin = 0
        
GPIO.cleanup()