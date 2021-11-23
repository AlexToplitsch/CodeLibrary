# -*- coding: utf-8 -*-

 

"""
Module implementing LAB_Ausbilder.
"""
from PyQt5.QtCore import  Qt,pyqtSlot#,  QDate
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from other.database import Database
from sub.bs.Ui_Bs import Ui_Berufsschule
#from pyreportjasper import JasperPy
#from sub.XML.XML_Class import XML_Class
from tkinter import messagebox
import tkinter as tk
#import os,  time
import datetime
from datetime import date
from sub.bs.Bs_Suche import Suche_Dialog
from sub.XML.XML_Class import DBtoXML
#from datetime import strptime
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
        self.cb_Bs.setCurrentText(" ")
        self.cb_Bs.addItem("Eibiswald")
        self.cb_Bs.addItem("St. Peter")
        self.cb_Bs.addItem("Mureck")
        self.cb_Bs.setCurrentText(" ")
        
        pass

    def tw_Data_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        
        
        self.tw_Data.setColumnCount(8)
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
        colname = QTableWidgetItem("Benutzer")
        self.tw_Data.setHorizontalHeaderItem(6, colname) 
        colname = QTableWidgetItem("Änderung")
        self.tw_Data.setHorizontalHeaderItem(7, colname) 
    
        
        self.tw_Data.setRowCount(1)
        sql = "SELECT * FROM KAT_berufsschulzeit"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        
        zeile = 0
        for z in mycursor: 
            self.tw_Data.setRowCount(zeile+1)
            fielditem = QTableWidgetItem(str(z[0]))
            self.tw_Data .setItem(zeile,  0,  fielditem)
            for s in range(0, 8):
                self.tw_Data.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s+1]))
                self.tw_Data .setItem(zeile,  s,  fielditem)
            
            y, m, d = str(z[2])[0:4], str(z[2])[5:7], str(z[2])[8:10]
                
            today = datetime.date.today()
            ty, tm, td = str(today)[0:4], str(today)[5:7], str(today)[8:10]
            
            if ty > y:
                lj = int(ty) - int(y)
                if tm > m and td > d:
                    lj = int(ty) - int(y) + 1
            else:
                lj = 1
               
            self.tw_Data.setRowCount(zeile+1)
            fielditem1 = QTableWidgetItem(str(lj))
            self.tw_Data .setItem(zeile,  1,  fielditem1)

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
        Schließt das im Moment geöffnete Fenster(Fachrichtungen)
        """
        
        #self.parent().show()
        self.parent().setWindowOpacity(1.0)
        self.close()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
    
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
    
        try:
            self.INFO("Eintrag wurde in der Datenbank  Eingetragen",  "I")# info asugabe
            sql = "UPDATE kat_berufsschulzeit set VonDatum=%s, BisDatum=%s, Berufsschule=%s, Ansprechperson=%s, Benutzer=%s WHERE PERS_NR = '" + self.le_PersNr.text() + "'"
            val = (self.de_Eintritt.text(),  self.de_Austritt.text(),  self.cb_Bs.currentText(),  self.le_Ansprechpartner.text(),  self.parent().label_eingeloggt_als.text())
            print(val)
            print(self.le_PersNr.text())
            db.insert(sql, val)
            self.tw_Data_anzeigen()
        except Exception as e:
            print(e)
        pass
        
        print("lel")

    def on_btHelp_clicked(self):
        """
        Button zum Help Fenster/Datei
        """
    
    def back_to_login(self):
        """
        Zweite methode ins hauptmenu zurück zu kommen 
        """
        self.parent().back_to_login()
        self.close()
        pass
        
    def on_btExcel_clicked(self):
        """
        Erstellt ein XML Datei aus der Datenbank
        """
        self.INFO("Excel-Datei wure erstellt.",  "I")# info asugabe
        db = Database.get_instance(self)
        DBtoXML.MakeXML(db, "kat_berufsschulzeit")
       
        #os.startfile("Excel\kat_bs.xlsx")

        pass
        
    def on_pb_report_clicked(self):
#        
#        try:
#            db = Database.get_instance(self)
#            db.writeSQLite("kat_berufsschulzeit")
#            print("dsadsa")
#            input_file = 'Reports\kat_berufsschulzeit.jasper'
#    #        output = 'MyReports' # Ziel-/SUB-Ordner
#           
#            output = 'Reports\kat_berufsschulzeit'
#            print("asdasdasd")
#            jasper = JasperPy()
#           
#            con={
#            'driver':'generic',
#            'jdbc_driver':'org.sqlite.JDBC',
#            'jdbc_url':'jdbc:sqlite:kat.db'
#            }
#            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])  
#            print("dsa")
#            self.setCursor(Qt.WaitCursor)
#            time.sleep(2)
#            #self.setCursor(Qt.WaitCursor)
#           
#            os.startfile("Reports\kat_berufsschulzeit.pdf")
#            print("asd")
#            
#            self.INFO("Report wurde erstellt.",  "I")# info asugabe
#        except Exception as e:
#            print(e)
#                
#        except Exception:
#            self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
#        
        pass
    
    def on_btLoeschen_clicked(self):
        """
        on_btLoeschen_clicked löscht eine Zeile aus der Tabelle
        """
        db = Database.get_instance(self)
        sql = "select * from KAT_berufsschulzeit WHERE PERS_NR = '" + self.le_PersNr.text() + "'"
        mycursor = db.select(sql)
        today = date.today()
        
        if mycursor == "backtolgin":
            self.back_to_login()
            return
    
        try:
            date_str = today.strftime("%d.%m.%Y")
            print("Löschen")
            print(date_str)
            self.INFO("Eintrag wurde in der Datenbank  Gelöscht",  "I")# info asugabe
            #print(self.de_Eintritt.text()+" 2-->"+ int(self.de_Austritt.text())+" 3-->"+  self.cb_Bs.currentText()+" 4-->"+   self.le_Ansprechpartner.text()+" ")
            sql = "UPDATE kat_berufsschulzeit set VonDatum=%s, BisDatum=%s, Berufsschule=%s, Ansprechperson=%s, Benutzer=%s WHERE PERS_NR = '" + self.le_PersNr.text() + "'"
            val = (date_str,  date_str,  " ",  " ",  self.parent().label_eingeloggt_als.text())
            print(val)
            print(self.le_PersNr.text())
            db.insert(sql, val)
            self.tw_Data_anzeigen()
        except Exception as e:
            print(e)
        pass
        
        print("lel")
        
    def on_pb_suchen_clicked(self):
        """
        Such funktion um Raum in Datenbank zu Suchen
        """
        self.searchWindow = Suche_Dialog(self)
        self.searchWindow.show()
        
        pass
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
        today = date.today()
        
        if self.tw_Data.item(row,  2). text() == "None":
            date_str = today.strftime("%d.%m.%Y")
            self.de_Eintritt.setDate(datetime.datetime.strptime(date_str, '%d.%m.%Y').date())
        else:
            date_str = self.tw_Data.item(row,  2).text()
            EINTRITTS_DATUM = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
            self.de_Eintritt.setDate(EINTRITTS_DATUM)
        
        if self.tw_Data.item(row,  3). text() == "None":
            date_str = today.strftime("%d.%m.%Y")
            self.de_Austritt.setDate(datetime.datetime.strptime(date_str, '%d.%m.%Y').date())
        else:
            date_str = self.tw_Data.item(row,  3).text()
            AUSTRITTS_DATUM = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
            self.de_Austritt.setDate(AUSTRITTS_DATUM)
            
        #date_str = self.tw_Data.item(row,  5).text()
        self.le_PersNr.setText(self.tw_Data.item(row,  0).text())

        self.cb_Bs.setCurrentText(self.tw_Data.item(row,  4).text())
        self.le_Ansprechpartner.setText(self.tw_Data.item(row,  5).text())
        #raise NotImplementedError
