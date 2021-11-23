# -*- coding: utf-8 -*-

"""
Module implementing Lehrlingseinteilungtabelle.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QMessageBox
from sub.XML.XML_Class import DBtoXML
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem  
from sub.rotation.Ui_Lehrlingseinteilungstabelle import Ui_Dialog
from sub.rotation.Lehrlingseinteilung import Lehrlingseinteilung_App

from other.database import Database
import tkinter as tk
from tkinter import messagebox
import os, time
import datetime
from pyreportjasper import JasperPy


class Lehrlingseinteilungtabelle(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrlingseinteilungtabelle, self).__init__(parent)
        self.setupUi(self)
        self.twData_anzeigen()
        
        self.actualDate = str(datetime.datetime.now().date())
        self.date1 = int(self.actualDate[:4])
        self.date2 = self.date1 - 1
    
    @pyqtSlot()
    def on_pB_leftArrow_clicked(self):
        """
        Slot documentation goes here.
        """
        self.date1 -= 1
        self.date2 -= 1
        self.lbl_Ausbildungsjahr.setText(str(self.date2) +"/" + str(self.date1))
        self.twData_anzeigen()
    
    @pyqtSlot()
    def on_pB_rightArrow_clicked(self):
        """
        Slot documentation goes here.
        """
        self.date1 += 1
        self.date2 += 1
        self.lbl_Ausbildungsjahr.setText(str(self.date2) +"/" + str(self.date1))
        self.twData_anzeigen()
    
    @pyqtSlot(int, int)
    def on_tW_Lehrlingseinteilung_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        self.w = Lehrlingseinteilung_App(self)
        self.w.setAusbildungswoche(column)
        self.w.setZeile(row)
        self.w.show()
    
    @pyqtSlot()
    def on_pB_Mainmenu_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pB_Export_Data_clicked(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(
            self,
            self.tr("Hilfe"),
            self.tr("""Die Exportfunktion wird demnächst Hinzugefügt!"""))
        
    
    @pyqtSlot()
    def on_pB_Help_clicked(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(
            self,
            self.tr("Hilfe"),
            self.tr("""Die Hilfefunktion wird demnächst Hinzugefügt!"""))
        
        
    def twData_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """   
    
        #set Columnheader 
        self.tW_Lehrlingseinteilung.setColumnCount(59)
        colname = QTableWidgetItem("Lehrling")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("P-Nr.")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Beruf")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Lj")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Berufsschule")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Ausbildungsjahr")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(5, colname)
        kw = 34
        for i in range(6, 59):
            if kw == 54:
                kw = 1
            colname = QTableWidgetItem("KW " +str(kw))
            self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(i,  colname)
            kw = kw + 1
            
        self.tW_Lehrlingseinteilung.setRowCount(1)
        
        db = Database.get_instance(self)
        
        #ersten 6 spalten befüllen
        mycursor = db.select("SELECT Vorname, Nachname, Personalnummer, Lehrberuf, Lehrbeginn from kat_lehrlinge") 
        zeile = 0
        for z in mycursor:
            self.tW_Lehrlingseinteilung.setRowCount(zeile + 1)
            
            fielditem = QTableWidgetItem(str(z[0]) + " " + str(z[1]))
            self.tW_Lehrlingseinteilung.setItem(zeile,  0,  fielditem)
            
            fielditem = QTableWidgetItem(str(z[2]))
            self.tW_Lehrlingseinteilung.setItem(zeile,  1,  fielditem)
            
            fielditem = QTableWidgetItem(str(z[3]))
            self.tW_Lehrlingseinteilung.setItem(zeile,  2,  fielditem)
    
            fielditem = QTableWidgetItem(str(self.compareDate(str(datetime.datetime.now().date()),  str(z[4]))))
            self.tW_Lehrlingseinteilung.setItem(zeile,  3,  fielditem)
            zeile += 1
                
                
        
#        mycursor = db.select("SELECT * FROM kat_einteilung" )
#        zeile = 0 
#        for z in mycursor:
#            for s in range(6,  59):
#                fielditem = QTableWidgetItem(str(z[s]))
#                self.tW_Lehrlingseinteilung.setItem(zeile,  s,  fielditem)
#            zeile+=1
            
        mycursor.close()#cursor wird geschlossen
        self.tW_Lehrlingseinteilung.resizeColumnsToContents()
        self.tW_Lehrlingseinteilung.resizeRowsToContents()       

    def closeEvent(self, event):
        
        self.parent().show()
        
        
    def compareDate(self,  date_now,  date_apprentice):
        
        dateNow_month = int(date_now[5:7] + date_now[8:10])
        dateNow_year = int(date_now[:4])
        
        dateApprentice_month = int(date_apprentice[5:7] + date_apprentice[8:10])
        dateApprentice_year = int(date_apprentice[:4])
        
        if dateNow_year > dateApprentice_year:
            if dateNow_month >= dateApprentice_month:
                return (dateNow_year - dateApprentice_year) + 1
            else:
               return  dateNow_year - dateApprentice_year
        else:
            print("Eintrittsdatum des Lehrlings ist größer als das aktuelle Datum!")
            
    
