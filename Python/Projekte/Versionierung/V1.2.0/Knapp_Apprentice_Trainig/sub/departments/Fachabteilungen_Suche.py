# -*- coding: utf-8 -*-

"""
Module implementing Fachabteilungen_Suche.
"""
from other.database import Database
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *

from .Ui_Fachabteilungen_Suche import Ui_Dialog

class Fachabteilungen_Suche(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fachabteilungen_Suche, self).__init__(parent)
        self.setupUi(self)
        
    @pyqtSlot()
    def on_btSuchen_clicked(self):
        """
        Slot documentation goes here.
        """
        f = self.leSuche.text()
        print(f)
        if f != "":
            self.twAnzeige(f)
        else:
            self.twAnzeige()
            
    def closeEvent(self, event):
        self.parent().show()
        
    def twAnzeige(self,  f=""):
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        self.twAnzeige_suche.setColumnCount(17)
        colname=QTableWidgetItem("Fachabteilung")
        self.twAnzeige_suche.setHorizontalHeaderItem(0,  colname)
        colname=QTableWidgetItem("Bezeichnung")
        self.twAnzeige_suche.setHorizontalHeaderItem(1,  colname)
        colname=QTableWidgetItem("Gebäude")
        self.twAnzeige_suche.setHorizontalHeaderItem(2,  colname)
        colname=QTableWidgetItem("Stock")
        self.twAnzeige_suche.setHorizontalHeaderItem(3,  colname)
        colname=QTableWidgetItem("Abteilungsleiter")
        self.twAnzeige_suche.setHorizontalHeaderItem(4,  colname)
        colname=QTableWidgetItem("AL-Tel-Nr.")
        self.twAnzeige_suche.setHorizontalHeaderItem(5,  colname)
        colname=QTableWidgetItem("AL-E-Mail")
        self.twAnzeige_suche.setHorizontalHeaderItem(6,  colname)
        colname=QTableWidgetItem("Ansprechperson")
        self.twAnzeige_suche.setHorizontalHeaderItem(7,  colname)
        colname=QTableWidgetItem("AP-Tel-Nr.")
        self.twAnzeige_suche.setHorizontalHeaderItem(8,  colname)
        colname=QTableWidgetItem("AP-E-Mail")
        self.twAnzeige_suche.setHorizontalHeaderItem(9,  colname)
        colname=QTableWidgetItem("Mo")
        self.twAnzeige_suche.setHorizontalHeaderItem(10,  colname)
        colname=QTableWidgetItem("Di")
        self.twAnzeige_suche.setHorizontalHeaderItem(11,  colname)
        colname=QTableWidgetItem("Mi")
        self.twAnzeige_suche.setHorizontalHeaderItem(12,  colname)
        colname=QTableWidgetItem("Do")
        self.twAnzeige_suche.setHorizontalHeaderItem(13,  colname)
        colname=QTableWidgetItem("Fr")
        self.twAnzeige_suche.setHorizontalHeaderItem(14,  colname)
        colname=QTableWidgetItem("Benutzername")
        self.twAnzeige_suche.setHorizontalHeaderItem(15,   colname)
        colname=QTableWidgetItem("Änderungsdatum")
        self.twAnzeige_suche.setHorizontalHeaderItem(16,  colname)
        self.twAnzeige_suche.setRowCount(1)
        
        if f != "":
            sql= "SELECT FachabteilungAbk, FachabteilungBez, Gebäude, Stock, Abteilungsleiter, AL_Tel_Nr, AL_E_Mail, Ansprechsperson, AP_Tel_Nr, AP_E_Mail, wo_mo, wo_di, wo_mi, wo_do, wo_fr, Benutzer, Aenderung FROM kat_fachabteilungen WHERE FachabteilungAbk LIKE '%"+f+"%' OR FachabteilungBez LIKE '%"+f+"%' OR Abteilungsleiter LIKE '%"+f+"%'"
        else :
            sql = "SELECT FachabteilungAbk, FachabteilungBez, Gebäude, Stock, Abteilungsleiter, AL_Tel_Nr, AL_E_Mail, Ansprechsperson, AP_Tel_Nr, AP_E_Mail, wo_mo, wo_di, wo_mi, wo_do, wo_fr, Benutzer, Aenderung FROM kat_fachabteilungen"
        mycursor = db.select(sql)
        print(sql)
        
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile=0
        for z in mycursor:
            for s in range(0, 17):
                self.twAnzeige_suche.setRowCount(zeile+1)
                if s == 11:
                    fielditem = QTableWidgetItem("")
                    self.twAnzeige_suche.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 12:
                    fielditem = QTableWidgetItem("")
                    self.twAnzeige_suche.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 13:
                    fielditem = QTableWidgetItem("")
                    self.twAnzeige_suche.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 14:
                    fielditem = QTableWidgetItem("")
                    self.twAnzeige_suche.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 15:
                    fielditem = QTableWidgetItem("")
                    self.twAnzeige_suche.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s < 11 or s > 15:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.twAnzeige_suche.setItem(zeile, s, fielditem)
            zeile += 1  
        
        self.twAnzeige_suche.resizeColumnsToContents()
        self.twAnzeige_suche.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
        
    @pyqtSlot()
    def on_pB_BEENDEN_clicked(self):
        """
        Slot documentation goes here.
        """
        self.hide()
    
    @pyqtSlot(int, int)
    def on_twAnzeige_suche_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        self.parent().leFachabteilungabk.setText(self.twAnzeige_suche.item(row, 0).text())
        self.parent().leFachabteilungbez.setText(self.twAnzeige_suche.item(row, 1).text())
        self.parent().leGebaeude.setText(self.twAnzeige_suche.item(row, 2).text())
        self.parent().leStock.setText(self.twAnzeige_suche.item(row, 3).text())
        self.parent().leAbteilungsleitername.setText(self.twAnzeige_suche.item(row, 4).text())
        self.parent().leAbteilungsleitermail.setText(self.twAnzeige_suche.item(row, 6).text())
        self.parent().leAbteilungsleitertel.setText(self.twAnzeige_suche.item(row, 5).text())
        self.parent().leAnsprechspersonname.setText(self.twAnzeige_suche.item(row, 7).text())
        self.parent().leAnsprechspersonmail.setText(self.twAnzeige_suche.item(row, 9).text())
        self.parent().leAnsprechspersontel.setText(self.twAnzeige_suche.item(row, 8).text())
    
    @pyqtSlot(int, int)
    def on_twAnzeige_suche_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        self.hide()
