# -*- coding: utf-8 -*-

"""
Module implementing Lehrstoff.
"""
from sub.XML.XML_Class import DBtoXML 
from PyQt5 import *
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import  *
from other.database import Database
from tkinter import messagebox
import tkinter as tk
import time
import os
from pyreportjasper import JasperPy
from sub.learningcontent.Ui_Lehrstoff import Ui_Dialog
from sub.learningcontent.LehrstoffSuchen import Lehrstoff_Suche



class Lehrstoff(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        
        
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrstoff, self).__init__(parent)
        self.setupUi(self)
        self.combobox_befüllen()
        self.tW_Datenbank_Anzeigen()
        self.referenz_cB_befüllen()
                   
    @pyqtSlot()
    def on_pB_Abbrechen_clicked(self):
        
        """
        Methode um Lehrstofffenster zu schließen und Hauptmenufenster zu öffnen
        """
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pB_Speichern_clicked(self):
        
        
        """
        Methode um DB-Tabelle kat_lehrstoff zu befüllen oder zu aktualisieren
        """
        if self.cB_Ausbildungsthema.currentText() == "Alle Anzeigen":
            self.INFO("Bei 'Ausbildungsthema' wurde nichts ausgewählt!",  "H")
            return
        if self.cB_Verantwortlicher.currentText() == "Alle Anzeigen":
            self.INFO("Bei 'Verantwortlichr' wurde nichts ausgewählt!",  "H")
            return
        
        #datentabelle befüllen
        db = Database.get_instance(self)
        sql =  "select * from kat_lehrstoff WHERE Ausbildungsthema = '" + self.cB_Ausbildungsthema.currentText() + "' AND Lehrstoff_ID = '" +self.le_Lehrstoff_ID.text()+"'"
        mycursor = db.select(sql)
        
        if mycursor == "backtologin":
            self.back_to_login()
            return
        
        sql_satz = []
        sql_satz =  mycursor.fetchall()
        satz_len = len(sql_satz)
        
        if satz_len == 0:
            try:
                sql = "INSERT INTO kat_lehrstoff (Ausbildungsthema, Lehrstoff_ID, Hauptthema, Lehrstoff, Verantwortlicher, Dokument, Stunden, Hilfsmittel, LAPThemenID, Benutzer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.cB_Ausbildungsthema.currentText(),  self.le_Lehrstoff_ID.text(), self.le_Hauptthema.text(),  self.le_Lehrstoff.text(), self.cB_Verantwortlicher.currentText(), self.le_Dokument.text(),  self.sB_Stunden.value(), self.le_Hilfsmittel.text(), self.cB_Reference.itemData(self.cB_Reference.currentIndex()), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in die Datenbank gespeichert",  "I")
                db.insert(sql, val)
                self.clearFields()
            except Exception:
                self.INFO("Eintrag konnte nicht gespeichert werden!",  "F")
        else:
            try:    
                sql = "UPDATE kat_lehrstoff set Hauptthema=%s, Lehrstoff=%s, Verantwortlicher=%s, Dokument=%s, Stunden=%s, Hilfsmittel=%s, LAPThemenID=%s, Benutzer=%s" + " WHERE Ausbildungsthema='" + self.cB_Ausbildungsthema.currentText() + "' AND Lehrstoff_ID='" + self.le_Lehrstoff_ID.text()+"'"
                val = (self.le_Hauptthema.text(), self.le_Lehrstoff.text(), self.cB_Verantwortlicher.currentText(), self.le_Dokument.text(),  self.sB_Stunden.value(), self.le_Hilfsmittel.text(),  self.cB_Reference.itemData(self.cB_Reference.currentIndex()), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in der Datenbank aktualisiert." ,  "I")
                db.insert(sql, val)
                self.clearFields()
            except Exception:
                self.INFO("Eintrag konnte nicht aktualisiert werden!",  "F")

        self.tW_Datenbank_Anzeigen()

    @pyqtSlot()
    def on_pB_Loeschen_clicked(self):

        
        """
        Methode um ausgewählte Zeile aus DB-Tabelle zu löschen
        """
        db = Database.get_instance(self)
        try:
            sql = "DELETE FROM kat_lehrstoff WHERE Ausbildungsthema='" + self.cB_Ausbildungsthema.currentText()+ "'AND Lehrstoff_ID = '" + self.le_Lehrstoff_ID.text() + "'"
            db.delete(sql)
            self.tW_Datenbank_Anzeigen()
            self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht.",  "I")
        except Exception:
            self.INFO("Ausgewählter Eintrag konnte nicht aus der Datenbank gelöscht werden.",  "F")

    
    @pyqtSlot()
    def on_pB_Hilfe_clicked(self):
        
        """
        Slot documentation goes here
        """
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Hilfe",  "Die Hilfe-Funktion wird in kürze hinzugefügt!")
        
    
    @pyqtSlot(int, int)
    def on_tW_Datenbank_cellClicked(self, row, column):
        
        
        """
        Methode um alle Lineedit, Comboboxen, etc. mit den ausgewählten werten zu befüllen.
        """
        #QApplication.setOverridemycursor(Qmycursor(Qt.Waitmycursor)
        try:
            self.cB_Ausbildungsthema.setCurrentText(self.tW_Datenbank.item(row, 1).text())
            self.le_Lehrstoff_ID.setText(self.tW_Datenbank.item(row, 2).text())
            self.le_Hauptthema.setText(self.tW_Datenbank.item(row,  3).text())
            self.le_Lehrstoff.setText(self.tW_Datenbank.item(row, 4).text())
            self.cB_Verantwortlicher.setCurrentText(self.tW_Datenbank.item(row, 5).text())
            self.le_Dokument.setText(self.tW_Datenbank.item(row, 6).text())
            self.sB_Stunden.setValue(int(self.tW_Datenbank.item(row, 7).text()))
            self.le_Hilfsmittel.setText(self.tW_Datenbank.item(row, 8).text())
            self.cB_Reference.setCurrentText(self.tW_Datenbank.item(row, 9).text())
        except Exception:
            self.tW_Datenbank_Anzeigen()
                
    
    @pyqtSlot()
    def on_pB_Suchen_clicked(self):
        
        """
        Slot documentation goes here
        """
        self.searchWindow = Lehrstoff_Suche(self)
        self.searchWindow.show()


    @pyqtSlot()
    def on_tB_Dokument_Suchen_clicked(self):
        
        """
        Methode um ein Dokument aus einer Directory (Explorer-Suche) einzfügen
        """
        dokument = str(QtWidgets.QFileDialog.getOpenFileName(self))
        self.le_Dokument.setText(dokument)
        self.INFO("Dokument wurde eingefügt.",  "I")
        
    @pyqtSlot()
    def on_pB_Excel_clicked(self):
        
        """
        Methode um HTML Datei zu erstellen
        """
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "kat_lehrstoff")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)                  
            os.startfile("Excel\kat_lehrstoff.xlsx")
            self.INFO("Excel-Datei wurde erstellt.",  "I")
            
        except Exception:
            self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")

    @pyqtSlot()
    def on_pB_Report_clicked(self):
        
        """
        Methode um HTML Datei zu erstellen
        """
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_lehrstoff")
            
            input_file = 'Reports\kat_lehrstoff.jasper'
            output = 'Reports\kat_lehrstoff'
            jasper = JasperPy()
            con={
                'driver':'generic',
                'jdbc_driver':'"org.sqlite.JDBC"',
                'jdbc_url':'jdbc:sqlite:kat.db'
            }
            
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            
            os.startfile("Reports\kat_lehrstoff.pdf")
            self.INFO("PDF-Datei wurde erstellt.",  "I")
        except Exception:
            self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
        
    @pyqtSlot(str)
    def on_cB_Ausbildungsthema_currentTextChanged(self, p0):
        
        
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        if p0 == "Alle Anzeigen":
          self.clearFields()
          
        self.tW_Datenbank_Anzeigen("Ausbildungsthema", p0)
    
    @pyqtSlot(str)
    def on_cB_Verantwortlicher_currentTextChanged(self, p0):
        
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        if p0 == "Alle Anzeigen":
            self.clearFields()
        self.tW_Datenbank_Anzeigen("Verantwortlicher", p0)



    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
    
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")


    @pyqtSlot()
    def on_pB_ClearFields_clicked(self):
        """
        Slot documentation goes here.
        """
        self.clearFields()
        self.tW_Datenbank_Anzeigen()
        
        
    def closeEvent(self, event):
        
        self.parent().show()
        
        
    def combobox_befüllen(self):
        
        """
        Methode für das Befüllen der Combobox aus den Datenbanktabellen kat_fachgebiete und
        kat_ausbilder
        """
        #befüllen der ComboBox "cB_Ausbildungsthema" aus der DB kat_fachgebiete
        db = Database.get_instance(self)
        sql = "SELECT kat_ausbildungsthemen.Ausbildungsthema FROM kat_ausbildungsthemen"
        mycursor = db.select(sql)
        rows = mycursor.fetchall()
        if mycursor == "backtologin":
            self.back_to_login()
            return
        self.cB_Ausbildungsthema.addItem("Alle Anzeigen")
        for i in rows:
            self.cB_Ausbildungsthema.addItem(i[0])
            
         #befüllen der ComboBox "cB_Verantwortlicher" aus der DB kat_ausbilder
        sql = "SELECT kat_ausbilder.Familienname FROM kat_ausbilder"
        mycursor = db.select(sql)
        rows2 = mycursor.fetchall()
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        self.cB_Verantwortlicher.addItem("Alle Anzeigen")
        for i in rows2:
            self.cB_Verantwortlicher.addItem(i[0])
            
        #befüllen der Combobox "cB_Filter aus der der DB-Tabelle kat_fachrichtung
        sql = "SELECT KAT_fachrichtungen.Bezeichnung FROM KAT_fachrichtungen"
        mycursor = db.select(sql)
    
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        rows = mycursor.fetchall()
        self.cB_Filter.addItem("Alle Anzeigen")
        for i in rows:
            self.cB_Filter.addItem(i[0])
        
    def referenz_cB_befüllen(self):
    
        self.cB_Reference.clear()
        db = Database.get_instance(self)
        if self.cB_Filter.currentText() == "Alle Anzeigen":
            sql = "SELECT id, Fachrichtung, Themen_ID, Thema FROM kat_lap_themenkatalog"
        else: 
            sql = "SELECT id, Fachrichtung, Themen_ID, Thema FROM kat_lap_themenkatalog WHERE Fachrichtung = '" +self.cB_Filter.currentText()+"'"              #dazu noch eine on_current-textChanged (von der neuen CB) funktion wo die referenz_cb_befüllen methode aufgerufen wird
        mycursor = db.select(sql)
        rows = mycursor.fetchall()
        if mycursor == "backtologin":
            self.back_to_login()
            return
        for i in rows:
            self.cB_Reference.addItem(str(i[2]) + ":" + i[3],  i[0])
    
    
    @pyqtSlot(str)
    def on_cB_Filter_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        print("filter")
        self.referenz_cB_befüllen()




    def tW_Datenbank_Anzeigen(self, filter1 = "",  filter2 = ""):
        
        """
        Methode um das Tablewidget aus der DB-Tabelle kat_lehrstoff zu befüllen
        """
        self.setCursor(Qt.WaitCursor)
        db = Database.get_instance(self)
        #überschriften setzen
        self.tW_Datenbank.setColumnCount(11)
        colname = QTableWidgetItem("Ausbildungsthema")
        self.tW_Datenbank.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Lehrstoff_ID")
        self.tW_Datenbank.setHorizontalHeaderItem(1,  colname)
        colname = QTableWidgetItem("Hauptthema")
        self.tW_Datenbank.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Lehrstoff")
        self.tW_Datenbank.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Verantwortlicher")
        self.tW_Datenbank.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Dokument")
        self.tW_Datenbank.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Stunden")
        self.tW_Datenbank.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("Hilfsmittel")
        self.tW_Datenbank.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("LAP-Refernz-ID")
        self.tW_Datenbank.setHorizontalHeaderItem(8, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tW_Datenbank.setHorizontalHeaderItem(9, colname)
        colname = QTableWidgetItem("Änderung")
        self.tW_Datenbank.setHorizontalHeaderItem(10, colname)
        
        self.tW_Datenbank.setRowCount(1)
        if filter2 == "Alle Anzeigen":
            filter2 = ""
        if filter2 != "":
            sql =  "select * from kat_lehrstoff WHERE "+ filter1 +" = '" + filter2 + "'"
        else:
            sql = "select * from kat_lehrstoff"
            
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0 
     
        for z in mycursor:
            for s in range(0,  11):
                self.tW_Datenbank.setRowCount(zeile + 1)
                fielditem = QTableWidgetItem(str(z[s +1]))
                self.tW_Datenbank.setItem(zeile,  s,  fielditem)
            zeile+=1
                
        mycursor.close()
        
        self.tW_Datenbank.resizeColumnsToContents()
        self.tW_Datenbank.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        
    def back_to_login(self):


        """
        Methode um bei Verbindungsabbruch zur DB 
        """
        self.parent().back_to_login()
        self.close()


    def clearFields(self):
        self.cB_Ausbildungsthema.setCurrentText("Alle Anzeigen")
        self.le_Lehrstoff_ID.setText("")
        self.cB_Verantwortlicher.setCurrentText("Alle Anzeigen")
        self.le_Hauptthema.setText("")
        self.le_Lehrstoff.setText("")
        self.le_Dokument.setText("")
        self.sB_Stunden.setValue(0)
        self.le_Hilfsmittel.setText("")
    

