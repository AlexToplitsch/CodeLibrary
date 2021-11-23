# -*- coding: utf-8 -*-

 

"""
Module implementing LAB_Ausbilder.
"""

from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from other.database import Database
from sub.bs.Ui_Bs import Ui_Berufsschule
#from sub.XML.XML_Class import XML_Class
#from sub.XML.XML_Class import DBtoXML
from tkinter import messagebox
import tkinter as tk
#import os
#from PyQt5 import QtCore
#import ctypes
#from tkinter import simpledialog

root = tk.Tk()



class Bs(QDialog, Ui_Berufsschule):
    """
    Class documentation goes here.
    """


    def __init__(self, parent=None):
        super(Bs, self).__init__(parent)
        self.setupUi(self)
        self.tw_Data_anzeigen()  
        pass

    def tw_Data_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        self.tw_Data.setColumnCount(8)
        colname = QTableWidgetItem("ID")
        self.tw_Data.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Personal Nummer")
        self.tw_Data.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Lehrjahr")
        self.tw_Data.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Von-Datum")
        self.tw_Data.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Bis-Datum")
        self.tw_Data.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Berufschule")
        self.tw_Data.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Ansprechperson")
        self.tw_Data.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("Zeugnisse")
        self.tw_Data.setHorizontalHeaderItem(7, colname)
    
        self.tw_Data.setRowCount(1)
        sql = "SELECT * FROM KAT_berufsschulzeit"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        zeile = 0
        for z in mycursor: 
            for s in range(0, 8):
                self.tw_Data.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tw_Data .setItem(zeile,  s,  fielditem)
            zeile += 1
        
        #mycursor.close()
        
        self.tw_Data.resizeColumnsToContents()
        self.tw_Data.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)    
    
    
    
    
    def on_btLoeschen_clicked(self):
        """
        on_btLoeschen_clicked löscht eine Zeile aus der Tabelle
        """
        db = Database.get_instance(self)
        sql = "DELETE FROM KAT_berufsschulzeit WHERE PERS_NR = '" + self.lePersNr.text() + "'"
        db.delete(sql)
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe
        self.twAnzeigen()

    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        root = tk.Tk()
        root.withdraw()
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
            messagebox.showerror("Fehler", MELDUNG)
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
                messagebox.showwarning("Hinweis/Warnung", MELDUNG)
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
