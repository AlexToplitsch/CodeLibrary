# -*- coding: utf-8 -*-

"""
Module implementing Ausbilder_suchen.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog


from sub.trainer.Ui_Ausbilder_suchen import Ui_Ausbilder_suchen


class Ausbilder_suchen(QDialog, Ui_Ausbilder_suchen):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Ausbilder_suchen, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pb_cancel_clicked(self):
        self.parent().show()
        self.close()
        
#app = QApplication(sys.argv)
#ui = Ausbilder_suchen() #Name der bei der Anlage der Dialog-Klasse verwendet wurde
#ui.show()
#sys.exit(app.exec_())
