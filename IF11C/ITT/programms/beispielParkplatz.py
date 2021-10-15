array = [0,0,0,0,0,0,0,0,0,0]

while True:
    i = 0
    while i<=9:
        match array[i]:
            case 0: print("Parkplatz ", i+1, " ist frei.")
            case 1: print("Parkplatz ", i+1, " ist belegt.")
            case 2: print("Parkplatz ", i+1, " ist reserviert.")
        i=i+1
    iStatus = int(input())
    iParkplatzNr = int(input())
    print("Alte Parkplatznummer: ", array[iParkplatzNr])
    array[iParkplatzNr-1] = iStatus
