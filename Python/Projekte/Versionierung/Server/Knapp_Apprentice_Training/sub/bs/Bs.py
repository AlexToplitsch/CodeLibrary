# -*- coding: utf-8 -*-

 

"""
Module implementing LAB_Ausbilder.
"""
from PyQt5.QtCore import  Qt,pyqtSlot#,  QDate
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from other.database import Database
from sub.bs.Ui_Bs import Ui_Berufsschule
#from sub.XML.XML_Class import XML_Class
from sub.XML.XML_Class import DBtoXML
from tkinter import messagebox
import tkinter as tk
import os,  datetime
from datetime import date
#from PyQt5 import QtCore
#import ctypes
#from tkinter import simpledialog




class Bs(QDialog, Ui_Berufsschule):
    """
    Class documentation goes here.
    """
    

    def __init__(self, parent=None):
        super(Bs, self).__init__(parent)
        self.setupUi(self)
        self.tw_Data_anzeigen()  
        
        pass

    def tw_Data_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        self.cb_Bs.setCurrentText(" ")
        self.cb_Bs.addItem("Eibiswald")
        self.cb_Bs.addItem("St. Peter")
        self.cb_Bs.addItem("Mureck")
        self.cb_Bs.setCurrentText(" ")
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        
        
        self.tw_Data.setColumnCount(7)
        colname = QTableWidgetItem("Personal Nummer")
        self.tw_Data.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Lehrjahr")
        self.tw_Data.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Von-Datum")
        self.tw_Data.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Bis-Datum")
        self.tw_Data.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Berufschule")
        self.tw_Data.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Ansprechperson")
        self.tw_Data.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Zeugnisse")
        self.tw_Data.setHorizontalHeaderItem(6, colname) 
    
        
        self.tw_Data.setRowCount(1)
        sql = "SELECT * FROM KAT_berufsschulzeit"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        
        zeile = 0
        for z in mycursor: 
            y, m, d = str(z[2])[0:4], str(z[2])[5:7], str(z[2])[8:10]
            print(y +" -> "+m+" -> "+d)
                
            today = date.today()
            ty, tm, td = str(today)[0:4], str(today)[5:7], str(today)[8:10]
            print(ty +" -> "+tm+" -> "+td)
            
            if ty > y:
                lj = int(ty) - int(y)
                if tm > m and td > d:
                    lj = int(ty) - int(y) + 1
            else:
                lj = 1
               
            print(lj)
            self.tw_Data.setRowCount(zeile+1)
            fielditem1 = QTableWidgetItem(str(lj))
            self.tw_Data .setItem(zeile,  1,  fielditem1)

            self.tw_Data.setRowCount(zeile+1)
            fielditem = QTableWidgetItem(str(z[0]))
            self.tw_Data .setItem(zeile,  0,  fielditem)
            for s in range(0, 7):
                self.tw_Data.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s+1]))
                self.tw_Data .setItem(zeile,  s,  fielditem)
            zeile += 1
        
        mycursor.close()
        
        #mycursor.close()
        
        self.tw_Data.resizeColumnsToContents()
        self.tw_Data.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)    
        
    def on_btHp_clicked(self):
        """
        Geht zurück isn Hauptmenu
        """
        self.parent().show()
        self.close()
        
    def on_bt_clear_clicked(self):
        """ 
        Slot documentation goes here.
        """
        date = datetime.datetime.now()
        self.le_PersNr.setText("")
        self.de_Eintritt.setDate(date)
        self.de_Austritt.setDate(date)
        self.cb_Bs.setCurrentText(" ")
        self.le_Ansprechpartner.setText("")
        
        pass
    
    def closeEvent(self, event):
        """
        Geht zurück isn Hauptmenu
        """
        self.parent().show()
        self.INFO("Zurück im Hauptmenu",  "I")# info asugabe
        pass
    
    def on_btSpeichern_clicked(self):
        """
        Speichert den Neuen wert in die Datenbank
        """
        
        db = Database.get_instance(self)
        sql = "select * from KAT_berufsschulzeit WHERE PERS_NR = '" + self.le_PersNr.text() + "'"
        mycursor = db.select(sql)
        
        if mycursor == "backtolgin":
            self.back_to_login()
            return
        
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        
        print(satz_len,  sql)
        try:
            
            print("update")
            self.INFO("Eintrag wurde in der Datenbank  Aktualisiert",  "I")# info asugabe
            sql = "UPDATE kat_berufsschulzeit set Von-Datum=%s, Bis-Datum=%s, Berufsschule=%s, Anpsrechperson=%s WHERE PERS_NR = '" + self.le_PersNr.text() + "'"
            val = (self.de_Eintritt.text(),  int(self.de_Austritt.text()),  self.cb_Bs.currentText(),  self.le_Ansprechpartner.text().label_eingeloggt_als.text())
            db.insert(sql, val)
            self.twData_anzeigen()
        except:


            messagebox.showinfo("Information",  "Bitte geben sie alle Infomationen ein")
        
        pass
        
    def on_btHelp_clicked(self):
        """
        Button zum Help Fenster/Datei
        """
    
    def back_to_login(self):
        """
        Zweite methode ins hauptmenu zurück zu kommen 
        """
        self.parent().bacl_to_login()
        self.close()
        pass
        
    def on_btExcel_clicked(self):
        """
        Erstellt ein XML Datei aus der Datenbank
        """
        self.INFO("Excel-Datei wure erstellt.",  "I")# info asugabe
        db = Database.get_instance(self)
        DBtoXML.MakeXML(db, "kat_Bs")
       
        os.startfile("Excel\kat_Bs.xlsx")
        pass
    
    def on_btLoeschen_clicked(self):
        """
        on_btLoeschen_clicked löscht eine Zeile aus der Tabelle
        """
        db = Database.get_instance(self)
        sql = "DELETE FROM KAT_berufsschulzeit WHERE PERS_NR = '" + self.lePersNr.text() + "'"
        db.delete(sql)
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe
        self.twAnzeigen()

    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        root = tk.Tk()
        root.withdraw()
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
            messagebox.showerror("Fehler", MELDUNG)
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
                messagebox.showwarning("Hinweis/Warnung", MELDUNG)
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
    
    @pyqtSlot(int, int)
    def on_tw_Data_cellClicked(self, row, column):
        """
        Ausgwähltes objeckt aufrufen
        """
      #  AUSTRITTS_DATUM = datetime.datetime.strptime(self.tw_Data.item(row,  2).text(),  "%d.%m.%Y")
     #   EINTRITTS_DATUM = datetime.datetime.strptime(self.tw_Data.item(row,  3).text(),  "%d.%m.%Y")
#        print(datetime.date.today().strftime("%d.%m.%Y"))
#        self.le_PersNr.setText(self.tw_Data.item(row,  0).text())
#        self.de_Eintritt.setDate(EINTRITTS_DATUM)
#        self.de_Austritt.setDate(AUSTRITTS_DATUM)
#        self.cb_Bs.setText(self.tw_Data.item(row,  1).text())
#        self.le_Ansprechpartner.setText(self.tw_Data.item(row,  4).text())
#        raise NotImplementedError
