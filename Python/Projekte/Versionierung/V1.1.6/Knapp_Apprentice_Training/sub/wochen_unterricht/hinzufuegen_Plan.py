# -*- coding: utf-8 -*-

"""
Module implementing hinzufügen.
"""

from PyQt5.QtCore import pyqtSlot, QTime
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from other.database import Database
from sub.wochen_unterricht.Ui_hinzufuegen_Plan import Ui_Dialog
from sub.wochen_unterricht.Lehrlings_Tabelle import Lehrlings_Tabelle
from sub.wochen_unterricht.Anwesenheit import anwesenheit

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
        fielditem = QTableWidgetItem("  ")
        self.te_vorschau.setItem(3, 0, fielditem)
        fielditem = QTableWidgetItem("  ")
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
            self.comboBox_Ausbilder.addItems(werte)
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
            self.comboBox_Raum.addItems(werte)
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
    def on_comboBox_Ausbilder_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Vorname FROM kat_ausbilder WHERE Familienname = "'+ self.comboBox_Ausbilder.currentText()+'"' #select der lkz  wo das land
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
            print("")
        #self.te_vorschau.setText(self.te_vorschau.text()+"n/"+self.comboBox_ausbilder.currentText())
        fielditem = QTableWidgetItem(self.comboBox_Unterrichtsthema.currentText()+"  "+ self.comboBox_Ausbilder.currentText())
        self.te_vorschau.setItem(0, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        
    @pyqtSlot(str)
    def on_comboBox_Raum_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Stock, Gebäude FROM kat_raeume WHERE Raum = "'+ self.comboBox_Raum.currentText()+'"' #select der lkz  wo das land
        
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
            print("")
        #self.te_vorschau.setText(self.te_vorschau.text()+"n/"+self.comboBox_raum.currentText())
        fielditem = QTableWidgetItem("         "+self.comboBox_Raum.currentText()+"         ")
        self.te_vorschau.setItem(1, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()

    def Themen1(self):
        
        db = Database.get_instance(self)
        sql = "SELECT Hauptthema, Lehrstoff FROM kat_lehrstoff where Ausbildungsthema ='"+self.comboBox_Unterrichtsthema.currentText()+"'"
        mycursor = db.select(sql)
        try: #versuche die combobox zu befüllen
   
            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0]+"-" +i[1])
            self.comboBox_Thema1.addItems(werte)
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
    
    def Themen2(self):
        
        db = Database.get_instance(self)
        sql = "SELECT Hauptthema, Lehrstoff FROM kat_lehrstoff where Ausbildungsthema ='"+self.comboBox_Unterrichtsthema.currentText()+"'"
        mycursor = db.select(sql)
        try: #versuche die combobox zu befüllen
   
            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0]+"-" +i[1])
            self.comboBox_Thema2.addItems(werte)
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

    def Themen3(self):
        db = Database.get_instance(self)
        sql = "SELECT Hauptthema, Lehrstoff FROM kat_lehrstoff where Ausbildungsthema ='"+self.comboBox_Unterrichtsthema.currentText()+"'"
        mycursor = db.select(sql)
        try: #versuche die combobox zu befüllen
   
            #mycursor.execute("SELECT länder.LAND FROM LÄNDER") # select der länder von der db länder
            werte = []
            for i in mycursor: #befüllung der combobox 
                werte.append(i[0]+"-" +i[1])
            self.comboBox_Thema3.addItems(werte)
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
            

    def Combobox_Thema1_befuellen(self): # hier wird die Combobox lan befüllt
        self.Themen1()
    def Combobox_Thema2_befuellen(self): # hier wird die Combobox lan befüllt
        self.Themen2()
    def Combobox_Thema3_befuellen(self): # hier wird die Combobox lan befüllt
        self.Themen3()

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
        fielditem = QTableWidgetItem(self.comboBox_Unterrichtsthema.currentText()+"  "+ self.comboBox_Ausbilder.currentText())
        self.te_vorschau.setItem(0, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        
        self.Themen1()
        self.Themen2()
        self.Themen3()
        # TODO: not implemented yet
       # raise NotImplementedError
    
    
    def Stunden_abfrage(self):
        txt1 = self.timeEdit_von.text()
        txt2 = self.timeEdit_bis.text()
        von = txt1.replace(":", ".")
        bis = txt2.replace(":", ".")
#        print(von)
#        print(bis)
        gesamt =float(bis) - float(von)
#        print(gesamt)
        
        if gesamt== 0:
            self.pushButton_hinzufuegen.setEnabled(False)#danach wird der Button enabled
            
        if gesamt != 0:
            
            self.pushButton_hinzufuegen.setEnabled(True)#danach wird der Button enabled
    
    @pyqtSlot(QTime)
    def on_timeEdit_von_userTimeChanged(self, time):
        """
        Slot documentation goes here.
        
        @param time DESCRIPTION
        @type QTime
        """
        self.Stunden_abfrage()
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
        self.Stunden_abfrage()
        fielditem = QTableWidgetItem("         "+self.timeEdit_von.text()+" - "+self.timeEdit_bis.text())
        self.te_vorschau.setItem(2, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        self.kontrolle()

    
    @pyqtSlot()
    def on_pushButton_loeschen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Ermittelung_der_Nummer_Des_Tages()
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_wochen_unterricht WHERE Woche = '" + self.parent().label_jahr.text()+self.parent().te_KW.text()+ "' and Tag='"+str(spalte)+"' and Zeile='"+self.Row.text()+"'"
        db.delete(sql)
       # self.cell_tw_anzeige()
        #self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe 
        self.hide()
        self.parent().show()
        self.parent().twData_anzeigen()
        
    
    
    
    @pyqtSlot()
    def on_pushButton_hinzufuegen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Ermittelung_der_Nummer_Des_Tages()
        db = Database.get_instance(self)
        sql = "select * from kat_wochen_unterricht WHERE Woche = '" + self.parent().label_jahr.text()+self.parent().te_KW.text() + "' and Tag='"+str(spalte)+"' and Zeile='"+self.Row.text()+"'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        #vorschau= self.te_vorschau.item(0, 0).text()+"\n "+self.te_vorschau.item(1, 0).text()+"\n "+ self.te_vorschau.item(2, 0).text()+"\n "+self.te_vorschau.item(3, 0).text()+"\n "+self.te_vorschau.item(4, 0).text()
        if satz_len == 0:
            
                #+self.Wochen_Tag.text()+") \
            sql = "INSERT INTO kat_wochen_unterricht (Woche, Tag, Zeile, von_bis, Unterrichtsthema, Ausbilder, Platz_Raum,Klassen,Lehrlinge,Informationen,Ausbildungsthema_1,Ausbildungsthema_2,Ausbildungsthema_3,Benutzer,Aenderung)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val =(self.parent().label_jahr.text()+self.parent().te_KW.text(),str(spalte),self.Row.text(),self.timeEdit_von.text()+"-"+self.timeEdit_bis.text(),self.comboBox_Unterrichtsthema.currentText(),self.comboBox_Ausbilder.currentText(),self.comboBox_Raum.currentText(),self.te_vorschau.item(3, 0).text(),self.te_vorschau.item(4, 0).text(),self.le_information.text(),self.comboBox_Thema1.currentText(),self.comboBox_Thema2.currentText(),self.comboBox_Thema3.currentText(),"root","2020-12-14 09:05:42")
            db.insert(sql,  val)
           # self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugab
            
        else:
            sql = "UPDATE kat_wochen_unterricht set von_bis=%s, Unterrichtsthema=%s, Ausbilder=%s, Platz_Raum=%s,Klassen=%s,Lehrlinge=%s,Informationen=%s,Ausbildungsthema_1=%s,Ausbildungsthema_2=%s,Ausbildungsthema_3=%s,Benutzer=%s,Aenderung=%s WHERE Woche = '" + self.parent().label_jahr.text()+self.parent().te_KW.text() + "' and Tag='"+str(spalte)+"' and Zeile='"+self.Row.text()+"'"
            #sql = "UPDATE kat_ausbilder set "+self.Wochen_Tag.text()+"=%s where KW ='" + self.parent().te_KW.text()+ "'"
            val = (self.timeEdit_von.text()+" - "+self.timeEdit_bis.text(),self.comboBox_Unterrichtsthema.currentText(),self.comboBox_Ausbilder.currentText(),self.comboBox_Raum.currentText(),self.te_vorschau.item(3, 0).text(),self.te_vorschau.item(4, 0).text(),self.le_information.text(),self.comboBox_Thema1.currentText(),self.comboBox_Thema2.currentText(),self.comboBox_Thema3.currentText(),"root","2020-12-14 09:05:42")
            # self.INFO("Eintrag wurde in der Datenbank aktualisiert!",  "I")# info asugabe 
#            print("Unterricht: "+self.comboBox_Unterrichtsthema.currentText())
#            print(self.comboBox_Thema1.currentText())
            db.insert(sql,  val)


       # mycursor.close()
        self.hide()
        self.parent().show()
        self.parent().twData_anzeigen()


    def Ermittelung_der_Nummer_Des_Tages(self):
        global spalte
        if self.Wochen_Tag.text() == "Montag":
            spalte=1
        if self.Wochen_Tag.text() == "Dienstag":
            spalte=2        
        if self.Wochen_Tag.text() == "Mittwoch":
            spalte=3        
        if self.Wochen_Tag.text() == "Donnerstag":
            spalte=4        
        if self.Wochen_Tag.text() == "Freitag":
            spalte=5
    
    
    
    def closeEvent(self, event):
        self.parent().show()
    
    def kontrolle(self):
        #rechner = int(self.timeEdit_von.text()) - int(self.timeEdit_bis.text())
        txt1 = self.timeEdit_von.text()
        txt2 = self.timeEdit_bis.text()
        von = txt1.replace(":", ".")
        bis = txt2.replace(":", ".")
#        print(von)
#        print(bis)
        gesamt =float(bis) - float(von)
#        print(gesamt)
        
        if gesamt < float(self.gesamt_stunden.text()):
                print("")
                self.gesamt_stunden.setStyleSheet("background-color: rgb(255, 048, 048);")
               # self.pushButton_hinzufuegen.setEnabled(False)#danach wird der Button enabled

        if gesamt >= float(self.gesamt_stunden.text()):
                print("")                
                self.gesamt_stunden.setStyleSheet("background-color: rgb(000, 255, 127);")
                #self.pushButton_hinzufuegen.setEnabled(True)#danach wird der Button enabled
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
    def on_comboBox_Thema3_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Stunden FROM kat_lehrstoff WHERE Ausbildungsthema = "'+ self.comboBox_Thema3.currentText()+'"' #select der lkz  wo das land
        
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
            print("")
    
    @pyqtSlot(str)
    def on_comboBox_Thema1_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        split1, split2 = self.comboBox_Thema1.currentText().split("-")
        
        db = Database.get_instance(self)
        sql = 'SELECT Stunden FROM kat_lehrstoff WHERE Hauptthema = "'+ split1+'" and Lehrstoff="'+split2+'"' #select der lkz  wo das land
        
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
    def on_comboBox_Thema2_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION   
        @type str
        """
        db = Database.get_instance(self)
        sql = 'SELECT Stunden FROM kat_lehrstoff WHERE Ausbildungsthema = "'+ self.comboBox_Thema2.currentText()+'"' #select der lkz  wo das land
        
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
            print("")
    
    @pyqtSlot(str)
    def on_sb_Thema1_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        thema1 = int(self.sb_Thema1.text())
        thema2 = int(self.sb_Thema2.text())
        thema3 = int(self.sb_Thema3.text())
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
        thema3 = int(self.sb_Thema3.text())
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
        thema3 = int(self.sb_Thema3.text())
        gesamt = thema1 + thema2 + thema3
        
        self.gesamt_stunden.setText(str(gesamt))
    


            
        # TODO: not implemented yet
       # raise NotImplementedError
    
    def Checkbox_unchecked(self):
        print("")
        txt1 = self.timeEdit_von.text()
        txt2 = self.timeEdit_bis.text()
        von = txt1.replace(":", ".")
        bis = txt2.replace(":", ".")
#        print(von)
#        print(bis)
        gesamt =float(bis) - float(von)        
    

    
    def C_1A_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 1A")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        
    def C_2A_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 2A")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    def C_3A_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 3A")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        
    def C_4A_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 4A")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()        
        
    def C_1B_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 1B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        
    def C_2B_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 2B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
    
    def C_3B_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 3B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        
    def C_4B_checked(self):
        fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" 4B")
        self.te_vorschau.setItem(3, 0, fielditem)
        self.te_vorschau.resizeColumnsToContents()
        self.te_vorschau.resizeRowsToContents()
        

#        if self.checkBox_1A.isChecked()==False:
#            text =self.te_vorschau.item(3,  0).text()
#            x = text.split(", ")
#            print(x)
#            print(str(x[0]))
#            text =  x[0].replace("1A", "")  
#            for z in x : 
#                test =str(test) + str(x[z])
#            text= str(test)
#            fielditem = QTableWidgetItem(text)
#            self.te_vorschau.setItem(3, 0, fielditem)
#    

        # TODO: not implemented yet
        #raise NotImplementedError
#    
    def if_checked(self):
        fielditem = QTableWidgetItem("")
        self.te_vorschau.setItem(3, 0, fielditem)

        if self.checkBox_MB.isChecked()== False:
            self.checkBox_1A_3.setEnabled(False)
            self.checkBox_2A_3.setEnabled(False)
            self.checkBox_1B_3.setEnabled(False)
            self.checkBox_2B_3.setEnabled(False)
            self.checkBox_3A_3.setEnabled(False)
            self.checkBox_4A_3.setEnabled(False)
            self.checkBox_3B_3.setEnabled(False)
            self.checkBox_4B_3.setEnabled(False)  
            self.checkBox_MB.setChecked(False)
            self.checkBox_1A_3.setChecked(False)
            self.checkBox_2A_3.setChecked(False)
            self.checkBox_1B_3.setChecked(False)
            self.checkBox_2B_3.setChecked(False)
            self.checkBox_3A_3.setChecked(False)
            self.checkBox_4A_3.setChecked(False)
            self.checkBox_3B_3.setChecked(False)
            self.checkBox_4B_3.setChecked(False)  
        if self.checkBox_MB.isChecked()== True:
            fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" MB:")
            self.te_vorschau.setItem(3, 0, fielditem)
            self.te_vorschau.resizeColumnsToContents()
            self.te_vorschau.resizeRowsToContents()
            
            self.checkBox_1A_3.setEnabled(True)
            self.checkBox_2A_3.setEnabled(True)
            self.checkBox_1B_3.setEnabled(True)
            self.checkBox_2B_3.setEnabled(True)
            self.checkBox_3A_3.setEnabled(True)
            self.checkBox_4A_3.setEnabled(True)
            self.checkBox_3B_3.setEnabled(True)
            self.checkBox_4B_3.setEnabled(True)  
            if self.checkBox_1A_3.isChecked()== True:
                self.C_1A_checked()
            if self.checkBox_1B_3.isChecked()== True:
                self.C_1B_checked()
            if self.checkBox_2B_3.isChecked()== True:
                self.C_2B_checked()
            if self.checkBox_2A_3.isChecked()== True:
                self.C_2A_checked()
            if self.checkBox_3A_3.isChecked()== True:
                self.C_3A_checked()
            if self.checkBox_3B_3.isChecked()== True:
                self.C_3B_checked()
            if self.checkBox_4A_3.isChecked()== True:
                self.C_4A_checked()
            if self.checkBox_4B_3.isChecked()== True:
                self.C_4B_checked()            

     
        
        if self.checkBox_ME.isChecked()== False:
            self.checkBox_1A_2.setEnabled(False)
            self.checkBox_2A_2.setEnabled(False)
            self.checkBox_1B_2.setEnabled(False)
            self.checkBox_2B_2.setEnabled(False)
            self.checkBox_3A_2.setEnabled(False)
            self.checkBox_4A_2.setEnabled(False)
            self.checkBox_3B_2.setEnabled(False)
            self.checkBox_4B_2.setEnabled(False) 
            self.checkBox_ME.setChecked(False)
            self.checkBox_1A_2.setChecked(False)
            self.checkBox_2A_2.setChecked(False)
            self.checkBox_1B_2.setChecked(False)
            self.checkBox_2B_2.setChecked(False)
            self.checkBox_3A_2.setChecked(False)
            self.checkBox_4A_2.setChecked(False)
            self.checkBox_3B_2.setChecked(False)
            self.checkBox_4B_2.setChecked(False) 
        if self.checkBox_ME.isChecked()== True:
            fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" ME:")
            self.te_vorschau.setItem(3, 0, fielditem)
            self.te_vorschau.resizeColumnsToContents()
            self.te_vorschau.resizeRowsToContents()
            
            self.checkBox_1A_2.setEnabled(True)
            self.checkBox_2A_2.setEnabled(True)
            self.checkBox_1B_2.setEnabled(True)
            self.checkBox_2B_2.setEnabled(True)
            self.checkBox_3A_2.setEnabled(True)
            self.checkBox_4A_2.setEnabled(True)
            self.checkBox_3B_2.setEnabled(True)
            self.checkBox_4B_2.setEnabled(True)   
            if self.checkBox_1A_2.isChecked()== True:
                self.C_1A_checked()
            if self.checkBox_1B_2.isChecked()== True:
                self.C_1B_checked()
            if self.checkBox_2A_2.isChecked()== True:
                self.C_2A_checked()
            if self.checkBox_2B_2.isChecked()== True:
                self.C_2B_checked()
            if self.checkBox_3A_2.isChecked()== True:
                self.C_3A_checked()
            if self.checkBox_3B_2.isChecked()== True:
                self.C_3B_checked()
            if self.checkBox_4A_2.isChecked()== True:
                self.C_4A_checked()
            if self.checkBox_4B_2.isChecked()== True:
                self.C_4B_checked()
            
        if self.checkBox_APP.isChecked()== False:
            self.checkBox_1A.setEnabled(False)
            self.checkBox_2A.setEnabled(False)
            self.checkBox_1B.setEnabled(False)
            self.checkBox_2B.setEnabled(False)
            self.checkBox_3A.setEnabled(False)
            self.checkBox_4A.setEnabled(False)
            self.checkBox_3B.setEnabled(False)
            self.checkBox_4B.setEnabled(False)           
            self.checkBox_APP.setChecked(False)
            self.checkBox_1A.setChecked(False)
            self.checkBox_2A.setChecked(False)
            self.checkBox_1B.setChecked(False)
            self.checkBox_2B.setChecked(False)
            self.checkBox_3A.setChecked(False)
            self.checkBox_4A.setChecked(False)
            self.checkBox_3B.setChecked(False)
            self.checkBox_4B.setChecked(False)           
        if self.checkBox_APP.isChecked()== True:
            fielditem = QTableWidgetItem(self.te_vorschau.item(3,  0).text()+" APP:")
            self.te_vorschau.setItem(3, 0, fielditem)
            self.te_vorschau.resizeColumnsToContents()
            self.te_vorschau.resizeRowsToContents()
            
            self.checkBox_1A.setEnabled(True)
            self.checkBox_2A.setEnabled(True)
            self.checkBox_1B.setEnabled(True)
            self.checkBox_2B.setEnabled(True)
            self.checkBox_3A.setEnabled(True)
            self.checkBox_4A.setEnabled(True)
            self.checkBox_3B.setEnabled(True)
            self.checkBox_4B.setEnabled(True)
            if self.checkBox_1A.isChecked()== True:
                self.C_1A_checked()            
            if self.checkBox_1B.isChecked()== True:
                self.C_1B_checked()
            if self.checkBox_2A.isChecked()== True:
                self.C_2A_checked()
            if self.checkBox_2B.isChecked()== True:
                self.C_2B_checked()
            if self.checkBox_3A.isChecked()== True:
                self.C_3A_checked()
            if self.checkBox_3B.isChecked()== True:
                self.C_3B_checked()
            if self.checkBox_4A.isChecked()== True:
                self.C_4A_checked()
            if self.checkBox_4B.isChecked()== True:
                self.C_4B_checked()

    @pyqtSlot(int)
    def on_checkBox_ME_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        for x in range (3):
            self.if_checked()
        
    @pyqtSlot(int)
    def on_checkBox_APP_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        for x in range (3):
            self.if_checked()
        
    @pyqtSlot(int)
    def on_checkBox_MB_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        for x in range (3):
            self.if_checked()
       # self.if_checked()
       # self.if_checked()
    @pyqtSlot(int)
    def on_checkBox_1A_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
    @pyqtSlot(int)
    def on_checkBox_1B_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
    @pyqtSlot(int)
    def on_checkBox_2A_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
    @pyqtSlot(int)
    def on_checkBox_2B_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
    @pyqtSlot(int)
    def on_checkBox_3A_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
    
    @pyqtSlot(int)
    def on_checkBox_3B_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
    @pyqtSlot(int)
    def on_checkBox_4A_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
        
    @pyqtSlot(int)
    def on_checkBox_4B_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
        
    @pyqtSlot(int)
    def on_checkBox_1B_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
        
    @pyqtSlot(int)
    def on_checkBox_2A_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()

    @pyqtSlot(int)
    def on_checkBox_2B_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()



    @pyqtSlot(int)
    def on_checkBox_3A_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()



    @pyqtSlot(int)
    def on_checkBox_3B_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
        
    @pyqtSlot(int)
    def on_checkBox_4A_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()



    @pyqtSlot(int)
    def on_checkBox_4B_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()



    @pyqtSlot(int)
    def on_checkBox_1A_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
    
    @pyqtSlot(int)
    def on_checkBox_1B_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()


    @pyqtSlot(int)
    def on_checkBox_2A_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()



    @pyqtSlot(int)
    def on_checkBox_2B_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()


    @pyqtSlot(int)
    def on_checkBox_3A_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()


    @pyqtSlot(int)
    def on_checkBox_3B_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()


    @pyqtSlot(int)
    def on_checkBox_4A_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()



    @pyqtSlot(int)
    def on_checkBox_4B_3_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()


    @pyqtSlot(int)
    def on_checkBox_1A_2_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        self.if_checked()
    
    @pyqtSlot()
    def on_pushButton_Anwesenheit_clicked(self):
        """
        Slot documentation goes here.
        """
        w = anwesenheit(self)
        w.show()#Öffnen das SettingGui
        self.hide()#hide the current window
