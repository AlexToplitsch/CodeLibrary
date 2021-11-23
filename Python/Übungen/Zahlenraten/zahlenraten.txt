import random
import xlsxwriter
import csv

#######################Excel Datei und ein Blatt erstellen######################
workbook = xlsxwriter.Workbook("Auswertung_Zahlenratespiel.xlsx")
worksheet = workbook.add_worksheet()

#######################Worksheet mit Bild versehen##############################
worksheet.insert_image(0, 0, "Knapp_Logo.png")

#######################Erste Spalte vergrößern############################
worksheet.set_column("A:A", 20)

######################Text Edit "Fett" hinzufügen########################
bold = workbook.add_format({"bold" : True})

###################### Feldbeschreibung Einfügen #########################
worksheet.write("A4", "Zahlenbereich", bold)
worksheet.write("A5", "Versuche", bold)
worksheet.write("A6", "Zufallszahl", bold)


######Zahlen definition mit Try und except für die Überprfung der eingegebenen Werte######
while True:
    try:
        print("\nWählen Sie den Bereich in dem Sie eine Zahl erraten möchten.")
        obere_zahl = int(input("\nGeben Sie die obere Zahl des Bereiches ein: "))
        untere_zahl = int(input("\nGeben Sie die untere Zahl des Bereiches ein: "))
        break
        
    except ValueError:
        print("\nBitte geben Sie eine Zahl ein!")
       
 
#Setzen der Zufallszahl
if untere_zahl > obere_zahl:
    zwischenspeicher = untere_zahl
    untere_zahl = obere_zahl
    obere_zahl = zwischenspeicher
    
    
zufallszahl = random.randint(untere_zahl, obere_zahl)
ermittelte_zahl = 0
versuche = 1
trys = []


#################Vergleicht die eingegebene Zahl mit der Zufallszahl. Wenn falsch dann wiederholt es sich
while True:
    
###########Eingabe der Zahl mit Überprüfung der Eingabe
    while True:
        try:
            ermittelte_zahl = int(input("\nGeben Sie eine Zahl ein: "))
            break
        except ValueError:
            print("\nBitte geben Sie eine Zahl ein!")
            
            
    #########Versuche mit Zahl eintragen #################        
    worksheet.write(versuche + 8, 0, f"Versuch{versuche}", bold)
    worksheet.write(versuche + 8, 1, ermittelte_zahl) 

    ##########TOWrite Liste mit Versuchen erweitern##############
    trys.append([f"Versuch{versuche}\t", ermittelte_zahl])
    
    
    if ermittelte_zahl == zufallszahl:
        break
    else:
        print("\nDas war leider falsch. Probieren Sie es nochmal.")
    
    versuche += 1   
   
   
   
if versuche == 1:
    print(f"\nGratulation! Sie haben die Zahl mit {versuche} Versuch erraten.")
else:
    print(f"\nGratulation! Sie haben die Zahl in {versuche} Versuchen erraten.")
    
    
##################### Felder füllen ############################
worksheet.write("B4", f"    {untere_zahl} - {obere_zahl}")
worksheet.write("B5", versuche)
worksheet.write("B6", zufallszahl)



###################CSV Datei erstellen #########################

file = open("Auswertung_Zahlenratespiel.csv", "w")
with file:
    write = csv.writer(file)
    
    write.writerow(["Zahlenbereich\t", f"{untere_zahl} - {obere_zahl}"])
    write.writerow(["Versuche\t", f"{versuche}"])
    write.writerow(["Zufallszahl\t", f"{zufallszahl}"])
    for x in trys:
        write.writerow(x)
           


#################### Excel Datei schließen ##########################
workbook.close()


