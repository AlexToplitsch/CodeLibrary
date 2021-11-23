#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5 import QtGui
#from pyreportjasper import  JasperPy
import sys
import subprocess
import os
#import os 
#import hashlib
#import secrets
import bcrypt
#from captcha.image import ImageCaptcha
from configparser import ConfigParser

import mysql.connector
from Ui_users import Ui_Dialog

def SetEnabled(listOfCheckboxes):
    for s in range(0, len(listOfCheckboxes)):
        listOfCheckboxes[s].setChecked(True)


class Users(QDialog, Ui_Dialog):
    """
    Klasse zum Verwalten der Nutzer
    """
    mydb = ""
    dict = {}
    def DisableCheckboxes(self):
        for s in range(0, len(self.dict)):
            self.dict[s]["checkboxes"].setChecked(False)
        
    def __init__(self, parent=None):

        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Users, self).__init__(parent)
        self.setupUi(self)
        
        config_object = ConfigParser()
        config_object.read("config.ini")

        #Get the USERINFO section
        database = config_object["DATABASE"]
        
        try:
            self.mydb=mysql.connector.connect(
            host = database["host"],
            user = "root",
            passwd = "knapp22",
            db = database["database"]
            
        )
        except:
            print("Keine Verbindung zum Server möglich")
            exit(0)
        self.tableAnzeigen()
        self.dict = [ 
        {"number" : 1, "checkboxes":self.cbStammdaten}, 
        {"number" : 2, "checkboxes":self.cbBewegungsdaten}, 
        {"number" : 4, "checkboxes":self.cbAuswertungen}]
        #{"number" : "6", "checkboxes":[self.cbStammdaten, self.cbWochenplan]}]
        self.btnSpeichern.setEnabled(False)
        ##---------------CAPTCHA-------------------
        #from PIL import Image, ImageDraw, ImageFont
        #image = ImageCaptcha(width=100, height=30, font_sizes=[30])

        #data = image.generate("COOL")
        #captcha_image = Image.open(data)
        #ImageDraw.Draw(captcha_image)
        #captcha_image.show()
        ##---------------------------------------------
    @pyqtSlot()
    def on_btnAbbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.parent().setWindowOpacity(1.0)
        self.close()
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
        
    def tableAnzeigen(self):
        """
        Methode zum befüllen der Spalten aus der Datenbank ins QTableWidget
        """
        
        self.setCursor(Qt.WaitCursor)
        
        self.table.setColumnCount(3)
        colname=QTableWidgetItem("ID")
        self.table.setHorizontalHeaderItem(0,  colname)
        colname=QTableWidgetItem("Benutzername")
        self.table.setHorizontalHeaderItem(1,  colname)
    
    
#        colname=QTableWidgetItem("Passwort")
#        self.table.setHorizontalHeaderItem(2,  colname)
#        colname=QTableWidgetItem("PasswortSalt")
#        self.table.setHorizontalHeaderItem(3,  colname)
        colname=QTableWidgetItem("Rechte")
        self.table.setHorizontalHeaderItem(2,  colname)

        
        self.table.setRowCount(1)
        #sql = "SELECT ID, Benutzername, Passwort, PasswortSalt, Rechte FROM kat_nutzer ORDER BY ID"
        sql = "SELECT ID, Benutzername, Rechte FROM kat_nutzer ORDER BY ID"

        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        zeile=0
        
        for z in mycursor:
            for s in range(0, 3):
                self.table.setRowCount(zeile+1)
                #if s == 2 or s == 3:
                #    item = str(type(z[s]))
                #else:
                item = str(z[s])
                fielditem = QTableWidgetItem(item)
                if zeile % 2 == 0:
                    fielditem.setBackground(QColor(210, 210, 210))
                self.table.setItem(zeile, s, fielditem)
            zeile += 1
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
        #self.setTableWidth()
    
    @pyqtSlot()
    def on_btnSpeichern_clicked(self):
        """
        Slot documentation goes here.
        """
        
        
        self.setCursor(Qt.WaitCursor)
        
        #salt = os.urandom(32)
        #salt = secrets.token_bytes(32   )
        salt = bcrypt.gensalt(12)
        password = self.lePasswort.text()
        
        key = bcrypt.hashpw(password.encode(), salt)#hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 50000, dklen=32)  # It is recommended to use at least 100,000 iterations of SHA-256 
        
        rechte = 0
        #---------------------------RECHTE--------------------------
            #---------------Rechteliste---------------------------
            #            
            #            1 = Test
            #            2 = Stammdaten
            #            4= Wochenplan
            #            
            #            6 = Stammdaten + Wochenplan
            #            
            #-------------------------------------------------------
#        if self.cbAdmin.isChecked():
#            rechte += 1
#        if self.cbStammdaten.isChecked():
#            rechte += 2
#        if self.cbWochenplan.isChecked():
#            rechte += 4
        if self.cbStammdaten.isChecked():
            rechte += 1
        if self.cbBewegungsdaten.isChecked():
            rechte += 2
        if self.cbAuswertungen.isChecked():
            rechte += 4
        #---------------------------------------------------------------
        mycursor = self.mydb.cursor()
        sql_satz = []
        sql = "select * from kat_nutzer WHERE Benutzername = '"+ self.leBenutzername.text() + "'"
        mycursor.execute(sql)
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        if satz_len == 0:
            sql = 'INSERT INTO kat_nutzer(Benutzername,Passwort,PasswortSalt,Rechte) VALUES (%s, %s, %s, %s)'
            val = (self.leBenutzername.text(), key,  salt, rechte)
            #print(salt)
            #print(salt.decode('utf-8', 'ignore'))
            print(key)
            
            #print("KEY: "+str(password.encode('utf-8'))
        else:
            sql = "UPDATE kat_nutzer set Benutzername=%s, Passwort=%s, PasswortSalt=%s, Rechte=%s" +  " where Benutzername = '"  + self.leBenutzername.text() + "'" 
            val = (self.leBenutzername.text(), key,  salt, rechte)
        try:
            result = mycursor.execute(sql, val)
            print(result)
            self.mydb.commit()
            print("Datensatz wurde erfolgreich in DB-Tabelle kat_nutzer eingetragen/geändert")
            #self.txtINFO.setText("Datensatz wurde erfolgreich in DB-Tabelle <ADRESSEN> eingetragen/geändert")
        except mysql.connector.Error as error:
            #'print(result)
            print("Datensatz konnte nicht in DB-Tabelle kat_nutzer eingetragen/geändert werden {}".format(error))
            #self.txtINFO.setText("Datensatz konnte nicht in DB-Tabelle <ADRESSEN> eingetragen/geändert werden {}".format(error))
        self.tableAnzeigen()
        self.lePasswort.setText("")
        self.leBenutzername.setText("")
    
    @pyqtSlot(int, int)
    def on_table_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        #Checkboxen alle deaktivieren
        self.DisableCheckboxes()
        #----------------------------------
        self.leBenutzername.setText(self.table.item(row, 1).text())
        
        for i in range(0, len(self.dict)):
            #print(self.dict[i]["number"])
            if int(self.table.item(row, 2).text()) & self.dict[i]["number"]:
                self.dict[i]["checkboxes"].setChecked(True)
    
    @pyqtSlot()
    def on_btnAnmelden_clicked(self):
        """
        Slot documentation goes here.
        """
        mycursor = self.mydb.cursor()
        sql ="select * from kat_nutzer WHERE Benutzername = '" + self.leBenutzername.text() + "'"
        mycursor.execute(sql)
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        if satz_len == 0:
            print("Nutzer gibt es nicht")
            return
        #========COMPARISON==========================
        storedSalt = sql_satz[0][3]
        storedPassword = sql_satz[0][2]
        print(sql_satz[0])
        #print(storedSalt)
        
        #print("STORED SALT " + storedSalt)
        #print("STORED PASSWORD "+storedPassword)
        
        key = bcrypt.hashpw(self.lePasswort.text().encode(), storedSalt.encode()) #hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 50000, dklen=32)  # It is recommended to use at least 100,000 iterations of SHA-256 
        #print("CURRENT HASHED "+ str(str(key).encode('utf-8')))
        #print("STORED HASED "+ storedPassword)
        #print(key)
        #print(storedPassword.encode('utf-8'))
        #print(str(key))
        #print(storedPassword[0])
        #print(key.decode('utf-8', 'ignore')[0])
        #print(key.decode('utf-8', 'ignore'))
        print(key)
        print(storedPassword.encode())
        
        if key == storedPassword.encode():
            print('You have logged in successfully!')
        else:
            print('Something went wrong')
        #print(storedSalt)
    def Validation(self):
        flag = 0
        containsNum = 0
        containsSpecial = 0
        #Zahl in Passwort
        for char in self.lePasswort.text():
            if char.isdigit():
                containsNum += 1
            
        #Sonderzeichen in Passwort/Benutzername    
        if not self.lePasswort.text().isalnum() or not self.leBenutzername.text().isalnum():
            containsSpecial=True
        
        #print(containsNum == False)
        #print(containsSpecial == True)
        if containsNum != 1:
            flag-=1
        if containsSpecial == True:
            flag-=1

        #Ob Leezeichen drin ist
        if " " in self.lePasswort.text() or " " in self.leBenutzername.text():
            flag-=1
        #Länge checken
        if len(self.lePasswort.text()) <= 7 or len(self.leBenutzername.text()) <= 3:
            flag-=1
        
        if flag == 0:
            self.btnSpeichern.setEnabled(True)
        else:
            self.btnSpeichern.setEnabled(False)
        #print(flag)
    @pyqtSlot(str)
    def on_lePasswort_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.Validation()
    
    @pyqtSlot(str)
    def on_leBenutzername_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.Validation()
    
    @pyqtSlot()
    def on_btnLoeschen_clicked(self):
        """
        Slot documentation goes here.
        """
        sql = "DELETE FROM kat_nutzer WHERE Benutzername= '" + self.leBenutzername.text() + "'"
        
        #print("Nach SQL Befehl")
        cursor = self.mydb.cursor()
        cursor.execute(sql)
        self.mydb.commit()
        
        self.leBenutzername.setText("")
        self.lePasswort.setText("")
        self.DisableCheckboxes()
        self.tableAnzeigen()
        cursor.close()
        
        
        
        
        
        
        


#app = QApplication(sys.argv)
#ui = Users() #Name des UI Fensters
#ui.show()
#sys.exit(app.exec_())
