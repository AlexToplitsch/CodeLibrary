# -*- coding: utf-8 -*-

"""
Module implementing anwesenheit.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from sub.wochen_unterricht.Ui_Anwesenheit import Ui_Dialog


class anwesenheit(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(anwesenheit, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_Speichern_Abwesenheit.setEnabled(False)
    
    @pyqtSlot(int)
    def on_checkBox_Alle_Anwesend_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Speichern_Abwesenheit_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_Speichern_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
