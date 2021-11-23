# -*- coding: utf-8 -*-

"""
Module implementing Ausbilder_suchen.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem
from other.database import Database
import datetime

from sub.trainer.Ui_Ausbilder_suchen import Ui_Ausbilder_suchen
from tkinter import messagebox
import tkinter as tk

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
    
    @pyqtSlot()
    def on_pb_suchen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.cell_tw_suchen()
        
    def cell_tw_suchen(self):
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tw_suchen.setColumnCount(13)
        colname = QTableWidgetItem("Familienname")
        self.tw_suchen.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Vorname")
        self.tw_suchen.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Telefon")
        self.tw_suchen.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Wochenstunden")
        self.tw_suchen.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Eintrittsdatum")
        self.tw_suchen.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Austrittsdatum")
        self.tw_suchen.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("mo")
        self.tw_suchen.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("di")
        self.tw_suchen.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("mi")
        self.tw_suchen.setHorizontalHeaderItem(8, colname)
        colname = QTableWidgetItem("do")
        self.tw_suchen.setHorizontalHeaderItem(9, colname)
        colname = QTableWidgetItem("fr")
        self.tw_suchen.setHorizontalHeaderItem(10, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tw_suchen.setHorizontalHeaderItem(11, colname)
        colname = QTableWidgetItem("Änderung")
        self.tw_suchen.setHorizontalHeaderItem(12, colname)
        
        self.tw_suchen.setRowCount(1)
        sql = "SELECT Familienname, Vorname, Telefon, Wochenstunden, Eintrittsdatum, Austrittsdatum, wt_mo, wt_di, wt_mi, wt_do, wt_fr, Benutzer, Änderung from kat_ausbilder WHERE concat(Familienname, Vorname, Telefon, Wochenstunden, Eintrittsdatum, Austrittsdatum, wt_mo, wt_di, wt_mi, wt_do, wt_fr) like'" + '%' + self.le_suche.text() + '%' "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  13):
                self.tw_suchen.setRowCount(zeile + 1)
                if s == 6:
                    fielditem = QTableWidgetItem("")
                    self.tw_suchen.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 7:
                    fielditem = QTableWidgetItem("")
                    self.tw_suchen.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 8:
                    fielditem = QTableWidgetItem("")
                    self.tw_suchen.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                        

                if s == 9:
                    fielditem = QTableWidgetItem("")
                    self.tw_suchen.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                        
                    

                if s == 10:
                    fielditem = QTableWidgetItem("")
                    self.tw_suchen.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                                                
                if s < 6 or s >10:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.tw_suchen.setItem(zeile,  s,  fielditem)
                
            zeile += 1

        mycursor.close()
       
        self.tw_suchen.resizeColumnsToContents()
        self.tw_suchen.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
    
    @pyqtSlot()
    def on_pb_abbrechen_clicked(self):
        self.parent().show()
        self.close()
    
    @pyqtSlot(int, int)
    def on_tw_suchen_cellClicked(self, row, column):
        AUSTRITTS_DATUM = datetime.datetime.strptime(self.tw_suchen.item(row,  5).text(),  "%d.%m.%Y")
        EINTRITTS_DATUM = datetime.datetime.strptime(self.tw_suchen.item(row,  4).text(),  "%d.%m.%Y")
        self.parent().le_Familienname.setText(self.tw_suchen.item(row, 0).text())
        self.parent().le_Vorname.setText(self.tw_suchen.item(row, 1).text())
        self.parent().le_Telefon.setText(self.tw_suchen.item(row, 2).text())
        self.parent().sb_Wochenstunden.setValue(int(self.tw_suchen.item(row, 3).text()))
        self.parent().de_Eintritt.setDate(EINTRITTS_DATUM)
        self.parent().de_Austritt.setDate(AUSTRITTS_DATUM)
        self.parent().cb_montag.setChecked(self.tw_suchen.item(row,  6).checkState())
        self.parent().cb_Dienstag.setChecked(self.tw_suchen.item(row,  7).checkState())
        self.parent().cb_Mittwoch.setChecked(self.tw_suchen.item(row,  8).checkState())
        self.parent().cb_Donnerstag.setChecked(self.tw_suchen.item(row,  9).checkState())
        self.parent().cb_Freitag.setChecked(self.tw_suchen.item(row,  10).checkState())
    @pyqtSlot(int, int)
    def on_tw_suchen_cellDoubleClicked(self, row, column):
        self.hide()
        
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
    
        
#app = QApplication(sys.argv)
#ui = Ausbilder_suchen() #Name der bei der Anlage der Dialog-Klasse verwendet wurde
#ui.show()
#sys.exit(app.exec_())
