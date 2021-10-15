"""Programm to print and change parking spaces"""
def print_all_status():
    """Prints the status of all parking spaces"""
    counter = 1
    for pos in parkplatz:
        match pos:
            case 0:
                print("Parkplatz", counter, "ist Frei")
            case 1:
                print("Parkplatz", counter, "ist Belegt")
            case 2:
                print("Parkplatz", counter, "ist Reserviert")
        counter+=1

def number_in_range(given_number, floor, roof):
    """Checks for a specific number to be in a given range"""
    return floor <= given_number <= roof

def change_status():
    """Change the status of a given parking space"""
    while True:
        i_parkplatz_nr = int(input("Zum bearbeiten nummer eingeben:(1-10)"))
        i_status = int(input("Neuen Wert zuweisen:(0-2)"))
        if number_in_range(i_parkplatz_nr, 1, 10) and number_in_range(i_status, 0,2):
            parkplatz[i_parkplatz_nr-1] = i_status
            print("Parkplatz", i_parkplatz_nr, "hat nun den status", i_status)
        else:
            print("Eingabe abgebrochen/ungültig")

parkplatz = [0, 0, 1, 0, 1, 1, 2, 1, 0, 2]

while True:
    print("----- Starting PISS - Parkinglot Information Service Script -----")
    print_all_status()
    change = bool(input("Want to change a Space (0/1)?"))
    if change:
        change_status()
    print("--------------------------------")
