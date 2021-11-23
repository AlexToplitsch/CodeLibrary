# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
#from pyreportjasper import JasperPy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from tkinter import messagebox
import tkinter as tk
#import mysql.connector
from other.database import Database
from sub.field import Fachrichtungen_Suche
from sub.field.Ui_Fachrichtungen import Ui_Fachrichtungen
from sub.XML.XML_Class import DBtoXML
#import dicttoxml
from xml.dom.minidom import *
#import xml.etree.cElementTree as ET
#from xml.etree.ElementTree import Element, SubElement, Comment, tostring
#from xml.etree import ElementTree
import os

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
            messagebox.showerror("Fehler", MELDUNG)
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
                messagebox.showwarning("Hinweis/Warnung", MELDUNG)
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
    def Report_processing():
        
        os.chdir('\\Reports\\')
        input_file = '\Reports\fachrichtungen.jasper'
        output = '\\Reports\\report-datei'
        jasper = JasperPy()
        con={
            'driver': 'sqlite',
            'jdbc_driver':'sqlite ……',
            'jdbc_url':'jdbc:\\knapp_apprantice_training\kat.db'
            }
        jasper.process(input_file, output_file=output, db_connection=con,  format_list=["pdf"])
        
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
        self.twAnzeige.setHorizontalHeaderItem(3,  colname)
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
        #self.setTableWidth()
    def closeEvent(self, event):
        self.parent().show()
    @pyqtSlot()
    def on_btSpeichern_clicked(self):
        """
        Das Klickevent on_btSpeichern_clicked speichert die eingegebenen Daten die Datenbank
        Diese werden dann mithilfe der Methode self.twAnzeigen() im QTableWidget aktualisiert.
        """
        #mycursor = mydb.cursor()
        #sql_satz = []
        #sql = "select * from apprentice_fachrichtungen WHERE fachrichtung = '" + self.leFachrichtungabk.text() + "'"
        #mycursor.execute(sql)
        #sql_satz = mycursor.fetchall()
        #satz_len = len(sql_satz)
        #print(satz_len,  sql)
        if self.leFachrichtungabk.text() == "":
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Achtung!",  "Geben sie Daten ein! ")
            self.twAnzeigen()
            #db.toSQLite("kat_fachrichtungen")
        else: 
            db = Database.get_instance(self)
            sql = "select * from kat_fachrichtungen WHERE fachrichtung = '" + self.leFachrichtungabk.text() + "'"
            mycursor = db.select(sql)
        
            if mycursor == "backtologin":
                self.back_to_login
                return
            
            sql_satz = []
            sql_satz = mycursor.fetchall()
            satz_len = len(sql_satz)
        
            if satz_len == 0:
                print("insert")
                sql = "INSERT INTO kat_fachrichtungen (fachrichtung, bezeichnung, lehrjahre, benutzername) VALUES (%s, %s, %s, %s)"
                val = (self.leFachrichtungabk.text(),  self.leFachrichtungbez.text(),  self.sbLehrjahre.value(),  self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in die Datenbank gespeichert! ",  "I")
            else:
                print("update")
                sql = "UPDATE kat_fachrichtungen set bezeichnung=%s, lehrjahre=%s WHERE fachrichtung = '" + self.leFachrichtungabk.text() + "'"
                val = (self.leFachrichtungbez.text(), self.sbLehrjahre.value())
                self.INFO("Eintrag wurde in der Datenbank aktualisiert! ",  "I")
            db.insert(sql, val)
            self.twAnzeigen()
            #db.writeSQLite("kat_fachrichtungen")
    
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
        #db.writeSQLite("kat_fachrichtungen")
    
    @pyqtSlot()
    def on_btHilfe_clicked(self):
        """
        """
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Hilfe",  "Die hilfe Funktion wird in kürze hinzugefügt!")
#        db = Database.get_instance(self)
#        db.writeSQLite("kat_fachrichtungen")
        
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
        print(self.parent())
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
        self.INFO("PDF-Datei wure erstellt.",  "I")# info asugabe
        db = Database.get_instance(self)
        db.writeSQLite("kat_fachrichtungen")
        #self.Report_processing()
        pass
        
    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
