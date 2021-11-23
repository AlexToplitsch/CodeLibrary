# -*- coding: utf-8 -*-

"""
Module implementing Unterrichtsthemen.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem
from sub.ausbildungsthemen.Ui_Unterrichtsthemen import Ui_Unterrichtsthemen
from other.database import Database
from sub.XML.XML_Class import DBtoXML
import time,  os
from tkinter import messagebox
import tkinter as tk

class Unterrichtsthemen(QDialog, Ui_Unterrichtsthemen):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Unterrichtsthemen, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(int, int)
    def on_tw_anzeige_cellClicked(self, row, column):
        self.le_name.setText(self.tw_anzeige.item(row, 1).text())
    
    @pyqtSlot()
    def on_pb_excel_clicked(self):
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "kat_unterrichtsthemen")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            os.startfile("Excel\kat_unterrichtsthemen.xlsx")
            self.INFO("Excel-Datei wurde erstellt.",  "I")
            
        except Exception as e:
            print(e)
            self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")
    
    @pyqtSlot()
    def on_pb_back_clicked(self):
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pb_delete_clicked(self):
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_ausbildungsthemen WHERE Ausbildungsthema = '" + self.le_name.text() + "'"
        db.delete(sql)
        self.cell_tw_anzeige()
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe 
    
    @pyqtSlot()
    def on_pb_report_clicked(self):
        db = Database.get_instance(self)
        db.writeSQLite("kat_ausbildungsthemen")
        self.INFO("PDF-Datei wurde erstellt!",  "I")# info asugabe 
    def cell_tw_anzeige(self):
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tw_anzeige.setColumnCount(2)
        colname = QTableWidgetItem("ID")
        self.tw_anzeige.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Ausbildungsthema")
        self.tw_anzeige.setHorizontalHeaderItem(1, colname)

        
        self.tw_anzeige.setRowCount(1)
        sql = "SELECT * FROM kat_ausbildungsthemen"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  2):
                self.tw_anzeige.setRowCount(zeile + 1)

        mycursor.close()
       
        self.tw_anzeige.resizeColumnsToContents()
        self.tw_anzeige.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
    
    @pyqtSlot()
    def on_pb_hilfe_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pb_suchen_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pb_speichern_clicked(self):


        db = Database.get_instance(self)
        sql = "select * from kat_ausbildungsthemen WHERE Ausbildungsthema = '" + self.le_name.text() + "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)

        if satz_len == 0:
            sql = "INSERT INTO kat_ausbildungsthemen (Ausbildungsthema) \
            VALUES (%s)"
            val = (self.le_name.text())
            self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugabe 
        else:
            sql = "UPDATE kat_ausbildungsthemen set Ausbildungsthema=%s" + " where Ausbildungsthema ='" + self.le_name.text() + "'"
            val = (self.le_name.text())
            self.INFO("Eintrag wurde in der Datenbank aktualisiert!",  "I")# info asugabe 
        db.insert(sql,  val)
        
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
            messagebox.showerror("Fehler", MELDUNG)
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
                messagebox.showwarning("Hinweis/Warnung", MELDUNG)

            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")

        
#app = QApplication(sys.argv)
#ui = Unterrichtsthemen() #Name der bei der Anlage der Dialog-Klasse verwendet wurde
#ui.show()
#sys.exit(app.exec_())
