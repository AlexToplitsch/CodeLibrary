# -*- coding: utf-8 -*-

"""
Module implementing Lehrlingseinteilung_App.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QMessageBox

import datetime
from other.database import Database
import tkinter as tk
from tkinter import messagebox
import os, time
import datetime
from pyreportjasper import JasperPy

from sub.rotation.Ui_Lehrlingseinteilung import Ui_Lehrlingseinteilung


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
        #self.twData_anzeigen()
        
        
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
        #self.twData_anzeigen()
    
    @pyqtSlot(str)
    def on_cB_Lehrling_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        pass
    
    @pyqtSlot(str)
    def on_cB_Fachabteilung_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pB_Speichern_clicked(self):
        """
        
        @return void
        """
        if self.cB_Lehrling.currentText() == "Alle Anzeigen":
            self.INFO("Bei Lehrling wurde nichts ausgewählt!",  "H")
            return
        if self.cB_Fachabteilung.currentText() == "Alle Anzeigen":
            self.INFO("Bei Fachabteilung wurde nichts ausgewählt!",  "H")
            return
        #datentabelle befüllen
        db = Database.get_instance(self)
        sql = "select * from kat_einteilung WHERE Personalnummer = '" + self.cB_Lehrling.itemData(self.cB_Lehrling.currentIndex()) + '" AND Ausbildungsjahr = "' + self.lbl_Ausbildungjahr.text() + "'"
        mycursor = db.select(sql)
        
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        if satz_len == 0:
            try:
                sql = "INSERT INTO '" + self.buildSQLBefehl(self.sB_Dauer.value()) +"'"
    
                self.INFO("Eintrag wurde in die Datenbank gespeichert",  "I")
                self.clearFields()
                
            except Exception:
                self.INFO("Eintrag konnte nicht in die Datenbank gespeichert werden",  "F")

        else:
            try:
                sql = "UPDATE '" + self.buildSQLBefehl(self.sB_Dauer.value()) + "' WHERE Fachrichtung = '" + self.cB_Fachrichtung.currentText() + "' AND Themen_ID = '" + self.le_Themen_ID.text() + "'"
                
                self.INFO("Eintrag wurde in der Datenbank aktualisiert." ,  "I")
                self.clearFields()
                
            except Exception:
                self.INFO("Eintrag konnte nicht in der Datenbank aktualisiert werdeb." ,  "F")

        mycursor = db.insert(sql, val)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        self.tW_Db_Themenkatalog_Anzeigen()
    
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
        Slot documentation goes here.
        """
        pass
    
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
        print(self.aw)
        if kw > 53:
            kw = kw - 53
        self.sB_Ausbildungswoche.setValue(kw) 
        
    def setZeile(self,  zeile):
        """
        Nimmt die Zeilennummer des Tablewidget der Lehrlingseinteilungstabelle und übergibt diese wieder
        @param zeile Zeilennummer des Tablewidget
        @type int
        
        @return void
        """
        self.lehrlingIndex = zeile + 1
        self.cB_Lehrling.setCurrentIndex(self.lehrlingIndex)
        
        
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
        
    
    
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
    
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")

    def buildSQLBefehl(self, dauer):
        """
        erstellt je nachdem wie hoch der Wert von der Spinbox "sB_Dauer" ist, einen SQL befehl mit der richtigen Anzahl an werten
        und returned diesen
        
        @param dauer Dauer des Turnus
        @type int
        
        @return str
        """
        sql_ausbildungswochen = ""
        sql_values = ""
        for i in range(self.aw,  dauer + 1):
            sql_ausbildungswochen = sql_ausbildungswochen + ", AW" + str(i) 
            sql_values = sql_values + ", %s"
        
        sql = "kat_einteilung (Lehrling, Personalnummer, Beruf, Lehrjahr, Berufsschule, Ausbildungsjahr" + sql_ausbildungswochen +") VALUES (%s, %s, %s, %s, %s, %s" + sql_values + ")"
        print(sql)
        
        
        
