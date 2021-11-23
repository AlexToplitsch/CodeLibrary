# -*- coding: utf-8 -*-

"""
Module implementing Suche_Dialog.
"""
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem
from other.database import Database
from sub.bs.Ui_Bs_Suche import Ui_Suche
import datetime
from datetime import date
#import sys

class Suche_Dialog(QDialog, Ui_Suche):
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """

        super(Suche_Dialog, self).__init__(parent)
        self.setupUi(self)
        
    
    @pyqtSlot(int, int)
    def on_tb_Raeume_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        #today = date.today()
        
#        if self.tb_Raeume.item(row,  2). text() == "None":
#            date_str = today.strftime("%d.%m.%Y")
#            self.de_Eintritt.setDate(datetime.datetime.strptime(date_str, '%d.%m.%Y').date())
#        else:
#            date_str = self.tb_Raeume.item(row,  2).text()
#            EINTRITTS_DATUM = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
#            self.de_Eintritt.setDate(EINTRITTS_DATUM)
#        
#        if self.tb_Raeume.item(row,  3). text() == "None":
#            date_str = today.strftime("%d.%m.%Y")
#            self.de_Austritt.setDate(datetime.datetime.strptime(date_str, '%d.%m.%Y').date())
#        else:
#            date_str = self.tb_Raeume.item(row,  3).text()
#            AUSTRITTS_DATUM = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
#            self.de_Austritt.setDate(AUSTRITTS_DATUM)
#            
#        #date_str = self.tb_Raeume.item(row,  5).text()
#        self.le_PersNr.setText(self.tb_Raeume.item(row,  0).text())
        
        self.parent().le_PersNr.setText(self.tb_Raeume.item(row,  0).text())
        #self.parent().le_PersNr.setText(self.tb_Raeume.item(row,  3).text())
        #self.parent().le_PersNr.setText(self.tb_Raeume.item(row,  4).text())
        self.parent().cb_Bs.setCurrentText(self.tb_Raeume.item(row,  4).text())
        self.parent().le_Ansprechpartner.setText(self.tb_Raeume.item(row,  5).text())
        
    
    @pyqtSlot(int, int)
    def on_tb_Raeume_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        today = date.today()
        
        if self.tb_Raeume.item(row,  2). text() == "None":
            date_str = today.strftime("%d.%m.%Y")
            self.parent().de_Eintritt.setDate(datetime.datetime.strptime(date_str, '%d.%m.%Y').date())
        else:
            date_str = self.tb_Raeume.item(row,  2).text()
            EINTRITTS_DATUM = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
            self.parent().de_Eintritt.setDate(EINTRITTS_DATUM)
        
        if self.tb_Raeume.item(row,  3). text() == "None":
            date_str = today.strftime("%d.%m.%Y")
            self.parent().de_Austritt.setDate(datetime.datetime.strptime(date_str, '%d.%m.%Y').date())
        else:
            date_str = self.tb_Raeume.item(row,  3).text()
            AUSTRITTS_DATUM = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
            self.parent().de_Austritt.setDate(AUSTRITTS_DATUM)
        
        self.parent().le_PersNr.setText(self.tb_Raeume.item(row,  0).text())
        #self.parent().le_PersNr.setText(self.tb_Raeume.item(row,  3).text())
        #self.parent().le_PersNr.setText(self.tb_Raeume.item(row,  4).text())
        self.parent().cb_Bs.setCurrentText(self.tb_Raeume.item(row,  4).text())
        self.parent().le_Ansprechpartner.setText(self.tb_Raeume.item(row,  5).text())
        self.hide()
    
    @pyqtSlot()
    def on_pB_Suchen_clicked(self):
        """
        Slot documentation goes here.
        """
        
        self.cell_tb_Raeume(self.leRaeume.text())
        self.leRaeume.setText("")
             
    
    @pyqtSlot()
    
    def cell_tb_Raeume(self,  f1 = ""):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        
        
        self.tb_Raeume.setColumnCount(8)
        colname = QTableWidgetItem("Personal Nummer")
        self.tb_Raeume.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Lehrjahr")
        self.tb_Raeume.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Von-Datum")
        self.tb_Raeume.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Bis-Datum")
        self.tb_Raeume.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Berufschule")
        self.tb_Raeume.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Ansprechperson")
        self.tb_Raeume.setHorizontalHeaderItem(5, colname)
#        colname = QTableWidgetItem("Zeugnisse")
#        self.tb_Raeume.setHorizontalHeaderItem(6, colname) 
        colname = QTableWidgetItem("Benutzer")
        self.tb_Raeume.setHorizontalHeaderItem(6, colname) 
        colname = QTableWidgetItem("Änderung")
        self.tb_Raeume.setHorizontalHeaderItem(7, colname) 
    
        
        if f1 != "":
           sql = "select PERS_NR,Lehrjahr,VonDatum,BisDatum,Berufsschule,Ansprechperson,Benutzer,`Änderung` from kat_berufsschulzeit where concat(PERS_NR,Lehrjahr,VonDatum,BisDatum,Berufsschule,Ansprechperson,Benutzer) like '"+ '%' + f1 + '%' "'"
        else:
            sql = "select PERS_NR,Lehrjahr,VonDatum,BisDatum,Berufsschule,Ansprechperson,Benutzer,`Änderung` from kat_berufsschulzeit"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        
        zeile = 0
        for z in mycursor: 
            self.tb_Raeume.setRowCount(zeile+1)
            fielditem = QTableWidgetItem(str(z[0]))
            self.tb_Raeume .setItem(zeile,  0,  fielditem)
            #            for s in range(0, 9):
#                self.tb_Raeume.setRowCount(zeile+1)
#                if s == 8:
#                    fielditem = QTableWidgetItem(str(z[s]))
#                else:
#                    fielditem = QTableWidgetItem(str(z[s+1]))
#                self.tb_Raeume .setItem(zeile,  s,  fielditem)
            for s in range(0, 8):
                self.tb_Raeume.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tb_Raeume.setItem(zeile,  s,  fielditem)

            y, m, d = str(z[1])[0:4], str(z[1])[5:7], str(z[1])[8:10] #Geht vom tb aus und nicht von der Heidi DB
            #print(str(z[1])[0:4]+" - "+ str(z[1])[5:7] +" - "+ str(z[1])[8:10])
            today = datetime.date.today()
            #print(today)
            ty, tm, td = str(today)[0:4], str(today)[5:7], str(today)[8:10]
            
            if ty > y:
                lj = int(ty) - int( y)
                if tm > m and td > d:
                    lj = int(ty) - int(y) + 1
            else:
                lj = 1
               
            self.tb_Raeume.setRowCount(zeile+1)
            fielditem1 = QTableWidgetItem(str(lj))
            self.tb_Raeume .setItem(zeile,  1,  fielditem1)

            zeile += 1
        
        mycursor.close()
        
        #mycursor.close()
        
        self.tb_Raeume.resizeColumnsToContents()
        self.tb_Raeume.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)    
        
        
    def on_pB_Beenden_clicked(self):
       self.hide()
       
        
    def closeEvent(self, event):
        self.parent().show()
