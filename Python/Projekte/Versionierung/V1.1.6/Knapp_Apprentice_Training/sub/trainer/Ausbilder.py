# -*- coding: utf-8 -*-

"""
Module implementing LAB_Ausbilder.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
import datetime,  time,  os,  subprocess
from other.database import Database
from sub.trainer.Ui_Ausbilder import Ui_Ausbilder
from sub.XML.XML_Class import DBtoXML
from sub.trainer.Ausbilder_suchen import Ausbilder_suchen
from pyreportjasper import JasperPy
from tkinter import messagebox
import tkinter as tk
 
class Ausbilder(QDialog, Ui_Ausbilder):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Ausbilder, self).__init__(parent)
        self.setupUi(self)
        self.cell_tw_anzeige()
        date = datetime.datetime.now()
        self.de_Eintritt.setDate(date)
    
    @pyqtSlot()
    def on_pb_Speichern_clicked(self):


        db = Database.get_instance(self)
        sql = "select * from kat_ausbilder WHERE Familienname = '" + self.le_Familienname.text() + "' AND Vorname = '" + self.le_Vorname.text() + "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)

        if satz_len == 0:
            sql = "INSERT INTO kat_ausbilder (Familienname, Vorname, Telefon, Wochenstunden, Eintrittsdatum, Austrittsdatum, wt_mo, wt_di, wt_mi, wt_do, wt_fr, Benutzer) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.le_Familienname.text(),  self.le_Vorname.text(),  self.le_Telefon.text(),  self.sb_Wochenstunden.value(), self.de_Eintritt.text(),  self.de_Austritt.text(),  self.cb_montag.isChecked(),\
            self.cb_Dienstag.isChecked(),  self.cb_Mittwoch.isChecked(),  self.cb_Donnerstag.isChecked(),  self.cb_Freitag.isChecked(),  self.parent().label_eingeloggt_als.text())
            self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugabe 
        else:
            sql = "UPDATE kat_ausbilder set Telefon=%s, Wochenstunden=%s, Eintrittsdatum=%s, Austrittsdatum=%s, wt_mo=%s, wt_di=%s, wt_mi=%s, wt_do=%s, wt_fr=%s, Benutzer=%s" + " where Familienname ='" + self.le_Familienname.text() + "' and Vorname ='" + self.le_Vorname.text() + "'"
            val = (self.le_Telefon.text(),  self.sb_Wochenstunden.value(), self.de_Eintritt.text(),  self.de_Austritt.text(),  self.cb_montag.isChecked(),  self.cb_Dienstag.isChecked(),  self.cb_Mittwoch.isChecked(),  self.cb_Donnerstag.isChecked(),  self.cb_Freitag.isChecked(),  self.parent().label_eingeloggt_als.text())
            self.INFO("Eintrag wurde in der Datenbank aktualisiert!",  "I")# info asugabe 
        db.insert(sql,  val)
        
        

        self.cell_tw_anzeige()

        
    
    @pyqtSlot()
    def on_pb_Loeschen_clicked(self):
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_ausbilder WHERE Familienname = '" + self.le_Familienname.text() + "' AND Vorname = '" + self.le_Vorname.text() + "'"
        db.delete(sql)
        self.cell_tw_anzeige()
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe 

    
    @pyqtSlot()
    def on_pb_Abbrechen_clicked(self):
        self.parent().show()
        self.close()
    
    @pyqtSlot(int, int)
    def on_tw_anzeige_cellClicked(self, row, column):
        AUSTRITTS_DATUM = datetime.datetime.strptime(self.tw_anzeige.item(row,  6).text(),  "%d.%m.%Y")
        EINTRITTS_DATUM = datetime.datetime.strptime(self.tw_anzeige.item(row,  5).text(),  "%d.%m.%Y")
        self.le_Familienname.setText(self.tw_anzeige.item(row, 1).text())
        self.le_Vorname.setText(self.tw_anzeige.item(row, 2).text())
        self.le_Telefon.setText(self.tw_anzeige.item(row, 3).text())
        self.sb_Wochenstunden.setValue(int(self.tw_anzeige.item(row, 4).text()))
        self.de_Eintritt.setDate(EINTRITTS_DATUM)
        self.de_Austritt.setDate(AUSTRITTS_DATUM)
        self.cb_montag.setChecked(self.tw_anzeige.item(row,  7).checkState())
        self.cb_Dienstag.setChecked(self.tw_anzeige.item(row,  8).checkState())
        self.cb_Mittwoch.setChecked(self.tw_anzeige.item(row,  9).checkState())
        self.cb_Donnerstag.setChecked(self.tw_anzeige.item(row,  10).checkState())
        self.cb_Freitag.setChecked(self.tw_anzeige.item(row,  11).checkState())
    def cell_tw_anzeige(self):
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tw_anzeige.setColumnCount(14)
        colname = QTableWidgetItem("id")
        self.tw_anzeige.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Familienname")
        self.tw_anzeige.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Vorname")
        self.tw_anzeige.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Telefon")
        self.tw_anzeige.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Wochenstunden")
        self.tw_anzeige.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Eintrittsdatum")
        self.tw_anzeige.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Austrittsdatum")
        self.tw_anzeige.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("mo")
        self.tw_anzeige.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("di")
        self.tw_anzeige.setHorizontalHeaderItem(8, colname)
        colname = QTableWidgetItem("mi")
        self.tw_anzeige.setHorizontalHeaderItem(9, colname)
        colname = QTableWidgetItem("do")
        self.tw_anzeige.setHorizontalHeaderItem(10, colname)
        colname = QTableWidgetItem("fr")
        self.tw_anzeige.setHorizontalHeaderItem(11, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tw_anzeige.setHorizontalHeaderItem(12, colname)
        colname = QTableWidgetItem("Änderung")
        self.tw_anzeige.setHorizontalHeaderItem(13, colname)
        
        self.tw_anzeige.setRowCount(1)
        sql = "SELECT * FROM kat_ausbilder"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  14):
                self.tw_anzeige.setRowCount(zeile + 1)
                if s == 7:
                    fielditem = QTableWidgetItem("")
                    self.tw_anzeige.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 8:
                    fielditem = QTableWidgetItem("")
                    self.tw_anzeige.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 9:
                    fielditem = QTableWidgetItem("")
                    self.tw_anzeige.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                        

                if s == 10:
                    fielditem = QTableWidgetItem("")
                    self.tw_anzeige.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                        
                    

                if s == 11:
                    fielditem = QTableWidgetItem("")
                    self.tw_anzeige.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                                                
                if s < 7 or s >11:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.tw_anzeige.setItem(zeile,  s,  fielditem)
                
            zeile += 1

        mycursor.close()
       
        self.tw_anzeige.resizeColumnsToContents()
        self.tw_anzeige.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
    
    @pyqtSlot()
    def on_pb_Hilfe_clicked(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Hilfe",  "Die hilfe Funktion wird in kürze hinzugefügt!")
    @pyqtSlot()
    def closeEvent(self, event):
        self.parent().show()
    @pyqtSlot()
    def on_pb_suchen_clicked(self):
        self.suchen  = Ausbilder_suchen(self)
        self.suchen.show()
        #root = tk.Tk()
        #root.withdraw()
        #messagebox.showinfo("Suchen",  "Die suchen Funktion wird in kürze hinzugefügt!")
    @pyqtSlot()
    def on_pb_excel_clicked(self):
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "kat_ausbilder")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            os.startfile("Excel\kat_ausbilder.xlsx")
            self.INFO("Excel-Datei wurde erstellt.",  "I")
            
        except Exception as e:
            print(e)
            self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")


    @pyqtSlot()
    def on_pb_report_clicked(self):
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_ausbilder")
        
            input_file = 'Reports/kat_ausbilder.jasper'
            output = 'Reports/kat_ausbilder'
            jasper = JasperPy()
            con={
            'driver':'generic',
            'jdbc_driver':'org.sqlite.JDBC',
            'jdbc_url':'jdbc:sqlite:kat.db'
            }
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])

            self.INFO("PDF-Datei wurde erstellt!",  "I")# info asugabe 
            os.startfile("Reports\kat_ausbilder.pdf")
            
        except Exception:
            self.INFO("PDF-Datei wurde erstellt!",  "I")# info asugabe 
    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
    @pyqtSlot()
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
    
    @pyqtSlot()
    def on_pb_leeren_clicked(self):
#        AUSTRITTS_DATUM = datetime.datetime.strptime(self.tw_anzeige.item(row,  6).text(),  "%d.%m.%Y")
#        EINTRITTS_DATUM = datetime.datetime.strptime(self.tw_anzeige.item(row,  5).text(),  "%d.%m.%Y")
        date = datetime.datetime.now()
        self.le_Familienname.setText("")
        self.le_Vorname.setText("")
        self.le_Telefon.setText("")
        self.sb_Wochenstunden.setValue(int("0"))
        self.de_Eintritt.setDate(date)
        self.de_Austritt.setDate(date)
        self.cb_montag.setChecked(Qt.Unchecked)
        self.cb_Dienstag.setChecked(Qt.Unchecked)
        self.cb_Mittwoch.setChecked(Qt.Unchecked)
        self.cb_Donnerstag.setChecked(Qt.Unchecked)
        self.cb_Freitag.setChecked(Qt.Unchecked)

