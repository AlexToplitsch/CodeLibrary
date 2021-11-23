# -*- coding: utf-8 -*-

"""
Module implementing LoginSettings.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from sub.login.Ui_login_settings import Ui_LoginSettings
from configparser import ConfigParser

class LoginSettings(QDialog, Ui_LoginSettings):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LoginSettings, self).__init__(parent)
        self.setupUi(self)
        self.daten_auslesen()
        
    def daten_auslesen(self):
        
        #Read config.ini file
        config_object = ConfigParser()
        config_object.read("config.ini")

        #Get the password
        database = config_object["DATABASE"]
        self.lineEdit_host.setText(database["host"])
        self.lineEdit_database.setText(database["database"])
    
    @pyqtSlot()
    def on_pushButton_abbrechen_clicked(self):
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pushButton_speichern_clicked(self):
        #Read config.ini file
        config_object = ConfigParser()
        config_object.read("config.ini")

        #Get the USERINFO section
        database = config_object["DATABASE"]
        

        #Update the password
        database["host"] =  self.lineEdit_host.text()
        database["database"] =  self.lineEdit_database.text()

        #Write changes back to file
        with open('config.ini', 'w') as conf:
            config_object.write(conf)
        
        self.parent().show()
        self.close()
