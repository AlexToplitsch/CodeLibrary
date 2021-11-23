# -*- coding: utf-8 -*-

"""
Module implementing passwortAendern.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5 import QtGui


import bcrypt
from configparser import ConfigParser
from other.database import Database
from sub.passwortAendern.Ui_passwortAendern import Ui_Dialog

import mysql.connector
class passwortAendern(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(passwortAendern, self).__init__(parent)
        self.setupUi(self)
        

        self.le_Benutzername.setText(self.parent().parent().benutzername)
            
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
    def Validation(self):
        flag = 0
        containsNum = 0
        containsSpecial = 0
        #Zahl in Passwort
        for char in self.le_neuesPasswort.text():
            if char.isdigit():
                containsNum += 1
            
        #Sonderzeichen in Passwort/Benutzername    
        if not self.le_neuesPasswort.text().isalnum():
            containsSpecial=True
        
        #print(containsNum == False)
        #print(containsSpecial == True)
        if containsNum != 1:
            flag-=1
        if containsSpecial == True:
            flag-=1

        #Ob Leezeichen drin ist
        if " " in self.le_neuesPasswort.text():
            flag-=1
        #Länge checken
        if len(self.le_neuesPasswort.text()) <= 7:
            flag-=1
        
        if flag == 0:
            self.pushButton_aendern.setEnabled(True)
        else:
            self.pushButton_aendern.setEnabled(False)
        #print(flag)
    
    @pyqtSlot()
    def on_pushButton_aendern_clicked(self):
        """
        Slot documentation goes here.
        """
        db = Database.get_instance(self)
        ##ALTES PW
        #db = Database.get_instance(self)
        sql = "select * from kat_nutzer WHERE Benutzername = '"+ self.le_Benutzername.text() + "'"
        mycursor = db.select(sql)
        mycursor.execute(sql)
        sql_satz = mycursor.fetchall()
        #satz_len = len(sql_satz)
        
        storedSalt = sql_satz[0][3]
        storedPassword = sql_satz[0][2]
        print(sql_satz[0])
        
        key = bcrypt.hashpw(self.le_altesPasswort.text().encode(), storedSalt.encode()) #hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 50000, dklen=32)  # It is recommended to use at least 100,000 iterations of SHA-256 

        print(storedPassword.encode())
        
        if key == storedPassword.encode():
            print('Passwort stimmt überein')
        else:
            print('Something went wrong')
        ##ALTES PW
        
        ##NEUES PW
        salt = bcrypt.gensalt(12)
        password = self.le_neuesPasswort.text()
        
        key = bcrypt.hashpw(password.encode(), salt)
        
        sql = "UPDATE kat_nutzer set Passwort=%s, PasswortSalt=%s" +  " where Benutzername = '"  + self.le_Benutzername.text()+ "'" 
        val = (key, salt)
        try:
            result = db.insert(sql, val)
            print(result)
            #self.mydb.commit()
            print("Datensatz wurde erfolgreich in DB-Tabelle kat_nutzer eingetragen/geändert")
            self.parent().setWindowOpacity(1.0)
            self.parent().back_to_login()
            self.close()
            #self.txtINFO.setText("Datensatz wurde erfolgreich in DB-Tabelle <ADRESSEN> eingetragen/geändert")
        except mysql.connector.Error as error:
            #'print(result)
            print("Datensatz konnte nicht in DB-Tabelle kat_nutzer eingetragen/geändert werden {}".format(error))
            #self.txtINFO.setText("Datensatz konnte nicht in DB-Tabelle <ADRESSEN> eingetragen/geändert werden {}".format(error))
        ##NEUES PW
    
    @pyqtSlot(str)
    def on_le_neuesPasswort_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        self.Validation()
