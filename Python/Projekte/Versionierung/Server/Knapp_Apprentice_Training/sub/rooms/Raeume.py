# -*- coding: utf-8 -*-

 

"""
Module implementing LAB_Ausbilder.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidgetItem
from other.database import Database
from sub.rooms.Ui_Raeume import Ui_Raeume
#from sub.XML.XML_Class import XML_Class
from sub.XML.XML_Class import DBtoXML
from tkinter import messagebox
import tkinter as tk
import os,  time
from pyreportjasper import JasperPy
#from PyQt5 import QtCore
from sub.rooms.Raeume_Suche import Suche_Dialog
#import ctypes
#from tkinter import simpledialog

root = tk.Tk()



class Raeume(QDialog, Ui_Raeume):
    """
    Class documentation goes here.
    """


    def __init__(self, parent=None):
        super(Raeume, self).__init__(parent)
        self.setupUi(self)
        self.twData_anzeigen()  
        pass
    @pyqtSlot() 
        
    def twData_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        self.twData.setColumnCount(7)
        colname = QTableWidgetItem("Raum")
        self.twData.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Gebäude")
        self.twData.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Stock")
        self.twData.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("RaumNr")
        self.twData.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Plätze")
        self.twData.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Benutzer")
        self.twData.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Änderung")
        self.twData.setHorizontalHeaderItem(6, colname)
        
        
        self.twData.setRowCount(1)
        sql = "SELECT raum,gebäude,stock,raumnr,plätze,benutzer,änderung FROM KAT_raeume"
        mycursor = db.select(sql)
        if mycursor == "backtolgin":
            self.back_to_login()
            return
            
        zeile = 0
        for z in mycursor: 
            for s in range(0, 7):
                self.twData.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.twData .setItem(zeile,  s,  fielditem)
            zeile += 1
        
        mycursor.close()
        
        self.twData.resizeColumnsToContents()
        self.twData.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        #self.INFO("Alle Adressen werden in Tabelle angezeigt",  "I")
        
        pass
    
    @pyqtSlot(int, int)
    def on_cbRaum_currentTextChanged(self, p0):
        """
        Ausgewähltes Objekt in Labels angezeigt.
        """
        db = Database.get_instance(self)
        sql = 'Select * from KAT_raeume where Raum = "' + self.cbRaum.currentText() +'"'
        mycursor = db.select(sql)
        if mycursor == "backtolgin":
            self.back_to_login()
            return
        sql_satz = []
        sql_satz = mycursor.fetchall()

        self.leRaum.setText(sql_satz[0][1])
        self.leGebaeude.setText(sql_satz[0][2])
        self.leStock.setText(str(sql_satz[0][3]))
        self.leRaumNr.setText(sql_satz[0][4])
        self.lePlaetze.setText(sql_satz[0][5])
        
        pass
    
    @pyqtSlot(int, int)
    def on_twData_cellClicked(self, row, column):
        """
        Ausgwähltes objeckt aufrufen
        """
        self.leRaum.setText(self.twData.item(row,  0).text())
        self.leGebaeude.setText(self.twData.item(row,  1).text())
        self.leStock.setText(self.twData.item(row,  2).text())
        self.leRaumNr.setText(self.twData.item(row,  3).text())
        self.lePlaetze.setText(self.twData.item(row,  4).text())
        
        pass
    
    @pyqtSlot()
    def on_btHp_clicked(self):
        """
        Geht zurück isn Hauptmenu
        """
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pb_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        self.leGebaeude.setText("")
        self.lePlaetze.setText("")
        self.leRaum.setText("")
        self.leRaumNr.setText("")
        self.leStock.setText("")
        
        pass
        
    def closeEvent(self, event):
        """
        Geht zurück isn Hauptmenu
        """
        self.parent().show()
        self.INFO("Zurück im Hauptmenu",  "I")# info asugabe
        pass
    
    @pyqtSlot()
    def on_btSpeichern_clicked(self):
        """
        Speichert den Neuen wert in die Datenbank
        """
        
        db = Database.get_instance(self)
        sql = "select * from KAT_raeume WHERE Raum = '" + self.leRaum.text() + "'"
        mycursor = db.select(sql)
        
        if mycursor == "backtolgin":
            self.back_to_login()
            return
        
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        
        print(satz_len,  sql)
        try:
            if satz_len == 0:
                print("insert")
                self.INFO("Eintrag wurde in die Datenbank gespeichert",  "I")# info asugabe
                sql = "INSERT INTO KAT_raeume (Raum, Gebäude, Stock, RaumNr, Plätze, Benutzer) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (self.leRaum.text(),  self.leGebaeude.text(),  int(self.leStock.text()),  self.leRaumNr.text(),  self.lePlaetze.text(), self.parent().label_eingeloggt_als.text())
            else:
                print("update")
                self.INFO("Eintrag wurde in der Datenbank  Aktualisiert",  "I")# info asugabe
                sql = "UPDATE KAT_raeume set Gebäude=%s, Stock=%s, RaumNr=%s, Plätze=%s, Benutzer=%s WHERE Raum = '" + self.leRaum.text() + "'"
                val = (self.leGebaeude.text(),  int(self.leStock.text()),  self.leRaumNr.text(),  self.lePlaetze.text(), self.parent().label_eingeloggt_als.text())
            db.insert(sql, val)
            self.twData_anzeigen()
        except:
            messagebox.showinfo("Information",  "Bitte geben sie alle Infomationen ein")
        
        pass
    
    @pyqtSlot()
    def on_btHelp_clicked(self):
        """
        Button zum Help Fenster/Datei
        """
        
    
    @pyqtSlot()
    def on_btLoeschen_clicked(self):
        """
        Löscht den Ausgwählten Raum aus der Datenbank
        """
        self.INFO("Ausgwählter eintrag wurde aus der Datenbank gelöscht",  "I")# info asugabe
        db = Database.get_instance(self)
        sql = "DELETE FROM KAT_raeume WHERE Raum = '" + self.leRaum.text() + "'"
        db.delete(sql)
        
        self.twData_anzeigen()
    
    @pyqtSlot()
    def on_btSearch_clicked(self):
        """
        Such funktion um Raum in Datenbank zu Suchen
        """
        self.searchWindow = Suche_Dialog(self)
        self.searchWindow.show()
        
        pass
        
    
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
        DBtoXML.MakeXML(db, "kat_raeume")
       
        os.startfile("Excel\kat_raeume.xlsx")
        pass
    
    def on_btReport_clicked(self):
        
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_raeume")
            print("dsadsa")
            input_file = 'Reports\kat_raeume.jasper'
    #        output = 'MyReports' # Ziel-/SUB-Ordner
           
            output = 'Reports\kat_raeume'
            print("asdasdasd")
            jasper = JasperPy()
           
            con={
            'driver':'generic',
            'jdbc_driver':'org.sqlite.JDBC',
            'jdbc_url':'jdbc:sqlite:kat.db'
            }
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])  
            print("dsa")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            #self.setCursor(Qt.WaitCursor)
           
            os.startfile("Reports\kat_raeume.pdf")
            print("asd")
            
            self.INFO("PDF-Datei wurde erstellt.",  "I")# info asugabe
        except Exception as e:
            print(e)
                
        except Exception:
            self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
        
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
