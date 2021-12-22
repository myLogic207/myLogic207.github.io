#Version 1.1
#Erstellt am: 06.07.2021
#Ersteller: Rol
#Zweck: Werkstatttorüberwachung mit Änderungskennzeichen.

#Änderungshistory
#Verwendung 

# Import Module
import RPi.GPIO as GPIO  
import time

# Module für OPCUA
from random import randint
from opcua import ua, uamethod, Server
from opcua.ua import ObjectIds
import datetime #für Ausgabe

# Setup GPIO-Pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Listen für GPIOs und Schalterzustände 
Inputs = [3,5,7,11]
Outputs = [8,10,16,18,32]
S = [0,0,0,0,0]


#Liste für Initialzustände
ChangeFlagOld = [0, 0, 0, 0]      

for value in Inputs:
    GPIO.setup(value, GPIO.IN)

for value in Outputs:
    GPIO.setup(value, GPIO.OUT)

#Kommentar einfügen
server=Server()
url="opc.tcp://192.168.2.59:4840"
server.set_endpoint(url)

#Kommentar einfügen
name="OPCUA_Serverraum"
addspace=server.register_namespace(name)
node= server.get_objects_node();

#Objekt Raspi Kommentar ergänzen
Raspi=node.add_object(addspace,"Raspi")

#Kommentar ergänzen
myfolder = Raspi.add_folder(addspace, "Schalter")

#OPUA Datenpunkte/Variblen "Schalter1-4" und Changed in den Ordner "Schalter" festlegen
Schalter1 = myfolder.add_variable(addspace,"Schalter1",6.1)
Schalter2 = myfolder.add_variable(addspace,"Schalter2",6.2)
Schalter3 = myfolder.add_variable(addspace,"Schalter3",6.3)
Schalter4 = myfolder.add_variable(addspace,"Schalter4",6.4)
Changed = myfolder.add_variable(addspace,"Changed",6.5)
Time = node.add_variable(addspace,"Time",0)

Schalter1.set_writable()
Schalter2.set_writable()
Schalter3.set_writable()
Schalter4.set_writable()
Changed.set_writable()
Time.set_writable()

#Kommentar ergänzen
server.start()
print("Server startet auf {}",format(url))
while True:
    #Zeit ermitteln
    TIME = datetime.datetime.now()

    #Setze neue Liste für Initialzustände auf 0
    ChangeFlagNew = [0,0,0,0]
    
    GPIO.output(32, GPIO.LOW) #ChangedFlag /Trigger
    S[4]=0
    
    for i in range(len(Inputs)):
        if GPIO.input(Inputs[i]) == GPIO.HIGH:
            GPIO.output(Outputs[i], GPIO.HIGH)
            S[i]=1         #Setze Wert 1 am Index
            ChangeFlagNew[i] = 1    
        else:
            GPIO.output(Outputs[i], GPIO.LOW)
            S[i]=0          #Setze Wert 0 am Index
            ChangeFlagNew[i] = 0    
    
    print(ChangeFlagOld)               #Ausgabe der ursprünglichen Werte    
    if ChangeFlagOld != ChangeFlagNew:  #Vergleiche Ursprüngliche Liste mit neuer Liste
        print("Änderung erfolgt")        #Ausgabe das Änderung passiert ist.
        GPIO.output(32, GPIO.HIGH)
        S[4]=1
    
    #ChangeFlagOld = ChangeFlagNew.copy() #Kopiere alle Werte der neuen Liste in alteListe, da sonst eine Referenz erstellt wird.
    ChangeFlagOld = list(ChangeFlagNew) #Alternative, da copy() erst ab Python 3.3. geht. 
    
    #Ausgabe CLI/Shell
    #print(S[0],S[1],S[2],S[3],S[4],TIME)

    #OPCUA-Nodes .....Kommentar ergänzen..... und damit an url versenden!
    Schalter1.set_value(S[0])
    Schalter2.set_value(S[1])
    Schalter3.set_value(S[2])
    Schalter4.set_value(S[3])
    Changed.set_value(S[4]) #Changed-Flag /Trigger

    Time.set_value(TIME)

    time.sleep(1)
