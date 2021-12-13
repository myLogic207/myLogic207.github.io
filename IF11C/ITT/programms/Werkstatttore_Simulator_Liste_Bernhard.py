#Version 1.0
#Erstellt am: 06.07.2021
#Ersteller: Rol
#Zweck: Werkstatttorueberwachung mit LED Ausgabe.

# import modules
import RPi.GPIO as GPIO   #Importiere Modul und vergebe Alias
import time               

GPIO.setmode(GPIO.BOARD)  #Modus BCM oder Board je nach Bedarf

Inputs = [3, 5, 7, 11]  #Alternativ als Tupel Inputs = (3, 5, 7, 11)
Outputs = [8, 10, 16, 18, 32]
ChangedFlagOld = [0, 0, 0, 0]

def ledCheck():
    for i in range(len(Inputs)):         
        if GPIO.input(Inputs[i]) == GPIO.HIGH:  #Falls Spannung auf Input am Index i
            GPIO.output(Outputs[i], GPIO.HIGH)  #Gebe Spannung auf Output am Index i
            ChangedFlagNew[i] = 1
        else:
            GPIO.output(Outputs[i], GPIO.LOW)
            ChangedFlagNew[i] = 0    

def report():
    print(ChangedFlagNew)
    if ChangedFlagNew != ChangedFlagOld:
        print("Keine Änderungen")
        GPIO.output(32, GPIO.HIGH)

# setup pins

for value in Inputs:            
    GPIO.setup(value, GPIO.IN)  #Setze Wert als GPIO Input

for value in Outputs:           
    GPIO.setup(value, GPIO.OUT) #Setze Wert als GPIO Output 
    
while True:                   #Endlosschleife
    ChangedFlagNew = [0, 0, 0, 0]
    GPIO.output(32, GPIO.LOW)
    ledCheck()
    report()
    ChangedFlagOld = ChangedFlagNew
    time.sleep(1)



    
    

