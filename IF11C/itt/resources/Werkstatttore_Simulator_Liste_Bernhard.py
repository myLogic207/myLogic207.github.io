#Version 1.0
#Erstellt am: 06.07.2021
#Ersteller: Rol
#Zweck: Werkstatttorüberwachung mit LED Ausgabe.

# import modules
import RPi.GPIO as GPIO   #Importiere Modul und vergebe Alias
import time               #Zeit wird für sleep Befehl benötigt

# setup pins
GPIO.setmode(GPIO.BOARD)  #Modus BCM oder Board je nach Bedarf

Inputs = [3, 5, 7, 11]  #Alternativ als Tupel Inputs = (3, 5, 7, 11)
Outputs = [8 , 10, 16, 18]

for value in Inputs:            #Für jeden Wert aus Liste lstInputs
    GPIO.setup(value, GPIO.IN)  #Setze Wert als GPIO Input

for value in Outputs:           #Für jeden Wert aus Liste lstOutputs
    GPIO.setup(value, GPIO.OUT) #Setze Wert als GPIO Output 
    
while True:                   #Endlosschleife
    for i in range(len(Inputs)):          #Zählergesteuerte Schleife für Anzahl der Elemente
        if GPIO.input(Inputs[i]) == GPIO.HIGH:  #Falls Spannung auf Input am Index i
            GPIO.output(Outputs[i], GPIO.HIGH)  #Gebe Spannung auf Output am Index i
        else:
            GPIO.output(Outputs[i], GPIO.LOW)
    time.sleep(1)
    
    

