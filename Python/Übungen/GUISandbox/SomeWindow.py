# -*- coding: utf-8 -*-

"""
Module implementing Hauptmaske.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_SomeWindow import Ui_Dialog


class Hauptmaske(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Hauptmaske, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushBtn_pushme_clicked(self):
        print("Hallo")
