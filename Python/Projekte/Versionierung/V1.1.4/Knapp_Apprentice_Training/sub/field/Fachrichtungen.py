# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from pyreportjasper import JasperPy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from xml.dom.minidom import *
import os
from other.database import Database
from sub.field import Fachrichtungen_Suche
from sub.field.Ui_Fachrichtungen import Ui_Fachrichtungen
from sub.XML.XML_Class import DBtoXML


class Fachrichtungen(QDialog, Ui_Fachrichtungen):
    """
    Klasse zum Verwalten der Fachrichtungen(Lehrberufe)
    """
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fachrichtungen, self).__init__(parent)
        self.setupUi(self)
        self.twAnzeigen()
     
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
            root = tk.Tk()
            root.withdraw()
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
    
    def twAnzeigen(self):
        """
        Methode zum befüllen der Spalten aus der Datenbank ins QTableWidget
        """
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        self.twAnzeige.setColumnCount(5)
        colname=QTableWidgetItem("Fachrichtung")
        self.twAnzeige.setHorizontalHeaderItem(0,  colname)
        colname=QTableWidgetItem("Bezeichnung")
        self.twAnzeige.setHorizontalHeaderItem(1,  colname)
        colname=QTableWidgetItem("Lehrjahre")
        self.twAnzeige.setHorizontalHeaderItem(2,  colname)
        colname=QTableWidgetItem("Benutzername")
        self.twAnzeige.setHorizontalHeaderItem(3,   colname)
        colname=QTableWidgetItem("Änderungsdatum")
        self.twAnzeige.setHorizontalHeaderItem(4,  colname)
        self.twAnzeige.setRowCount(1)
        
        sql = "SELECT fachrichtung, bezeichnung, lehrjahre, benutzername, aenderungsdatum  FROM kat_fachrichtungen"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile=0
        
        for z in mycursor:
            for s in range(0, 5):
             self.twAnzeige.setRowCount(zeile+1)
             fielditem = QTableWidgetItem(str(z[s]))
             self.twAnzeige.setItem(zeile, s, fielditem)
            zeile += 1
        
        self.twAnzeige.resizeColumnsToContents()
        self.twAnzeige.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()

    def closeEvent(self, event):
        self.parent().show()

    @pyqtSlot()
    def on_btSpeichern_clicked(self):
        """
        Das Klickevent on_btSpeichern_clicked speichert die eingegebenen Daten die Datenbank
        Diese werden dann mithilfe der Methode self.twAnzeigen() im QTableWidget aktualisiert.
        """
        if self.leFachrichtungabk.text() == "":
            root = tk.Tk()
            root.withdraw()
            self.twAnzeigen()
        else: 
            db = Database.get_instance(self)
            sql = "select * from kat_fachrichtungen WHERE fachrichtung='" + self.leFachrichtungabk.text() +"'"
            
            mycursor = db.select(sql)
            print(sql)
            if mycursor == "backtologin":
                self.back_to_login
                return
            sql_satz = []
            sql_satz = mycursor.fetchall()
            satz_len = len(sql_satz)

            if satz_len == 0:
                sql = "INSERT INTO kat_fachrichtungen (fachrichtung, bezeichnung, lehrjahre, benutzername) VALUES (%s, %s, %s, %s)"
                val = (self.leFachrichtungabk.text(), self.leFachrichtungbez.text(), self.sbLehrjahre.value(), self.parent().label_eingeloggt_als.text())
                
                self.INFO("Eintrag wurde in die Datenbank gespeichert! ",  "I")
            else:
                sql = "UPDATE kat_fachrichtungen SET bezeichnung=%s, lehrjahre=%s, benutzername=%s WHERE fachrichtung = '" + self.leFachrichtungabk.text() + "'"
                val = (self.leFachrichtungbez.text(), self.sbLehrjahre.value(), self.parent().label_eingeloggt_als.text())
                
                self.INFO("Eintrag wurde in der Datenbank aktualisiert! ",  "I")
            db.insert(sql, val)
            self.twAnzeigen()
    
    @pyqtSlot()
    def on_btLoeschen_clicked(self):
        """
        on_btLoeschen_clicked löscht eine Zeile aus der Tabelle
        """
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_fachrichtungen WHERE fachrichtung = '" + self.leFachrichtungabk.text() + "'"
        db.delete(sql)
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe
        self.twAnzeigen()
    
    @pyqtSlot()
    def on_btHilfe_clicked(self):
        """
        """
        self.INFO("Hilfe Funktion wird noch hinzugefügt!",  "I")# info asugabe
    
    @pyqtSlot()
    def on_btClear_clicked(self):
        """
        """
        self.leFachrichtungabk.setText("")
        self.leFachrichtungbez.setText("")
        Lehrjahre = float("3.5")
        self.sbLehrjahre.setValue(Lehrjahre)

    @pyqtSlot(int, int)
    def on_twAnzeige_cellClicked(self, row, column):
        """
        """
        self.leFachrichtungabk.setText(self.twAnzeige.item(row,  0).text())
        self.leFachrichtungbez.setText(self.twAnzeige.item(row,  1).text())
        Lehrjahre = float(self.twAnzeige.item(row,  2).text())
        self.sbLehrjahre.setValue(Lehrjahre)

    @pyqtSlot()
    def on_btAbbrechen_clicked(self):
        """
        """
        
        self.parent().show()
        self.close()
 
    @pyqtSlot()
    def on_btExcel_clicked(self):
        """
        """
        
        self.INFO("Excel-Datei wure erstellt.",  "I")# info asugabe
        db = Database.get_instance(self)
        DBtoXML.MakeXML(db, "kat_fachrichtungen")
        
        os.startfile("Excel\kat_fachrichtungen.xlsx")

    @pyqtSlot()
    def on_btSuchen_clicked(self):
        """
        """
        self.suchefenster = Fachrichtungen_Suche.Suche_Dialog(self)
        self.suchefenster.show()
    
    @pyqtSlot()
    def on_btCSV_clicked(self):
        """
        """
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_fachrichtungen")
        
            input_file = "Reports/kat_fachrichtungen.jasper"
            output = "Reports/kat_fachrichtungen"
            jasper = JasperPy()
            con={
            'driver': 'generic',
            'jdbc_driver':'org.sqlite.JDBC',
            'jdbc_url':'jdbc:sqlite:kat.db'
            }
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])
        
            self.INFO("PDF-Datei wurde erstellt",  "I")
        except Exception:
            self.INFO("PDF-Datei konnte nicht erstellt werden.",  "F")
        os.startfile("Reports\kat_fachrichtungen.pdf")

    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
