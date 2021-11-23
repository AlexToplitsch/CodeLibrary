from PyQt5.QtCore import pyqtSlot,  Qt,  QDate
from PyQt5.QtWidgets import QDialog,  QMessageBox
from datetime import date

from other.database import Database

from sub.apprentice.Ui_apprentice_edit import Ui_ApprenticeEdit

class GuiApprenticeEdit(QDialog, Ui_ApprenticeEdit):

    def __init__(self, parent=None):
        
        super(GuiApprenticeEdit, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.frameGeometry().width(), self.frameGeometry().height())
        self.personalnummerweitergabe = self.parent().personalnummerweitergabe
        self.db_auslesen()
        
            
    def closeEvent(self, event):
        self.parent().show()    
    
    def db_auslesen(self):
        
        #Datenbank Klasse aufrufen
        db = Database.get_instance(self)
        
        #Zeile mit der ausgewählten Personalnummer aus der DB auslesen
        sql = "SELECT * FROM kat_lehrlinge WHERE Personalnummer = '"+ self.personalnummerweitergabe +"'"
        
        cursor = db.select(sql)
        
        if cursor == "backtologin":
                self.backtologin()
                return
        
        for z in cursor: #Zeile auslesen und ausgeben
            self.lineEdit_vorname.setText(str(z[1]))

            self.lineEdit_nachname.setText(str(z[2]))
            
            print(str(z[8]))
            
            #Datum richtig formatrieren und in die Datum Felder einfügen
            y, m, d = str(z[3])[0:4], str(z[3])[5:7], str(z[3])[8:10]
            self.dateEdit_geburtsdatum.setDate(QDate(int(y),int(m), int(d)))

            y, m, d = str(z[8])[0:4], str(z[8])[5:7], str(z[8])[8:10]
            self.dateEdit_lehrbeginn.setDate(QDate(int(y),int(m), int(d)))
            
            #Das richtige Item in den Comboboxen auswählen!
            index = self.comboBox_geschlecht.findText(str(z[4]), Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_geschlecht.setCurrentIndex(index)

            index = self.comboBox_lehrberuf.findText(str(z[5]), Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_lehrberuf.setCurrentIndex(index)

            index = self.comboBox_hauptmodul.findText(str(z[6]), Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_hauptmodul.setCurrentIndex(index)

            index = self.comboBox_spezialmodul.findText(str(z[7]), Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_spezialmodul.setCurrentIndex(index)
                
            #Weitere Werte aus der DB in die Felder schreibern
            self.label_personalnummer.setText(str(z[0]))
            self.lineEdit_vorname.setText(str(z[1]))
            self.lineEdit_nachname.setText(str(z[2]))
            self.spinBox_lehrdauer.setValue(int(z[9]))
            self.lineEdit_mail.setText(str(z[10]))
            self.lineEdit_telefonnummer.setText(str(z[11]))
            self.lineEdit_strasse.setText(str(z[12]))
            self.lineEdit_hausnummer.setText(str(z[13]))
            self.lineEdit_plz.setText(str(z[14]))
            self.lineEdit_ort.setText(str(z[15]))
            self.lineEdit_lkz.setText(str(z[16]))
            
            #Vor und Nachname gemeinsam in einem Feld Ausgeben
            self.label_vor_nach_name.setText(str(z[1]+ " " + str(z[2])))
            
            #Lehrjahr berechnen und ausgeben
            today = date.today()
            ty, tm, td = str(today)[0:4], str(today)[5:7], str(today)[8:10]
            
            if ty > y:
                lj = int(ty) - int(y)
                if tm > m and td > d:
                    lj = int(ty) - int(y) + 1
            else:
                lj = 1
            
            self.label_lj.setText(str(lj))
        
        del db
        
    @pyqtSlot()
    def on_pushButton_abbrechen_clicked(self):
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pushButton_speichern_clicked(self):
        
        #Textfelder (Änderungen in den Textfeldern) in Variablen speichern
        Personalnummer = self.label_personalnummer.text()
        
        errors = []
        
        self.lineEdit_vorname.setStyleSheet("border: 1px solid grey")
        self.lineEdit_nachname.setStyleSheet("border: 1px solid grey")
        
        #Eingaben in die Textfelder in Variablen speichen
        Vorname = self.lineEdit_vorname.text()
        Nachname = self.lineEdit_nachname.text()
        Geburtsdatum = self.dateEdit_geburtsdatum.text()
        Geschlecht = self.comboBox_geschlecht.currentText()
        Lehrberuf = self.comboBox_lehrberuf.currentText()
        Hauptmodul = self.comboBox_hauptmodul.currentText()
        Spezialmodul = self.comboBox_spezialmodul.currentText()
        Lehrbeginn = self.dateEdit_lehrbeginn.text()
        Lehrdauer = self.spinBox_lehrdauer.text()
        Mail = self.lineEdit_mail.text()
        Telefonnummer = self.lineEdit_telefonnummer.text()
        Strasse = self.lineEdit_strasse.text()
        Hausnummer = self.lineEdit_hausnummer.text()
        PLZ = self.lineEdit_plz.text()
        ORT = self.lineEdit_ort.text()
        LKZ = self.lineEdit_lkz.text()
        
        #Eingaben von Datum in richtiges Format für DB umwandeln 
        d, m, y = str(Geburtsdatum)[0:2], str(Geburtsdatum)[3:5], str(Geburtsdatum)[6:10]
        Geburtsdatum = y +"-"+ m +"-"+ d
        print(str(Geburtsdatum))
        
        d, m, y = str(Lehrbeginn)[0:2], str(Lehrbeginn)[3:5], str(Lehrbeginn)[6:10]
        Lehrbeginn = y +"-"+ m +"-"+ d
        
        #Errors
        if Personalnummer.isdecimal() == False:
            errors.append("Personalnummer")
            self.lineEdit_personalnummer.setStyleSheet("border: 1px solid red")
        if Vorname == "":
            errors.append("Vorname")
            self.lineEdit_vorname.setStyleSheet("border: 1px solid red")
        if Nachname == "":
            errors.append("Nachname")
            self.lineEdit_nachname.setStyleSheet("border: 1px solid red")
        
        if len(errors) < 1:
            #Variablen in Datenbank schreiben
            sql = "REPLACE INTO kat_lehrlinge (Personalnummer,Vorname,Nachname,Geburtsdatum,Geschlecht,Lehrberuf,Hauptmodul,Spezialmodul,Lehrbeginn,Lehrdauer,Mail,Telefonnummer,Strasse,Hausnummer,PLZ,ORT,LKZ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (str(Personalnummer), str(Vorname), str(Nachname),str(Geburtsdatum), str(Geschlecht),str(Lehrberuf),str(Hauptmodul),str(Spezialmodul),str(Lehrbeginn),str(Lehrdauer),str(Mail),str(Telefonnummer),str(Strasse),str(Hausnummer),str(PLZ),str(ORT),str(LKZ))
            
            #Datenbank Klasse aufrufen
            db = Database.get_instance(self)
            error = db.insert(sql, val)
            
            if error == "backtologin":
                self.back_to_login()
                return

            self.parent().stammdaten_db_auslesen()
            self.parent().show()
            self.close()
        
        #Error Message Box ausgeben
        else:
            messageBox = QMessageBox(self)
            messageBox.setWindowTitle("Fehler")
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setText("Es wurde nicht alles richtig ausgefüllt!\nBeachtzen sie Pflichtfelder!")
            messageBox.addButton("Okay", QMessageBox.NoRole) 
            messageBox.exec_()
    
    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
