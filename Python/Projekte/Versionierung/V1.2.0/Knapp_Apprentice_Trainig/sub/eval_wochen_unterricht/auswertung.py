# -*- coding: utf-8 -*-

"""
Module implementing Auswertung.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from other.database import Database


from Ui_auswertung import Ui_Auswertung


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
        cb_ausb_befuellen()
        cb_unter_befuellen()
        super(Auswertung, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(self)
    def cb_ausb_befuellen(self):
        db = Database.get_instance(self)
        sql = "SELECT Ausbiler FROM kat_wochen_unterricht"
        mycursor = db.select(sql)
        ausbilder = []
        for i in mycursor:
            ausbilder.append(i[0])
        
        self.cb_ausbilder.addItems(ausbilder)
        self.cb_ausbilder.addItem("")
        
    @pyqtSlot(self)
    def cb_unter_befuellen(self):
        db = Database.get_instance(self)
        sql = "SELECT Unterrichtsthema FROM kat_wochen_unterricht"
        mycursor = db.select(sql)
        thema = []
        for i in mycursor:
            thema.append(i[0])
        
        self.cb_unterrichtsthema.addItems(ausbilder)
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
