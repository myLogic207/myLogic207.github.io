# Version 1.0
# Erstellt am: 06.07.2021
# Ersteller: Rol
# Zweck: Werkstatttorüberwachung mit LED Ausgabe.

# import modules
from RPi import GPIO
from time import sleep

# setup pins
GPIO.setmode(GPIO.BOARD)  # Modus BCM oder Board je nach Bedarf

Inputs = [3, 5, 7, 11]
Outputs = [8, 10, 16, 18, 32]
ChangeFlagOld = [0, 0, 0, 0]

for value in Inputs:
    GPIO.setup(value, GPIO.IN)

for value in Outputs:
    GPIO.setup(value, GPIO.OUT)


print(ChangeFlagOld)
while True:
    ChangeFlagNew = [0, 0, 0, 0]
    GPIO.output(32, GPIO.LOW)
    for i in range(len(Inputs)):
        if GPIO.input(Inputs[i]) == GPIO.HIGH:
            GPIO.output(Outputs[i], GPIO.HIGH)
            ChangeFlagNew[i] = 1
        else:
            GPIO.output(Outputs[i], GPIO.LOW)
            ChangeFlagNew[i] = 0
    if ChangeFlagOld != ChangeFlagNew:
        print("Input changed!")
        GPIO.output(32, GPIO.HIGH)
        print(f"{ChangeFlagOld} --> {ChangeFlagNew}")
    ChangeFlagOld = ChangeFlagNew
    sleep(0.05)
