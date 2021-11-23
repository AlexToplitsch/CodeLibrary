# -*- coding: utf-8 -*-

"""
Module implementing LAP_Themenkatalog_Suche.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem
from other.database import Database
from sub.lapcontent.Ui_LAP_Suche import Ui_LAP_Themenkatalog_Suche

class LAP_Themenkatalog_Suche(QDialog, Ui_LAP_Themenkatalog_Suche):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LAP_Themenkatalog_Suche, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(int, int)
    def on_tW_LAP_Themenkatalog_DB_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        try:
            self.parent().cB_Fachrichtung.setCurrentText(self.tW_LAP_Themenkatalog_DB.item(row, 1).text())
            self.parent().le_Themen_ID.setText(self.tW_LAP_Themenkatalog_DB.item(row, 2).text())
            self.parent().le_Hauptthema.setText(self.tW_LAP_Themenkatalog_DB.item(row, 3).text())
            self.parent().le_Thema.setText(self.tW_LAP_Themenkatalog_DB.item(row, 4).text())
            self.parent().cB_Ausbilder.setCurrentText(self.tW_LAP_Themenkatalog_DB.item(row, 5).text())
            self.parent().sB_Lehrjahr.setValue(int(self.tW_LAP_Themenkatalog_DB.item(row, 6).text()))
            self.parent().sB_BS_Jahr.setValue(int(self.tW_LAP_Themenkatalog_DB.item(row, 7).text()))
        except Exception:
            self. tW_LAP_Themenkatalog_DB_Anzeigen()
    @pyqtSlot(int, int)
    def on_tW_LAP_Themenkatalog_DB_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        try:
            self.parent().cB_Fachrichtung.setCurrentText(self.tW_LAP_Themenkatalog_DB.item(row, 1).text())
            self.parent().le_Themen_ID.setText(self.tW_LAP_Themenkatalog_DB.item(row, 2).text())
            self.parent().le_Hauptthema.setText(self.tW_LAP_Themenkatalog_DB.item(row, 3).text())
            self.parent().le_Thema.setText(self.tW_LAP_Themenkatalog_DB.item(row, 4).text())
            self.parent().cB_Ausbilder.setCurrentText(self.tW_LAP_Themenkatalog_DB.item(row, 5).text())
            self.parent().sB_Lehrjahr.setValue(int(self.tW_LAP_Themenkatalog_DB.item(row, 6).text()))
            self.parent().sB_BS_Jahr.setValue(int(self.tW_LAP_Themenkatalog_DB.item(row, 7).text()))
            self.close()
        except Exception:
            self.tW_LAP_Themenkatalog_DB_Anzeigen()
        
    @pyqtSlot()
    def on_pB_Suchen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tW_LAP_Themenkatalog_DB_Anzeigen(self.le_Suchbegriff.text())
        self.le_Suchbegriff.setText("")
    
    @pyqtSlot()
    def on_pB_Beenden_clicked(self):
       self.hide()
       
    def tW_LAP_Themenkatalog_DB_Anzeigen(self, f1 = ""):
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tW_LAP_Themenkatalog_DB.setColumnCount(9)
        #colname = QTableWidgetItem("ID")
        #self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Fachrichtung")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Themen_ID")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Hauptthema")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Thema")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Ausbilder")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Lehrjahr")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("BS_Lehrjahr")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("Änderung")
        self.tW_LAP_Themenkatalog_DB.setHorizontalHeaderItem(8, colname)
        
        self.tW_LAP_Themenkatalog_DB.setRowCount(1)
        
        db = Database.get_instance(self)

        if f1 != "":
           sql = "select Fachrichtung,Themen_ID,Hauptthema,Thema,Ausbilder,Lehrjahr,BS_Lehrjahr,Benutzer,`Änderung` from kat_lap_themenkatalog where concat(Fachrichtung, Themen_ID, Hauptthema, Thema, Ausbilder) like '"+ '%' + f1 + '%' "'"
        else:
            sql = "select Fachrichtung,Themen_ID,Hauptthema,Thema,Ausbilder,Lehrjahr,BS_Lehrjahr,Benutzer,`Änderung`from KAT_lap_themenkatalog"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        
        zeile = 0 
        for z in mycursor:
            for s in range(0,  9):
                self.tW_LAP_Themenkatalog_DB.setRowCount(zeile + 1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tW_LAP_Themenkatalog_DB.setItem(zeile,  s,  fielditem)
            zeile+=1
                
        mycursor.close()
        
        self.tW_LAP_Themenkatalog_DB.resizeColumnsToContents()
        self.tW_LAP_Themenkatalog_DB.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
        
    def keyPressEvent(self,  event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
