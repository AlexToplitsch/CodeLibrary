import csv  

#adress_file = open("Adressverwaltung.csv", "a")
#writer = csv.writer(adress_file, delimiter = "\t")


while True:
############open csv file#######################
    adress_file = open("Adressverwaltung.csv", "a")
    writer = csv.writer(adress_file, delimiter = ";")
    
    desicion = input("Wollen Sie eine Adresse hinzufügen?   ja/nein \n")
    if desicion.lower() == "nein":
        break
    elif desicion.lower() != "ja":
        continue
        
    while True:  
        last_name = input("Geben Sie den Nachnamen ein:\n")
        if last_name.replace(" ", "") != "":
            break
    while True:
        name = input("Geben Sie den Vornamen ein:\n")
        if name.replace(" ", "") != "":
                break
    while True:
        street = input("Geben Sie die Straße ein:\n")
        if street.replace(" ", "") != "":
                break
            
    while True:
        try:
            house_nr = int(input("Geben Sie die Hausnummer ein: \n"))
            break
        except ValueError:
            print("Bitte geben Sie eine Zahl ein!\n")
            
    while True:        
        place = input("Geben Sie den Ort ein:\n")
        if place.replace(" ", "") != "":
                break
    
    while True:
        try:
            plz = int(input("Geben Sie die Postleitzahl ein: \n"))
            break
        except ValueError:
            print("Bitte geben Sie eine Zahl ein!\n")
            
    with adress_file:
        writer.writerow((last_name.replace(" ", ""), name.replace(" ", ""), street.replace(" ", ""), house_nr, place.replace(" ", ""), plz))
