# -*- coding: utf-8 -*-

"""
Module implementing hinzufügen.
"""

from PyQt5.QtCore import pyqtSlot, QTime
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from other.database import Database
from sub.wochen_unterricht.Ui_hinzufuegen_Plan import Ui_Dialog
from sub.wochen_unterricht.Lehrlings_Tabelle import Lehrlings_Tabelle
class hinzufügen(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(hinzufügen, self).__init__(parent)
        self.setupUi(self)

        #db = Database.get_instance(self)#verbindung zur Datenbank
  
        self.Combobox_Unterrichtsthema_befuellen()
        self.Combobox_Ausbildner_befuellen()
        self.Combobox_Räume_befuellen()
        self.Combobox_Thema1_befuellen()
        self.Combobox_Thema2_befuellen()
        self.Combobox_Thema3_befuellen()
        fielditem = QTableWidgetItem(".")
        self.te_vorschau.setItem(3, 0, fielditem)
        fielditem = QTableWidgetItem(".")
        self.te_vorschau.setItem(4, 0, fielditem)
        self.gesamt_stunden.setText("0")
        self.pushButton_hinzufuegen.setEnabled(False)#danach wird der Button enabled

    
    def Combobox_Unterrichtsthema_befuellen(self): # hier wird die Combobox lan befüllt
        db = Database.get_instance(self)
        sql = "SELECT Ausbildungsthema FROM kat_ausbildungsthemen"
        mycursor = db.select(sql)
        try: #versuche die combobox zu befüllen
   
            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0])
            self.comboBox_Unterrichtsthema.addItems(werte)
            mycursor.close()
        except:#falls ein fehler auftauch soll er das machen 
            res = QMessageBox.critical(
                self,
                self.tr("FEHLER"),
                self.tr("""Die Combobox "Unterrichtsthema" konnte nicht befüllt werden !
Kontrollieren Sie bitte Ihre Datenbankverbindung !"""),
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
            print(res)

    def Combobox_Ausbildner_befuellen(self): # hier wird die Combobox lan befüllt
        db = Database.get_instance(self)
        sql = "SELECT Familienname FROM kat_ausbilder"

        try: #versuche die combobox zu befüllen
            mycursor = db.select(sql)

            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0])
            self.comboBox_ausbilder.addItems(werte)
            mycursor.close()
        except:#falls ein fehler auftauch soll er das machen 
            print("")
            

    def Combobox_Räume_befuellen(self): # hier wird die Combobox lan befüllt
        db = Database.get_instance(self)
        sql = "SELECT Raum FROM kat_raeume"

        try: #versuche die combobox zu befüllen
            mycursor = db.select(sql)

            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0])
            self.comboBox_raum.addItems(werte)
            mycursor.close()
        except:#falls ein fehler auftauch soll er das machen 
            print("")
    
    
    @pyqtSlot()
    def on_pushButton_abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().show()
        self.close()
    
    @pyqtSlot(str)
    def on_comboBox_ausbilder_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Vorname FROM kat_ausbilder WHERE Familienname = "'+ self.comboBox_ausbilder.currentText()+'"' #select der lkz  wo das land
        try: #versuche die combobox zu befüllen
            mycursor = db.select(sql)
           # mycursor.execute(sql)# hier wird der sql befehl ausgeführt
            sql_satz = mycursor.fetchall()# das ist das ergebniss
            mycursor.close()# hier wird der mycursor geschlossen
            satz_len = len (sql_satz)
            if satz_len == 0:           # wenn kein land ausgewählt wurde erscheint ein "?" im entryfiel "LKZ" 
                self.le_vorname.setText('?')
            else:
                self.le_vorname.setText(sql_satz[0][0])
        except:#falls ein fehler auftauch soll er das machen 
            print("test")
        #self.te_vorschau.setText(self.te_vorschau.text()+"n/"+self.comboBox_ausbilder.currentText())
        fielditem = QTableWidgetItem(self.comboBox_Unterrichtsthema.currentText()+"  "+ self.comboBox_ausbilder.currentText())
        self.te_vorschau.setItem(0, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        
    @pyqtSlot(str)
    def on_comboBox_raum_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Stock, Gebäude FROM kat_raeume WHERE Raum = "'+ self.comboBox_raum.currentText()+'"' #select der lkz  wo das land
        
        try: #versuche die combobox zu befüllen
            mycursor = db.select(sql)
           # mycursor.execute(sql)# hier wird der sql befehl ausgeführt
            sql_satz = mycursor.fetchall()# das ist das ergebniss
            mycursor.close()# hier wird der mycursor geschlossen
            satz_len = len (sql_satz)
            if satz_len == 0:           # wenn kein land ausgewählt wurde erscheint ein "?" im entryfiel "LKZ" 
                self.le_raum.setText('?')
            else:
                self.le_raum.setText("Stock "+str(sql_satz[0][0])+"  Gebäude "+str(sql_satz[0][1]))
        except:#falls ein fehler auftauch soll er das machen 
            print("test")
        #self.te_vorschau.setText(self.te_vorschau.text()+"n/"+self.comboBox_raum.currentText())
        fielditem = QTableWidgetItem("         "+self.comboBox_raum.currentText()+"         ")
        self.te_vorschau.setItem(1, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()

    
    
    def Combobox_Thema1_befuellen(self): # hier wird die Combobox lan befüllt
        db = Database.get_instance(self)
        sql = "SELECT Ausbildungsthema FROM kat_lehrstoff"
        mycursor = db.select(sql)
        try: #versuche die combobox zu befüllen
   
            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0])
            self.comboBox_thema1.addItems(werte)
            mycursor.close()
        except:#falls ein fehler auftauch soll er das machen 
            res = QMessageBox.critical(
                self,
                self.tr("FEHLER"),
                self.tr("""Die Combobox "Themen" konnte nicht befüllt werden !
Kontrollieren Sie bitte Ihre Datenbankverbindung !"""),
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
            print(res)
    
    def Combobox_Thema2_befuellen(self): # hier wird die Combobox lan befüllt
        db = Database.get_instance(self)
        sql = "SELECT Ausbildungsthema FROM kat_lehrstoff"
        mycursor = db.select(sql)
        try: #versuche die combobox zu befüllen
   
            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0])
            self.comboBox_thema2.addItems(werte)
            mycursor.close()
        except:#falls ein fehler auftauch soll er das machen 
            res = QMessageBox.critical(
                self,
                self.tr("FEHLER"),
                self.tr("""Die Combobox "Themen" konnte nicht befüllt werden !
Kontrollieren Sie bitte Ihre Datenbankverbindung !"""),
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
            print(res)
        
    def Combobox_Thema3_befuellen(self): # hier wird die Combobox lan befüllt
        db = Database.get_instance(self)
        sql = "SELECT Ausbildungsthema FROM kat_lehrstoff"
        mycursor = db.select(sql)
        try: #versuche die combobox zu befüllen
   
            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0])
            self.comboBox_thema3.addItems(werte)
            mycursor.close()
        except:#falls ein fehler auftauch soll er das machen 
            res = QMessageBox.critical(
                self,
                self.tr("FEHLER"),
                self.tr("""Die Combobox "Themen" konnte nicht befüllt werden !
Kontrollieren Sie bitte Ihre Datenbankverbindung !"""),
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
            print(res)

    @pyqtSlot()
    def on_pushButton_einzelne_lehrlinge_clicked(self):
        """
        Slot documentation goes here.
        """
        w = Lehrlings_Tabelle(self)
        w.show()#Öffnen das SettingGui
        self.hide()#hide the current window
    
    @pyqtSlot(str)
    def on_comboBox_Unterrichtsthema_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
       # self.te_vorschau.setText(self.te_vorschau.text()+"     "+self.comboBox_Unterrichtsthema.currentText())
        fielditem = QTableWidgetItem(self.comboBox_Unterrichtsthema.currentText()+"  "+ self.comboBox_ausbilder.currentText())
        self.te_vorschau.setItem(0, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        # TODO: not implemented yet
       # raise NotImplementedError
    
    @pyqtSlot()
    def on_checkBox_1A_clicked(self):
        """
        Slot documentation goes here.
        """
        fielditem = QTableWidgetItem("1A")
        print(self.te_vorschau.item(3,  0).text())
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    

    
    @pyqtSlot()
    def on_checkBox_1B_clicked(self):
        """
        Slot documentation goes here.
        """
        print(self.te_vorschau.item(3,  0).text())
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 1B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    @pyqtSlot()
    def on_checkBox_2A_clicked(self):
        """
        Slot documentation goes here.
        """
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 2A")
        
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    @pyqtSlot()
    def on_checkBox_2B_clicked(self):
        """
        Slot documentation goes here.
        """
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 2B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    @pyqtSlot()
    def on_checkBox_3A_clicked(self):
        """
        Slot documentation goes here.
        """
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 3A")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    @pyqtSlot()
    def on_checkBox_3B_clicked(self):
        """
        Slot documentation goes here.
        """
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 3B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    @pyqtSlot()
    def on_checkBox_4A_clicked(self):
        """
        Slot documentation goes here.
        """
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 4A")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    @pyqtSlot()
    def on_checkBox_4B_clicked(self):
        """
        Slot documentation goes here.
        """
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 4B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    @pyqtSlot(QTime)
    def on_timeEdit_von_userTimeChanged(self, time):
        """
        Slot documentation goes here.
        
        @param time DESCRIPTION
        @type QTime
        """
        fielditem = QTableWidgetItem("         "+self.timeEdit_von.text()+" - "+self.timeEdit_bis.text())
        self.te_vorschau.setItem(2, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        self.kontrolle()

    @pyqtSlot(QTime)
    def on_timeEdit_bis_timeChanged(self, time):
        """
        Slot documentation goes here.
        
        @param time DESCRIPTION
        @type QTime
        """
        fielditem = QTableWidgetItem("         "+self.timeEdit_von.text()+" - "+self.timeEdit_bis.text())
        self.te_vorschau.setItem(2, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        self.kontrolle()

    
    @pyqtSlot()
    def on_pushButton_hinzufuegen_clicked(self):
        """
        Slot documentation goes here.
        """
        db = Database.get_instance(self)
        sql = "select * from kat_wochenplan WHERE KW = '" + self.parent().te_KW.text() + "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        
        vorschau= self.te_vorschau.item(0, 0).text()+" "+self.te_vorschau.item(1, 0).text()+" "+ self.te_vorschau.item(2, 0).text()+" "+self.te_vorschau.item(3, 0).text()+" "+self.te_vorschau.item(4, 0).text()
        if satz_len == 0:
            try:
                sql = "INSERT INTO kat_wochenplan (KW,"+self.Wochen_Tag.text()+") \
                VALUES (%s,%s)"
                val = (self.parent().te_KW.text()+","+vorschau)
                db.insert(sql,  val)
                print(sql)
                print(val)
                print("ferttttttttttttttttttttttig")
            except:
                print("Fehler")
           # self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugabe 
        else:
            sql = "UPDATE kat_ausbilder set "+self.Wochen_Tag.text()+"=%s where KW ='" + self.parent().te_KW.text()+ "'"
            val = (sql_satz+";"+vorschau)
            # self.INFO("Eintrag wurde in der Datenbank aktualisiert!",  "I")# info asugabe 
            db.insert(sql,  val)
            print("fertig else")
        
    def closeEvent(self, event):
        self.parent().show()
    
    def kontrolle(self):
        #rechner = int(self.timeEdit_von.text()) - int(self.timeEdit_bis.text())
        txt1 = self.timeEdit_von.text()
        txt2 = self.timeEdit_bis.text()
        von = txt1.replace(":", ".")
        bis = txt2.replace(":", ".")
        print(von)
        print(bis)
        gesamt =float(bis) - float(von)
        print(gesamt)
        
        if gesamt < float(self.gesamt_stunden.text()):
                print("")
                self.gesamt_stunden.setStyleSheet("background-color: rgb(255, 048, 048);")
                self.pushButton_hinzufuegen.setEnabled(False)#danach wird der Button enabled

        if gesamt >= float(self.gesamt_stunden.text()):
                print("")                
                self.gesamt_stunden.setStyleSheet("background-color: rgb(000, 255, 127);")
                self.pushButton_hinzufuegen.setEnabled(True)#danach wird der Button enabled
        # TODO: not implemented yet
        #raise NotImplementedError
    @pyqtSlot(str)
    def on_gesamt_stunden_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.kontrolle()

    
    @pyqtSlot(str)
    def on_comboBox_thema3_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Stunden FROM kat_lehrstoff WHERE Ausbildungsthema = "'+ self.comboBox_thema3.currentText()+'"' #select der lkz  wo das land
        
        try: #versuche die combobox zu befüllen
            mycursor = db.select(sql)
           # mycursor.execute(sql)# hier wird der sql befehl ausgeführt
            sql_satz = mycursor.fetchall()# das ist das ergebniss
            mycursor.close()# hier wird der mycursor geschlossen
            satz_len = len (sql_satz)
            if satz_len == 0:           # wenn kein land ausgewählt wurde erscheint ein "?" im entryfiel "LKZ" 
                self.sb_Thema3.setText('0')
            else:
                self.sb_Thema3.setText(str(sql_satz[0][0]))
        except:#falls ein fehler auftauch soll er das machen 
            print("test")
    
    @pyqtSlot(str)
    def on_comboBox_thema1_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Stunden FROM kat_lehrstoff WHERE Ausbildungsthema = "'+ self.comboBox_thema1.currentText()+'"' #select der lkz  wo das land
        
        try: #versuche die combobox zu befüllen
            mycursor = db.select(sql)
           # mycursor.execute(sql)# hier wird der sql befehl ausgeführt
            sql_satz = mycursor.fetchall()# das ist das ergebniss
            mycursor.close()# hier wird der mycursor geschlossen
            satz_len = len (sql_satz)
            if satz_len == 0:           # wenn kein land ausgewählt wurde erscheint ein "?" im entryfiel "LKZ" 
                self.sb_Thema1.setText('0')
            else:
                self.sb_Thema1.setText(str(sql_satz[0][0]))
        except:#falls ein fehler auftauch soll er das machen 
            print("test")
    
    @pyqtSlot(str)
    def on_comboBox_thema2_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION   
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Stunden FROM kat_lehrstoff WHERE Ausbildungsthema = "'+ self.comboBox_thema2.currentText()+'"' #select der lkz  wo das land
        
        try: #versuche die combobox zu befüllen
            mycursor = db.select(sql)
           # mycursor.execute(sql)# hier wird der sql befehl ausgeführt
            sql_satz = mycursor.fetchall()# das ist das ergebniss
            mycursor.close()# hier wird der mycursor geschlossen
            satz_len = len (sql_satz)
            if satz_len == 0:           # wenn kein land ausgewählt wurde erscheint ein "?" im entryfiel "LKZ" 
                self.sb_Thema2.setText('0')
            else:
                self.sb_Thema2.setText(str(sql_satz[0][0]))
        except:#falls ein fehler auftauch soll er das machen 
            print("test")
    
    @pyqtSlot(str)
    def on_sb_Thema1_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        thema1 = int(self.sb_Thema1.text())
        thema2 = int(self.sb_Thema2.text())
        print(thema2)
        thema3 = int(self.sb_Thema3.text())
        print(thema3)
        gesamt = thema1 + thema2 + thema3
        
        self.gesamt_stunden.setText(str(gesamt))
    
    @pyqtSlot(str)
    def on_sb_Thema2_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        thema1 = int(self.sb_Thema1.text())
        thema2 = int(self.sb_Thema2.text())
        print(thema2)
        thema3 = int(self.sb_Thema3.text())
        print(thema3)
        gesamt = thema1 + thema2 + thema3
        
        self.gesamt_stunden.setText(str(gesamt))    
    
    @pyqtSlot(str)
    def on_sb_Thema3_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        thema1 = int(self.sb_Thema1.text())
        thema2 = int(self.sb_Thema2.text())
        print(thema2)
        thema3 = int(self.sb_Thema3.text())
        print(thema3)
        gesamt = thema1 + thema2 + thema3
        
        self.gesamt_stunden.setText(str(gesamt))
