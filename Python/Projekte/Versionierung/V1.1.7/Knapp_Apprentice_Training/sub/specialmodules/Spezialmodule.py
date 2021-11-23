# -*- coding: utf-8 -*-

"""
Module implementing Spezialmodule.
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from tkinter import messagebox
import tkinter as tk
from sub.XML.XML_Class import DBtoXML
from other.database import Database
from sub.specialmodules.Ui_Spezialmodule import Ui_Spezialmodule
from sub.specialmodules import spezial_suche
import os
from pyreportjasper import JasperPy
import time

class Spezialmodule(QDialog, Ui_Spezialmodule):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        
        super(Spezialmodule, self).__init__(parent)
        self.setupUi(self)
        
        self.tw_Table_anzeigen()
        
       
    @pyqtSlot()
    def on_btn_abbrechen_clicked(self):
        self.parent().show()
        self.close()
    
    
    
    @pyqtSlot()
    def on_btn_loschen_clicked(self):
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_spezialmodule WHERE spezial = '" + self.le_Modul.text() + "' AND beschreib = '"+ self.te_Beschreib.toPlainText() +  "'"
        
        db.delete(sql)
        self.tw_Table_anzeigen()
        self.INFO("Ausgewähler Eintrag wurde aus der Datenbank gelöscht.",  "I")
    
    
    def tw_Table_anzeigen(self):
        db = Database.get_instance(self)
        
        self.setCursor(Qt.WaitCursor)
        
        self.tw_Table.setColumnCount(4)
        
        
        colname = QTableWidgetItem("Spezialmodul")
        self.tw_Table.setHorizontalHeaderItem(0,  colname)
        colname = QTableWidgetItem("Beschreibung")
        self.tw_Table.setHorizontalHeaderItem(1,  colname)
        colname = QTableWidgetItem("Benutzer")
        self.tw_Table.setHorizontalHeaderItem(2,  colname)
        colname = QTableWidgetItem("Änderung")
        self.tw_Table.setHorizontalHeaderItem(3,  colname)
        
        
        self.tw_Table.setRowCount(1)
        sql = "SELECT spezial, beschreib, Benutzer, Änderung FROM kat_spezialmodule"
        mycursor=db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  4):
                self.tw_Table.setRowCount(zeile +1)
                fielditem=QTableWidgetItem(str(z[s]))
                self.tw_Table.setItem(zeile, s, fielditem)
            zeile+=1
        self.tw_Table.resizeColumnsToContents()
        self.tw_Table.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
        
        
        
        
        
        
    @pyqtSlot()
    def on_btn_speichern_clicked(self):
       
        db = Database.get_instance(self)
        
        
        sql = "select * from kat_spezialmodule WHERE spezial = '" + self.le_Modul.text() + "'"
        mycursor =db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        sql_satz = []            
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        if satz_len == 0:
            sql = "INSERT INTO kat_spezialmodule (spezial, beschreib, Benutzer) VALUES (%s, %s, %s)"
            val = (self.le_Modul.text(),  self.te_Beschreib.toPlainText(),  self.parent().label_eingeloggt_als.text())
            self.INFO("Eintrag wurde in die Datenbank gespeichert.",  "I")
            
        else:
            sql = "UPDATE kat_spezialmodule set beschreib=%s, Benutzer=%s"+" WHERE spezial='" + self.le_Modul.text() + "'"
            
            val = (self.te_Beschreib.toPlainText(), self.parent().label_eingeloggt_als.text())
            
            self.INFO("Eintrag wurde in der Datenbank aktualisiert.",  "I")
        db.insert(sql,  val)
        self.clearAll()
        self.tw_Table_anzeigen()
        
    
    @pyqtSlot(int, int)
    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
    
    @pyqtSlot()
    def on_btn_excel_clicked(self):
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "kat_spezialmodule")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            os.startfile("Excel\kat_spezialmodule.xlsx")
            self.INFO("Excel-Datei wurde erstellt.",  "I")
            
        except Exception as e:
            print(e)
            self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")
    @pyqtSlot()
    def on_btn_report_clicked(self):
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_spezialmodule")
            
            input_file = 'Reports\kat_spezialmodule.jasper'
    #        output = 'MyReports' # Ziel-/SUB-Ordner
            
            output = 'Reports\kat_spezialmodule'
            
            jasper = JasperPy()
            
            con={
            'driver':'generic', 
            'jdbc_driver':'org.sqlite.JDBC', 
            'jdbc_url':'jdbc:sqlite:kat.db'
            }
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])   
            
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            
            self.INFO("PDF-Datei wurde erstellt.",  "I")
            os.startfile("Reports\kat_spezialmodule.pdf")
            
        except Exception as e:
            print(e)
            self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
        
    @pyqtSlot()
    def on_btn_hilfe_clicked(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Report",  "Die Report Funktion wird in kürze hinzugefügt!")
    
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
    
    
    def closeEvent(self, event):
        self.parent().show()
    @pyqtSlot()   
    def on_btn_Suchen_clicked(self):
        
        self.suchefenster = spezial_suche.Suche_Spezial(self)
        self.suchefenster.show()
    
    @pyqtSlot(int, int)
    def on_tw_Table_cellClicked(self, row, column):
        
        self.le_Modul.setText(self.tw_Table.item(row,  0).text())
        self.te_Beschreib.setPlainText(self.tw_Table.item(row,  1).text())
    
    @pyqtSlot()
    def clearAll(self):
        self.le_Modul.setText("")
        self.te_Beschreib.setPlainText("")
    @pyqtSlot()    
    def on_btn_clear_clicked(self):
        self.clearAll()
