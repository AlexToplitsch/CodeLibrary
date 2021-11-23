# -*- coding: utf-8 -*-

"""
Module implementing Lehrlingseinteilung_App.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QMessageBox

import datetime

from sub.rotation.Ui_Lehrlingseinteilung import Ui_Lehrlingseinteilung


class Lehrlingseinteilung_App(QDialog, Ui_Lehrlingseinteilung):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrlingseinteilung_App, self).__init__(parent)
        self.setupUi(self)
        self.actualDate = str(datetime.datetime.now().date())
        self.date1 = int(self.actualDate[:4])
        self.date2 = self.date1 -1
        
    
    @pyqtSlot()
    def on_pB_leftArrow_clicked(self):
        """
        Slot documentation goes here.
        """
        self.date1 -= 1
        self.date2 -= 1
        self.lbl_Ausbildungjahr.setText(str(self.date2) +"/" + str(self.date1))
        #self.twData_anzeigen()
        
        
    @pyqtSlot()
    def on_pB_rightArrow_clicked(self):
        """
        Slot documentation goes here.
        """
        self.date1 += 1
        self.date2 += 1
        self.lbl_Ausbildungjahr.setText(str(self.date2) +"/" + str(self.date1))
        #self.twData_anzeigen()
    
    @pyqtSlot(str)
    def on_cB_Lehrling_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(str)
    def on_cB_Fachabteilung_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(int, int)
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
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pB_Speichern_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pB_Abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().show()
        self.close()
    
    
    @pyqtSlot()
    def on_pB_Hilfe_clicked(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(
        self,
        self.tr("Hilfe"),
        self.tr("""Die Hilfefunktion wird demnächst Hinzugefügt!"""))
    
    def setAusbildungswoche(self,  woche): #woche fängt bei 6 an weil Spaltennummer
        if woche < 6:
            kw =34
        else:
            kw = int(woche) +28
            
        if kw > 53:
            kw = kw - 53
        self.sB_Ausbildungswoche.setValue(kw) 
