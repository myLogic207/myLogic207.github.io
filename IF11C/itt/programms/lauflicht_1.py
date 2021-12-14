import RPi.GPIO as GPIO   #Importiere Modul und vergebe Alias
import time               

GPIO.setmode(GPIO.BOARD)  #Modus BCM oder Board je nach Bedarf

Outputs = [8, 10, 16, 18, 22, 24, 26, 32]
Dauer = 1

for i in Outputs:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

while True:
    for i in Outputs:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(Dauer)
        GPIO.output(i, GPIO.LOW)