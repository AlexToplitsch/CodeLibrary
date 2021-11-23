import csv
toWrite = [["a","b"],["c","D"]]

file = open("Auswertung_Zahlenratespiel.csv", "w")
with file:
    writer = csv.writer(file)
    
for row in toWrite:
    writer.writerow(row)

file.close()