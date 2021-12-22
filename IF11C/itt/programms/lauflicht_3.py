import RPi.GPIO as GPIO   #Importiere Modul und vergebe Alias
import time               

GPIO.setmode(GPIO.BOARD)  #Modus BCM oder Board je nach Bedarf

Outputs = [8, 10, 16, 18, 22, 24, 26, 32]
Inputs = [3, 5, 7]
Dauer = 1
rechtslauf = True
pin = 0

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
    if GPIO.input(5) == GPIO.HIGH:
        rechtslauf = False
    if GPIO.input(7) == GPIO.HIGH:
        rechtslauf = True
    
    lauflicht(pin)
    
    if rechtslauf:
        pin += 1
    else:
        pin -= 1
    
    if pin < 0:
        pin = 7
    elif pin > 7:
        pin = 0
        
GPIO.cleanup()