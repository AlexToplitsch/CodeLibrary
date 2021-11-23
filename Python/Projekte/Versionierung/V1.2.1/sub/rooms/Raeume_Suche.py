# -*- coding: utf-8 -*-

"""
Module implementing Suche_Dialog.
"""
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem
from other.database import Database
from sub.rooms.Ui_Raeume_Suche import Ui_Dialog
#import sys

class Suche_Dialog(QDialog, Ui_Dialog):
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
        self.parent().leRaum.setText(self.tb_Raeume.item(row, 1).text())
        self.parent().leGebaeude.setText(self.tb_Raeume.item(row, 2).text())
        self.parent().leStock.setText(self.tb_Raeume.item(row, 3).text())
        self.parent().leRaumNr.setText(self.tb_Raeume.item(row, 4).text())
        self.parent().lePlaetze.setText(self.tb_Raeume.item(row, 5).text())
        
    
    @pyqtSlot(int, int)
    def on_tb_Raeume_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        self.parent().leRaum.setText(self.tb_Raeume.item(row, 1).text())
        self.parent().leGebaeude.setText(self.tb_Raeume.item(row, 2).text())
        self.parent().leStock.setText(self.tb_Raeume.item(row, 3).text())
        self.parent().leRaumNr.setText(self.tb_Raeume.item(row, 4).text())
        self.parent().lePlaetze.setText(self.tb_Raeume.item(row, 5).text())
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
        self.setCursor(Qt.WaitCursor)
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tb_Raeume.setColumnCount(8)
        colname = QTableWidgetItem("ID")
        self.tb_Raeume.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Raum")
        self.tb_Raeume.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Gebäude")
        self.tb_Raeume.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Stock")
        self.tb_Raeume.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("RaumNr")
        self.tb_Raeume.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Plätze")
        self.tb_Raeume.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tb_Raeume.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("Änderung")
        self.tb_Raeume.setHorizontalHeaderItem(7, colname)
        
        self.tb_Raeume.setRowCount(1)
        
        db = Database.get_instance(self)

        if f1 != "":
           sql = "select Raum,Gebäude,Stock,RaumNr,Plätze,Benutzer,`Änderung` from kat_raeume where concat(Raum, Gebäude, Stock, RaumNr, Plätze, Benutzer) like '"+ '%' + f1 + '%' "'"
        else:
            sql = "select Raum,Gebäude,Stock,RaumNr,Plätze,Benutzer,`Änderung` from kat_raeume"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        zeile = 0 
        for z in mycursor:
            for s in range(0,  7):
                self.tb_Raeume.setRowCount(zeile + 1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tb_Raeume.setItem(zeile,  s,  fielditem)
            zeile+=1
        
                
        mycursor.close()
        
        self.tb_Raeume.resizeColumnsToContents()
        self.tb_Raeume.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        
        
    def on_pB_Beenden_clicked(self):
       self.hide()
       
        
    def closeEvent(self, event):
        self.parent().show()
