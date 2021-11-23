# -*- coding: utf-8 -*-

"""
Module implementing Unterrichtsthemen_suchen.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem
from other.database import Database

from .Ui_Unterrichtsthemen_suchen import Ui_Unterrichtsthemen_suchen


class Unterrichtsthemen_suchen(QDialog, Ui_Unterrichtsthemen_suchen):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Unterrichtsthemen_suchen, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pb_suchen_clicked(self):
        self.cell_tw_suchen()

    
    @pyqtSlot()
    def cell_tw_suchen(self):
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
#        print("nach Qt.WaitCursor")
        #überschriften setzen
        self.tw_suchen.setColumnCount(4)
#        print("nach ColumnCount")
#        colname = QTableWidgetItem("ID")
#        self.tw_suchen.setHorizontalHeaderItem(0, colname)
#        print("nach HorizontalHeaderItem")
        colname = QTableWidgetItem("Ausbildungsthema")
#        print("nach colname Ausbildungsthema")
        self.tw_suchen.setHorizontalHeaderItem(0, colname)
#        print("nach setHorizontalHeaderItem 2")
        colname = QTableWidgetItem("Ausbilder")
        self.tw_suchen.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Benutzername")
        self.tw_suchen.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Änderungsdatum")
        self.tw_suchen.setHorizontalHeaderItem(3, colname)



        self.tw_suchen.setRowCount(1)
#        print("nach RowCount 1")
        sql = "SELECT Ausbildungsthema, Ausbilder, Benutzername, Aenderungsdatum from kat_ausbildungsthemen WHERE concat(Ausbildungsthema, Ausbilder, Benutzername, Aenderungsdatum) like'" + '%' + self.le_suche.text() + '%' "'"
#        print("nach Select")
        mycursor = db.select(sql)
        #mycursor.fetchall()
#        print("nach db.select")
        if mycursor == "backtologin":
#            print("nach mycursor backtologin")
            self.back_to_login()
#            print("nach self.backtologin")
            return
#            print("nach return")
        zeile = 0
        #print("nach Zeile = 0")
        for z in mycursor:
            #print("for z in mycursor")
            for s in range(0,  4):
                if s == 3:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.tw_suchen.setItem(zeile,  s,  fielditem)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tw_suchen.setRowCount(zeile+1)
                self.tw_suchen.setItem(zeile,s ,fielditem)
            zeile += 1
            #print("in range")
            # self.tw_suchen.setRowCount(zeile + 1)
            #print("setRowCount(zeile + 1")
        mycursor.close()
        #print("mycursor.close")
        self.tw_suchen.resizeColumnsToContents()
        #print("1")
        self.tw_suchen.resizeRowsToContents()
        #print("2")
        self.setCursor(Qt.ArrowCursor)
    @pyqtSlot()
    def on_pb_abbrechen_clicked(self):
        self.parent().show()
        self.close()

    @pyqtSlot(int, int)
    def on_tw_suchen_cellClicked(self, row, column):
        self.parent().le_name.setText(self.tw_suchen.item(row, 0).text())
        self.parent().cb_ausbilder.setCurrentText(self.tw_suchen.item(row, 1).text())
    
    
    @pyqtSlot(int, int)
    def on_tw_suchen_cellDoubleClicked(self, row, column):
        self.hide()
