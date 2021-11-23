from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage,  QPixmap
from PyQt5.QtWidgets import  QDialog, QMessageBox
from datetime import date

from other.database import Database

from sub.apprentice.Ui_apprentice_manager import Ui_ApprenticeManager

from sub.apprentice.apprentice_edit import GuiApprenticeEdit


class GuiApprenticeManager(QDialog, Ui_ApprenticeManager):
    
    def __init__(self, parent=None):

        super(GuiApprenticeManager, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.frameGeometry().width(), self.frameGeometry().height())
        self.personalnummerweitergabe = self.parent().personalnummerweitergabe
        self.stammdaten_db_auslesen()
        
    def stammdaten_db_auslesen(self):
        
        #Datenbank Klasse aufrufen
        db = Database.get_instance(self)
        
        sql = "SELECT * FROM kat_lehrlinge WHERE Personalnummer = '"+ self.personalnummerweitergabe +"'"
        cursor = db.select(sql)
        
        if cursor == "backtologin":
                self.backtologin()
                return
        
        for z in cursor: #Zeilen auslesen und ausgeben
            
            #Lehrjahr berechnen!
            y, m, d = str(z[8])[0:4], str(z[8])[5:7], str(z[8])[8:10]
            today = date.today()
            ty, tm, td = str(today)[0:4], str(today)[5:7], str(today)[8:10]
            
            if ty > y:
                lj = int(ty) - int(y)
                if tm > m and td > d:
                    lj = int(ty) - int(y) + 1
            else:
                lj = 1
            
            #Bild des Lehrlings ausgeben
            qimg = QImage.fromData(z[21])
            pixmap = QPixmap.fromImage(qimg)
            pixmap = pixmap.scaled(100, 100)
            self.label_picture.setPixmap(pixmap)
            
            #Stammdaten des Lehrlings in die Felder schreiben
            self.label_geburtsdatum.setText(str(z[3]))
            self.label_geschlecht.setText(str(z[4]))
            self.label_personalnummer.setText(str(z[0]))
            self.label_lehrberuf.setText(str(z[5]))
            self.label_hauptmodul.setText(str(z[6]))
            self.labe_spezialmodul.setText(str(z[7]))
            self.label_lehrbeginn.setText(str(z[8]))
            self.label_lehrdauer.setText(str(z[9]))
            self.label_mail.setText(str(z[10]))
            self.label_telefonnummer.setText(str(z[11]))
            self.label_strasse.setText(str(z[12]))
            self.label_hausnummer.setText(str(z[13]))
            self.label_plz.setText(str(z[14]))
            self.label_ort.setText(str(z[15]))
            self.label_lkz.setText(str(z[16]))
            self.label_vor_nach_name.setText(str(z[1]+ " " + str(z[2])))
            self.label_lj.setText(str(lj))
            
    def closeEvent(self, event):
        self.parent().show()
    
    @pyqtSlot()
    def on_pushButton_lehrling_loeschen_clicked(self):
        
        #Messagebox für abfrage ob der Lehrling wirklich gelöscht werden soll.
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Wirklich löschen?")
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setText("Möchten sie den Lehrling wirklich löschen?")
        ok = messageBox.addButton("Löschen", QMessageBox.YesRole)    
        messageBox.addButton("Abbrechen", QMessageBox.NoRole) 
        messageBox.exec_()
        
        #Wenn Löschung bestätigt, dann den Lehrling löschen
        if messageBox.clickedButton() == ok:
            
            #Datenbank Klasse aufrufen
            db = Database.get_instance(self)
            
            #Lehrling löschen
            sql = "DELETE FROM kat_lehrlinge WHERE Personalnummer ="+ self.personalnummerweitergabe +""
            error = db.delete(sql)
            
            if error == "backtologin":
                self.back_to_login()
                return
            
            self.parent().db_auslesen()
            self.parent().show()
            self.close()
        
    @pyqtSlot()
    def on_pushButton_stammdaten_bearbeiten_clicked(self):
        w = GuiApprenticeEdit(self)
        w.show()
        self.hide()
    
    @pyqtSlot()
    def on_pushButton_alle_lehrlinge_clicked(self):
        self.parent().db_auslesen()
        self.parent().show()
        self.close()
    
    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
