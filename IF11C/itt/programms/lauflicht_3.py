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

def ausstieg():
    if GPIO.input(3) == GPIO.HIGH:
        exit()

def richtungscheck():
    if GPIO.input(5) == GPIO.HIGH:
        rechtslauf == False
    if GPIO.input(7) == GPIO.HIGH:
        rechtslauf == True

def lauflicht(led):
    GPIO.output(Outputs[led], GPIO.HIGH)
    time.sleep(Dauer)
    GPIO.output(Outputs[led], GPIO.LOW)

def pincheck(led):
    if led == 0:
        pin = 8
    elif led == 8:
        pin = 0

while True:
    ausstieg()
    richtungscheck()
    if rechtslauf:
        pin += 1
    else:
        pin -= 1
    lauflicht(pin)
    pincheck(pin)