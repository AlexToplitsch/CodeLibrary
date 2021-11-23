# -*- coding: utf-8 -*-

"""
Module implementing Auswertung.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from other.database import Database



from sub.eval_wochen_unterricht.Ui_AW_Wochen_Unterricht import Ui_Auswertung


class Auswertung(QDialog, Ui_Auswertung):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """

        super(Auswertung, self).__init__(parent)
        self.setupUi(self)
        self.ch_bewertung.setEnabled(False)
        self.cb_ausb_befuellen()
        self.cb_unter_befuellen()
    
    @pyqtSlot()
    def cb_ausb_befuellen(self):
        db = Database.get_instance(self)
        sql = "SELECT Familienname FROM kat_ausbilder"
        mycursor = db.select(sql)
        ausbilder=[]
        for i in mycursor:
            ausbilder.append(i[0])
        self.cb_ausbilder.addItems(ausbilder)
        self.cb_ausbilder.addItem("")
        
    @pyqtSlot()
    def tw_anzeigen(self):
        db = Database.get_instance(self)
        
        self.setCursor(Qt.WaitCursor)
        self.tw_Table.setColumnCount(4)
        
        colname = QTableWidgetItem("Ausbilder")
        self.tw_Table.setHorizontalHeaderItem(0,  colname)
        colname = QTableWidgetItem("Ausbildungsthema")
        self.tw_Table.setHorizontalHeaderItem(1,  colname)
        colname = QTableWidgetItem("Datum")
        self.tw_Table.setHorizontalHeaderItem(2,  colname)
        colname = QTableWidgetItem("Teilnehmer")
        self.tw_Table.setHorizontalHeaderItem(3,  colname)
        
        sql = "SELECT ausbilder, unterrichtsthema, datum, lehrlinge FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "'"
           
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
    def tw_anzeigen2(self):
        db = Database.get_instance(self)
        
        self.setCursor(Qt.WaitCursor)
        self.tw_Table.setColumnCount(3)
        
        colname = QTableWidgetItem("Ausbilder")
        self.tw_Table.setHorizontalHeaderItem(0,  colname)
        colname = QTableWidgetItem("Ausbildungsthema")
        self.tw_Table.setHorizontalHeaderItem(1,  colname)
        colname = QTableWidgetItem("Datum")
        self.tw_Table.setHorizontalHeaderItem(2,  colname)
        
        
        sql = "SELECT ausbilder, unterrichtsthema, datum FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "'"
           
        mycursor=db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  3):
                self.tw_Table.setRowCount(zeile +1)
                fielditem=QTableWidgetItem(str(z[s]))
                self.tw_Table.setItem(zeile, s, fielditem)
            zeile+=1
        self.tw_Table.resizeColumnsToContents()
        self.tw_Table.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
        
    @pyqtSlot()
    def cb_unter_befuellen(self):
        db = Database.get_instance(self)
        sql = "SELECT Unterrichtsthema FROM kat_wochen_unterricht"
        mycursor = db.select(sql)
        thema = []
        for i in mycursor:
            thema.append(i[0])
        
        self.cb_unterrichtsthema.addItems(thema)
        self.cb_unterrichtsthema.addItem("")
    
    
    @pyqtSlot(int,  int)
    def on_tableWidget_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(bool)
    def on_btn_suchen_clicked(self):
        if self.ch_teilnehmer.isChecked() == True:
            self.tw_anzeigen()
        else:
            self.tw_anzeigen2()
    

    @pyqtSlot(int)
    def on_ch_teilnehmer_stateChanged(self, p0):
        if self.ch_teilnehmer.isChecked() == True:
                self.ch_bewertung.setEnabled(True)
        else:
            self.ch_bewertung.setEnabled(False)
