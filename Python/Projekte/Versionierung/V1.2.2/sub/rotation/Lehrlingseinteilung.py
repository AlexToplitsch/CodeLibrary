# -*- coding: utf-8 -*-

"""
Module implementing Lehrlingseinteilung_App.
"""

#---------------------------------PyQt und Dialog imports-----------------------------------------
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QMessageBox
from sub.rotation.Ui_Lehrlingseinteilung import Ui_Lehrlingseinteilung
#-------------------------------andere imports------------------------------------------------------
from other.database import Database
import datetime
import re




class Lehrlingseinteilung_App(QDialog, Ui_Lehrlingseinteilung):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrlingseinteilung_App, self).__init__(parent)
        self.setupUi(self)
        
        self.actualDate = str(datetime.datetime.now().date())
        self.date1 = int(self.actualDate[:4])
        self.date2 = self.date1 -1
        self.lehrlingIndex = 0
        self.aw = 1
        self.cB_Lehrling_Befüllen()
        self.cB_Fachabteilung_Befüllen()
        self.sqlBefehl = ""
        self.sqlBefehlVal = ""
        self.val = []
        
        
    
    @pyqtSlot()
    def on_pB_leftArrow_clicked(self):
        """
        Dekrementiert das Datums des Labels "lbl_Ausbildungsjahr"
        Übergabeparameter: keine
        Rückgabewert: void
        """
        self.date1 -= 1
        self.date2 -= 1
        self.lbl_Ausbildungjahr.setText(str(self.date2) +"/" + str(self.date1))
        self.setCursor(Qt.WaitCursor)
        self.tableWidget_Anzeige()
        self.setCursor(Qt.ArrowCursor)
        
        
        
    @pyqtSlot()
    def on_pB_rightArrow_clicked(self):
        """
        Inkrementiert die Datums des Labels "lbl_Ausbildungsjahr"
        Übergabeparameter: keine
        Rückgabewert: void
        """
        self.date1 += 1
        self.date2 += 1
        self.lbl_Ausbildungjahr.setText(str(self.date2) +"/" + str(self.date1))
        self.setCursor(Qt.WaitCursor)
        self.tableWidget_Anzeige()
        self.setCursor(Qt.ArrowCursor)
    
    
    
    @pyqtSlot(int)
    def on_sB_Ausbildungswoche_valueChanged(self, p0):
        """
        Funktion um die Variable self.aw und das maximum der Spinbox sb_Dauer immer zu aktualisieren
        
        @param p0 Wert der Spinbox
        @type int
        """
        if 33 < p0 and p0 < 54:
            self.aw = p0 - 33
        else:
            self.aw = p0 + 20
        
        if p0 >= 1 and p0 <= 33:
            self.sB_Dauer.setMaximum(34 - p0)
        else:
            self.sB_Dauer.setMaximum(53 - (p0-34) )
    
    
    
    @pyqtSlot(str)
    def on_cB_Lehrling_currentTextChanged(self, p0):
        """
        Bei der Änderung vom Lehrling, wird der gespeicherte SQL-Befehl mit der zugehörigen Variable "val" gelöscht        
        @param p0 Vorname, Nachname und Personalnummer des Lehrlings
        @type str
        """
        self.sqlBefehl = ""
        self.val = []       
        self.tableWidget_Anzeige()
    
    
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        pass
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        pass
    
    
    
    @pyqtSlot()
    def on_pB_Speichern_clicked(self):
        """
        Speichert einen Eintrag aus den Daten den Comboboxen "cB_Lehrling" und "cB_"
        """
        self.sqlBefehl = self.sqlBefehl[:-2]
        self.sqlBefehlVal = self.sqlBefehlVal[:-2]
        
#--------------------------------------- überprüfung ob in den Comboboxen Wert ausgeählt wurden -----------------------------------------------------------
        if self.cB_Lehrling.currentText() == "Alle Anzeigen":
            self.INFO("Bei Lehrling wurde nichts ausgewählt!",  "H")
            return
        if self.cB_Fachabteilung.currentText() == "Alle Anzeigen":
            self.INFO("Bei Fachabteilung wurde nichts ausgewählt!",  "H")
            return
#---------------------------------------------------------------------------------------datentabelle befüllen-------------------------------------------------------------------------
        db = Database.get_instance(self)
        sql = "select * from kat_einteilung WHERE Personalnummer = '" + str(self.cB_Lehrling.itemData(self.cB_Lehrling.currentIndex())) + '" AND Ausbildungsjahr = "' + self.lbl_Ausbildungjahr.text() + "'"
        mycursor = db.select(sql)
        
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        self.sqlBefehlVal = self.buildSQL_val()
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        if satz_len == 0:
            try:
                sql = "INSERT INTO kat_einteilung (Lehrling, Personalnummer, Beruf, Lehrjahr, Berufsschule, Ausbildungsjahr" + self.sqlBefehl +" ) VALUES (%s, %s, %s, %s, %s, %s"+ self.sqlBefehlVal+")" 
                val = self.setPermaVal() + self.val
                self.INFO("Eintrag wurde in die Datenbank gespeichert",  "I")
                mycursor = db.insert(sql, tuple(val))

            except Exception:
                self.INFO("Eintrag konnte nicht in die Datenbank gespeichert werden",  "F")

        else:
            try:
                sql = "UPDATE kat_einteilung set (" + self.sqlBefehl + " ) VALUES (" + self.sqlBefehlVal +" ) WHERE Personalnummer = '" + str(self.cB_Lehrling.itemData(self.cB_Lehrling.currentIndex())) + '" AND Ausbildungsjahr = "' + self.lbl_Ausbildungjahr.text() + "'"
                self.INFO("Eintrag wurde in der Datenbank aktualisiert." ,  "I")               

                mycursor = db.insert(sql, tuple(self.val))
                
            except Exception as e:
                print(e)
                self.INFO("Eintrag konnte nicht in der Datenbank aktualisiert werden." ,  "F")

        
        if mycursor == "backtologin":
            self.back_to_login()
            return
        self.sqlBefehl = ""
        self.sqlBefehlVal = ""
        self.val = []
        self.tableWidget_Anzeige()
    
    
    
    @pyqtSlot()
    def on_pB_Abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().show()
        self.close()
    
    
    
    @pyqtSlot()
    def on_pB_Hilfe_clicked(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(
        self,
        self.tr("Hilfe"),
        self.tr("""Die Hilfefunktion wird demnächst Hinzugefügt!"""))
        
        
        
    @pyqtSlot()
    def on_pB_Hinzufuegen_clicked(self):
        """
        Hier
        """
        if self.cB_Fachabteilung.currentText() == "Alle Anzeigen":
            self.INFO("Bei Fachabteilung wurde nichts ausgewählt",  "H")
            return
        if self.cB_Lehrling.currentText() == "Alle Anzeigen":
            self.INFO("Bei Lehrling wurde nichts ausgewählt",  "H")
            return
        self.buildSQL_val()
        self.buildSQLBefehl()
        print(self.sqlBefehl)
        print(self.sqlBefehlVal)
        print(tuple(self.val))

    
    
    def setAusbildungswoche(self,  woche): #woche fängt bei 6 an weil Spaltennummer
        """
        Nimmt die Spaltennummer des Tablewidget der Lehrlingseinteilungstabelle und setzt den Wert 
        der Spinbox "sB_Ausbildungswoche" auf die entsprechende KW (der faktor für das umrechnen von aw auf kw soll in config file passieren)
        @param woche Spaltennummer des Tablewidget
        @type int
        @return void
        """
        if woche < 6:
            self.aw = 1
            kw =34
        else:
            kw = woche +28
            self.aw = woche - 5
        if kw > 53:
            kw = kw - 53
        self.sB_Ausbildungswoche.setValue(kw) 
        
        
        
    def setZeile(self,  name):
        """
        Nimmt Namen aus dem Tablewidget der Lehrlingseinteilungstabelle und setzt den Text in cB_Lehrling 
        @param name Name des Lehrlings aus dem Tablewidget
        @type string
        
        @return void
        """
        print(name)
        self.cB_Lehrling.setCurrentText(name)
        
        
        
    def cB_Lehrling_Befüllen(self):
        """
        Combobox "cB_Lehrling" wird mit den Daten aus den Spalten Personalnummer, Vorname und Nachname
        aus der kat_lehrlinge Tabelle befüllt
        """
        #----------------cb_Lehrling aus kat_lehrlinge befüllen -----------------------#
        try:
            db = Database.get_instance(self)
            sql = "SELECT Vorname, Nachname, Personalnummer from kat_lehrlinge"
            mycursor = db.select(sql)
            
            if mycursor == "backtologin":
                self.back_to_login()
                return
                
            rows = mycursor.fetchall()
            self.cB_Lehrling.addItem("Alle Anzeigen")
            for i in rows:
                self.cB_Lehrling.addItem(i[0] + " " + i[1] + ": " + str(i[2]),  str(i[2]))
                
        except Exception:
            self.INFO("cB_Lehrlinge konnte nicht befüllt werden",  "F")
        
    
    
    def cB_Fachabteilung_Befüllen(self):
        try:
            db = Database.get_instance(self)
            sql = "SELECT FachabteilungAbk, FachabteilungBez from kat_fachabteilungen"
            mycursor = db.select(sql)
            
            if mycursor == "backtologin":
                self.back_to_login()
                return
                
            rows = mycursor.fetchall()
            self.cB_Fachabteilung.addItem("Alle Anzeigen")
            for i in rows:
                self.cB_Fachabteilung.addItem(i[1],  i[0])
                
        except Exception:
            self.INFO("cB_Lehrlinge konnte nicht befüllt werden",  "F")
        
        
        
        
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
    
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")



    def buildSQLBefehl(self):
        """
        erstellt je nachdem wie hoch der Wert von der Spinbox "sB_Dauer" ist, einen SQL befehl mit der richtigen Anzahl an werten
        und returned diesen
        
        @return str
        """
        if self.sqlBefehl != "":
            sql_ausbildungswochen = ", "
        else:
            sql_ausbildungswochen = ""
        #-------------------------------------------Überprüfung ob in dem string self.sqlBefehl die AW[i] schon vorhanden ist--------------------------------------------
        for i in range(len(self.sqlBefehl)):
            if self.sqlBefehl[i] == str(self.aw):
                res = QMessageBox.question(
                    self,
                    self.tr(""),
                    self.tr("Die ausgewählte Kalenderwoche: " + str(self.sB_Ausbildungswoche.value()) +" mit der zugehörigen Dauer: "+ str(self.sB_Dauer.value()) +" überschneidet sich mit einem bereits hinzugefügtem Eintrag. ÜBERSCHREIBEN?"),
                    QMessageBox.StandardButtons(
                        QMessageBox.No |
                        QMessageBox.Yes),
                    QMessageBox.No)
                if res == QMessageBox.No:
                    print("Nicht Überschreiben")
                    return
                else: #hier wird der sql Befehl und die zugehörigen values richtig zugeschnitte wenn der Befehl überschrieben werden muss
                    try:
                        self.sqlBefehl = self.sqlBefehl[:i-2] + self.sqlBefehl[i-2+(self.sB_Dauer.value() * 5):]
                    except Exception:
                        self.sqlBefehl = self.sqlBefehl[:i-2]
                    print("Überschreiben") 
        for i in range(self.aw,  self.aw + self.sB_Dauer.value()):
            sql_ausbildungswochen = sql_ausbildungswochen + "AW" + str(i) + ", " 

        self.sqlBefehl += sql_ausbildungswochen
        
        
        
    def buildSQL_val(self):
        res = len(re.findall('(?= AW)', self.sqlBefehl))
        if res != 0:
            for i in  range(0, res +1):
                if i == res:
                    self.sqlBefehlVal += "%s"
                    break
                self.sqlBefehlVal +="%s, "
            
        
        
    def setPermaVal(self):
        try:
            #--------------------------------------------Setzen der ersten fünf Fix-Werte der val Variable ------------------------------------------------------
            db = Database.get_instance(self)
            sql = "SELECT Vorname, Nachname, Personalnummer, Lehrberuf, Lehrbeginn from kat_lehrlinge where Personalnummer = '"  + str(self.cB_Lehrling.itemData(self.cB_Lehrling.currentIndex())) +"'"
            mycursor = db.select(sql)
            
            if mycursor == "backtologin":
                self.back_to_login()
                return
                
            lehrlingsdaten = mycursor.fetchall()
            lehrling = str(lehrlingsdaten[0][0]) + str(lehrlingsdaten[0][1])
            personalnummer = str(lehrlingsdaten[0][2])
            lehrberuf = str(lehrlingsdaten[0][3])
            lehrjahr = str(self.getLehrjahr(str(lehrlingsdaten[0][4])))
            
            #--------------------------------------------Setzen der letzten drei Fix-Werte der val Variable ------------------------------------------------------
            db = Database.get_instance(self)
            sql = "SELECT VonDatum, BisDatum from kat_berufsschulzeit where PERS_NR = '"  + str(self.cB_Lehrling.itemData(self.cB_Lehrling.currentIndex())) +"'"
            mycursor = db.select(sql)
            
            if mycursor == "backtologin":
                self.back_to_login()
                return
                
            berufsschuldaten = mycursor.fetchall()
            berufsschule = str(berufsschuldaten[0][0]) + " - " + str(berufsschuldaten[0][1])
            ausbildungsjahr = self.lbl_Ausbildungjahr.text()
            
        except Exception as e:
            print(e)
            self.INFO("Werte konnten nicht aus der kat_berufsschulzeiten und/oder kat_lehrlinge gesammelt werden",  "F")
            return
        
        #------------------------------------------------------------------------Erstellen der val Variable---------------------------------------------------------------------------------------------------------------------
        val = [lehrling,  int(personalnummer),  lehrberuf,  int(lehrjahr), berufsschule,  ausbildungsjahr]  
        return val
        
        
        
    def buildVal(self):
        """
        erstellt je nachdem wie hoch der Wert von der Spinbox "sB_Dauer" ist, die val variable für den SQL-Befehl mit der richtigen Anzahl an werten
        und returned diesen
        
        @param dauer Dauer des Turnus
        @type int
        
        @return str
        """
        for i in range(0,  self.sB_Dauer.value()):
            self.val.append(self.cB_Fachabteilung.currentText())
        
        
        
    def getLehrjahr(self,  eintrittsdatum):
        eintritt_jahr = str(eintrittsdatum)[:4]
        eintritt_monat = str(eintrittsdatum)[5:7]
        eintritt_tag = str(eintrittsdatum)[8:10]
        dt_now = str(datetime.datetime.now())
        dt_jahr = dt_now[:4]
        dt_monat = dt_now[5:7]
        dt_tag = dt_now[8:10]
        LJ = int(dt_jahr) - int(eintritt_jahr)
        if int(eintritt_monat) < int(dt_monat):
            LJ += 1
        elif int(eintritt_monat) == int(dt_monat) and int(eintritt_tag) <= int(dt_tag):
            LJ += 1
        return LJ
            
    
    
    def tableWidget_Anzeige(self):
        pass



    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()

       
       
    def keyPressEvent(self,  event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
