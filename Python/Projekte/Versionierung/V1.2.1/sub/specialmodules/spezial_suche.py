# -*- coding: utf-8 -*-

"""
Module implementing Suche_Spezial.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sub.specialmodules.Ui_spezial_suche import Ui_Dialog
from other.database import Database


class Suche_Spezial(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Suche_Spezial, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def initDatabase(self):
        self.mydb = Database.getinstance(self)
    
    
    def tw_Anzeige(self, b=""):
        
        
        self.setCursor(Qt.WaitCursor)
        
        self.tableWidget.setColumnCount(4)
        
        colname = QTableWidgetItem("Spezialmodul")
        self.tableWidget.setHorizontalHeaderItem(0,  colname)
        colname = QTableWidgetItem("Beschreibung")
        self.tableWidget.setHorizontalHeaderItem(1,  colname)
        colname = QTableWidgetItem("Benutzer")
        self.tableWidget.setHorizontalHeaderItem(2,  colname)
        colname = QTableWidgetItem("Änderung")
        self.tableWidget.setHorizontalHeaderItem(3,  colname)
        
        self.tableWidget.setRowCount(1)
        db = Database.get_instance(self)
        
        if b!="":            
            sql="select spezial, beschreib, benutzer, änderung FROM kat_spezialmodule WHERE spezial LIKE '%"+b+"%'"
        else:
            sql="select spezial, beschreib, benutzer, änderung FROM kat_spezialmodule"
        print(sql)
        mycursor=db.select(sql)    
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  4):
                self.tableWidget.setRowCount(zeile +1)
                fielditem=QTableWidgetItem(str(z[s]))
                self.tableWidget.setItem(zeile, s, fielditem)
            zeile+=1
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()    

    def on_btn_suchen_clicked(self):
        
        b = self.le_suche.text()
        
        if b != "":
            self.tw_Anzeige(b)
        else:
            self.tw_Anzeige
    
    @pyqtSlot()
    def on_btn_abbrechen_clicked(self):
        self.hide()
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellClicked(self, row, column):
        
        self.parent().le_Modul.setText(self.tableWidget.item(row,  0).text())
        self.parent().te_Beschreib.setPlainText(self.tableWidget.item(row,  1).text())
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):
        self.hide()
