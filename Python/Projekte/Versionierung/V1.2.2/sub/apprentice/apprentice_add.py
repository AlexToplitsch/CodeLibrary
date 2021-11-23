from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QMessageBox,  QFileDialog
from PyQt5.QtGui import QImage,  QPixmap

from other.database import Database

from sub.apprentice.Ui_apprentice_add import Ui_ApprenticeAdd

class GuiApprenticeAdd(QDialog, Ui_ApprenticeAdd):
    
    def __init__(self, parent):

        super(GuiApprenticeAdd, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.frameGeometry().width(), self.frameGeometry().height())
        
    @pyqtSlot()
    def on_pushButton_abbrechen_clicked(self):
        print("by")
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pushButton_add_picture_clicked(self):
        print("Hi")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Das Bild soll das Format 1:1 (Quadratisch) besitzen!","","JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            print(fileName)
            with open(fileName, 'rb') as file:
                self.binaryData = file.read()
            
            self.pushButton_add_picture.hide()
            #Bild des Lehrlings ausgeben
            qimg = QImage.fromData(self.binaryData)
            pixmap = QPixmap.fromImage(qimg)
            pixmap = pixmap.scaled(100, 100)
            self.label_picture.setPixmap(pixmap)
            
            
        
        
    @pyqtSlot()
    def on_pushButton_hinzufuegen_clicked(self):
        
        errors = []
        
        self.lineEdit_personalnummer.setStyleSheet("border: 1px solid grey")
        self.lineEdit_vorname.setStyleSheet("border: 1px solid grey")
        self.lineEdit_nachname.setStyleSheet("border: 1px solid grey")
        
        #Eingaben in die Textfelder in Variablen speichen
        Personalnummer = self.lineEdit_personalnummer.text()
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
        
        #Bild einfügen
        Bild = self.binaryData
        
        #Eingaben von Datum in richtiges Format für DB umwandeln 
        d, m, y = str(Geburtsdatum)[0:2], str(Geburtsdatum)[3:5], str(Geburtsdatum)[6:10]
        Geburtsdatum = y +"-"+ m +"-"+ d
        #print(str(Geburtsdatum))
        
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
            sql = "INSERT INTO kat_lehrlinge (Personalnummer,Vorname,Nachname,Geburtsdatum,Geschlecht,Lehrberuf,Hauptmodul,Spezialmodul,Lehrbeginn,Lehrdauer,Mail,Telefonnummer,Strasse,Hausnummer,PLZ,ORT,LKZ,Bild) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (str(Personalnummer), str(Vorname), str(Nachname),str(Geburtsdatum), str(Geschlecht),str(Lehrberuf),str(Hauptmodul),str(Spezialmodul),str(Lehrbeginn),str(Lehrdauer),str(Mail),str(Telefonnummer),str(Strasse),str(Hausnummer),str(PLZ),str(ORT),str(LKZ), Bild)
            
            #Datenbank Klasse aufrufen
            db = Database.get_instance(self)
            error = db.insert(sql, val)
            
            if error == "backtologin":
                self.back_to_login()
                return
            
            #Wenn der Error Code = 1062 (Personalnummer gibt es bereits)
            if error == 1062:
                self.lineEdit_personalnummer.setStyleSheet("border: 1px solid red")
                
                #Error Message Box ausgeben
                messageBox = QMessageBox(self)
                messageBox.setWindowTitle("Fehler")
                messageBox.setIcon(QMessageBox.Warning)
                messageBox.setText("Diese Personalnummer existiert bereits")
                messageBox.addButton("Okay", QMessageBox.NoRole) 
                messageBox.exec_()
                
            else:
                self.parent().db_auslesen()
                self.parent().show()
                self.close()
                
            del db
        
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
        
            
    def closeEvent(self, event):
        self.parent().show()
