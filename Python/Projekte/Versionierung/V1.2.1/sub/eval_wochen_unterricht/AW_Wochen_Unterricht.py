
# -*- coding: utf-8 -*-

"""
Module implementing Auswertung.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from other.database import Database
import datetime
from sub.XML.XML_Class import DBtoXML
import time
import os
from sub.eval_wochen_unterricht.Ui_AW_Wochen_Unterricht import Ui_Auswertung
from pyreportjasper import JasperPy
import tkinter as tk

class Auswertung(QDialog, Ui_Auswertung):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """

        super(Auswertung, self).__init__(parent)
        self.setupUi(self)
        self.ch_bewertung.setEnabled(False)
        date = datetime.datetime.now()
        self.de_von.setDate(date)
        self.de_bis.setDate(date)
        self.cb_ausb_befuellen()
        self.cb_unter_befuellen()
        self.cb_ausbilder.setCurrentText("")
        self.cb_unterrichtsthema.setCurrentText("")
    @pyqtSlot()
    def cb_ausb_befuellen(self):
        db = Database.get_instance(self)
        sql = "SELECT Familienname FROM kat_ausbilder"
        mycursor = db.select(sql)
        ausbilder=[]
        for i in mycursor:
            ausbilder.append(i[0])
        self.cb_ausbilder.addItems(ausbilder)
        self.cb_ausbilder.addItem("")
        
    @pyqtSlot()
    def tw_anzeigen(self):
        db = Database.get_instance(self)
        
        self.setCursor(Qt.WaitCursor)
        self.tw_Table.setColumnCount(8)
        
        colname = QTableWidgetItem("Ausbilder")
        self.tw_Table.setHorizontalHeaderItem(0,  colname)
        colname = QTableWidgetItem("Unterrichtsthema")
        self.tw_Table.setHorizontalHeaderItem(1,  colname)
        colname = QTableWidgetItem("Datum")
        self.tw_Table.setHorizontalHeaderItem(2,  colname)
        colname = QTableWidgetItem("Zeit")
        self.tw_Table.setHorizontalHeaderItem(3,  colname)
        
        colname = QTableWidgetItem("Ausbildungsthema1")
        self.tw_Table.setHorizontalHeaderItem(4,  colname)
        colname = QTableWidgetItem("Ausbildungsthema2")
        self.tw_Table.setHorizontalHeaderItem(5,  colname)
        colname = QTableWidgetItem("Ausbildungsthema3")
        self.tw_Table.setHorizontalHeaderItem(6,  colname)
        colname = QTableWidgetItem("Teilnehmer")
        self.tw_Table.setHorizontalHeaderItem(7,  colname)
        
        sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3, lehrlinge FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND ausbilder = '" + self.cb_ausbilder.currentText() + "' AND unterrichtsthema = '"+ self.cb_unterrichtsthema.currentText() +"'"
           
        if self.cb_ausbilder.currentText() == "" and self.cb_unterrichtsthema.currentText() == "":
            sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3, lehrlinge FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "'"
        elif self.cb_ausbilder.currentText() == "":
            sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3, lehrlinge FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND unterrichtsthema = '"+ self.cb_unterrichtsthema.currentText() +"'"
        elif self.cb_unterrichtsthema.currentText() == "":
            sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3, lehrlinge FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND ausbilder = '" + self.cb_ausbilder.currentText() + "'"
        
        mycursor=db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  8):
                self.tw_Table.setRowCount(zeile +1)
                fielditem=QTableWidgetItem(str(z[s]))
                self.tw_Table.setItem(zeile, s, fielditem)
            zeile+=1
        self.tw_Table.resizeColumnsToContents()
        self.tw_Table.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
        
        
    @pyqtSlot()
    def tw_anzeigen2(self):
        db = Database.get_instance(self)
        
        self.setCursor(Qt.WaitCursor)
        self.tw_Table.setColumnCount(7)
        
        colname = QTableWidgetItem("Ausbilder")
        self.tw_Table.setHorizontalHeaderItem(0,  colname)
        colname = QTableWidgetItem("Unterrichtsthema")
        self.tw_Table.setHorizontalHeaderItem(1,  colname)
    
    
#        colname = QTableWidgetItem("Ausbildungsthema")
#        self.tw_Table.setHorizontalHeaderItem(2,  colname)
        colname = QTableWidgetItem("Datum")
        self.tw_Table.setHorizontalHeaderItem(2,  colname)
        colname = QTableWidgetItem("Zeit")
        self.tw_Table.setHorizontalHeaderItem(3,  colname)
        colname = QTableWidgetItem("Ausbildungsthema1")
        self.tw_Table.setHorizontalHeaderItem(4,  colname)
        colname = QTableWidgetItem("Ausbildungsthema2")
        self.tw_Table.setHorizontalHeaderItem(5,  colname)
        colname = QTableWidgetItem("Ausbildungsthema3")
        self.tw_Table.setHorizontalHeaderItem(6,  colname)
        
        
        
        sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3 FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND ausbilder = '" + self.cb_ausbilder.currentText() + "' AND unterrichtsthema = '"+ self.cb_unterrichtsthema.currentText() +"'"
        
        if self.cb_ausbilder.currentText() == "" and self.cb_unterrichtsthema.currentText() == "":
            
            sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3 FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "'"
        elif self.cb_ausbilder.currentText() == "":
            sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3 FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND unterrichtsthema = '"+ self.cb_unterrichtsthema.currentText() +"'"
        elif self.cb_unterrichtsthema.currentText() == "":
            sql = "SELECT ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3 FROM kat_wochen_unterricht WHERE DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND ausbilder = '" + self.cb_ausbilder.currentText() + "'"
        
        mycursor=db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  7):
                self.tw_Table.setRowCount(zeile +1)
                fielditem=QTableWidgetItem(str(z[s]))
                self.tw_Table.setItem(zeile, s, fielditem)
            zeile+=1
        self.tw_Table.resizeColumnsToContents()
        self.tw_Table.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
        
    @pyqtSlot()
    def cb_unter_befuellen(self):
        db = Database.get_instance(self)
        sql = "SELECT ausbildungsthema FROM kat_ausbildungsthemen"
        mycursor = db.select(sql)
        thema = []
        
        for i in mycursor:
            thema.append(i[0])
        
        self.cb_unterrichtsthema.addItems(thema)
        self.cb_unterrichtsthema.addItem("")
    
    @pyqtSlot()
    def closeEvent(self, event):
        """
        Schließt das im Moment geöffnete Fenster(Fachrichtungen)
        """
        
        #self.parent().show()
        self.parent().setWindowOpacity(1.0)
        self.close()
        
    @pyqtSlot(int,  int)
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
    
    @pyqtSlot(bool)
    def on_btn_suchen_clicked(self):
        if self.ch_teilnehmer.isChecked() == True:
            self.tw_anzeigen()
        else:
            self.tw_anzeigen2()
        
        self.INFO("Suche erfolgreich.",  "I")
    
    @pyqtSlot()
    def on_ch_teilnehmer_stateChanged(self, p0):
        if self.ch_teilnehmer.isChecked() == True:
                self.ch_bewertung.setEnabled(True)
        else:
            self.ch_bewertung.setEnabled(False)
    
    @pyqtSlot()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
    
    
    def on_btn_excel_clicked(self):
        x = self.cb_ausbilder.currentText() 
        y= self.cb_unterrichtsthema.currentText()
        if x == "" and y =="":
            self.INFO("Wählen Sie einen Ausbilder oder ein Unterrichtsthema aus",  "F")
        else:
            try:
                db = Database.get_instance(self)
                if x == "":
                    DBtoXML.MakeXML(db, "kat_wochen_unterricht", "DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND unterrichtsthema = '"+ self.cb_unterrichtsthema.currentText() +"'", 
                "ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3, lehrlinge", "kat_auswertung_wochen_unterricht")
                elif y == "":
                    DBtoXML.MakeXML(db, "kat_wochen_unterricht", "DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND ausbilder = '" + self.cb_ausbilder.currentText() + "'", 
                "ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3, lehrlinge", "kat_auswertung_wochen_unterricht")
                 
                else:DBtoXML.MakeXML(db, "kat_wochen_unterricht", "DATUM >= '" + self.de_von.text() + "' AND DATUM <= '" + self.de_bis.text() + "' AND ausbilder = '" + self.cb_ausbilder.currentText() + "' AND unterrichtsthema = '"+ self.cb_unterrichtsthema.currentText() +"'", 
                "ausbilder, unterrichtsthema, datum, von_bis, ausbildungsthema_1, ausbildungsthema_2, ausbildungsthema_3, lehrlinge", "kat_auswertung_wochen_unterricht")
                    
                self.setCursor(Qt.WaitCursor)
                time.sleep(2)
                self.setCursor(Qt.ArrowCursor)
                os.startfile("Excel\kat_auswertung_wochen_unterricht.xlsx");
                self.INFO("Excel-Datei wurde erstellt.",  "I")
                    
            except Exception as e:
                self.setCursor(Qt.ArrowCursor)
                print(e)
                self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")
        
    def on_btn_hilfe_clicked(self):
        res = QMessageBox.information(
            self,
            self.tr("Hilfe"),
            self.tr("""Ist in Arbeit..."""))
    def on_btn_report_clicked(self):
        x = self.cb_ausbilder.currentText() 
        y= self.cb_unterrichtsthema.currentText()
        if x == "" and y =="":
            self.INFO("Wählen Sie einen Ausbilder oder ein Unterrichtsthema aus",  "F")
        else:
            try:
                db = Database.get_instance(self)
                if x == "":
                    db.writeSQLite("kat_wochen_unterricht",  "DATUM>='" + self.de_von.text() + "'AND DATUM<='" + self.de_bis.text() + "' AND unterrichtsthema='"+ self.cb_unterrichtsthema.currentText() +"'")
                elif y == "":
                    db.writeSQLite("kat_wochen_unterricht",  "DATUM>='" + self.de_von.text() + "'AND DATUM<='" + self.de_bis.text() + "' AND ausbilder='" + self.cb_ausbilder.currentText() + "'")
         
                else:
                    db.writeSQLite("kat_wochen_unterricht",  "DATUM>='" + self.de_von.text() + "'AND DATUM<='" + self.de_bis.text() + "' AND ausbilder='" + self.cb_ausbilder.currentText() + "' AND unterrichtsthema='"+ self.cb_unterrichtsthema.currentText() +"'")
                    
                input_file = 'Reports\kat_auswertung_wochen_unterricht.jasper'
            #       output = 'MyReports' # Ziel-/SUB-Ordner
                
                output = 'Reports\kat_auswertung_wochen_unterricht'
                
                jasper = JasperPy()
                
                con={
                'driver':'generic', 
                'jdbc_driver':'org.sqlite.JDBC', 
                'jdbc_url':'jdbc:sqlite:kat.db'
                }
                jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])   
                
                self.setCursor(Qt.WaitCursor)
                time.sleep(2)
                self.setCursor(Qt.ArrowCursor)
                
                self.INFO("PDF-Datei wurde erstellt.",  "I")
                os.startfile("Reports\kat_auswertung_wochen_unterricht.pdf")
            
            except Exception:
                    
                self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
    @pyqtSlot()
    def on_btn_abbrechen_clicked(self):
        self.parent().show()
        self.close()
