# -*- coding: utf-8 -*-

"""
Module implementing Ausbilder_suchen.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem
from other.database import Database


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
        self.tw_suchen.setColumnCount(14)
        colname = QTableWidgetItem("id")
        self.tw_suchen.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Familienname")
        self.tw_suchen.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Vorname")
        self.tw_suchen.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Telefon")
        self.tw_suchen.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Wochenstunden")
        self.tw_suchen.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Eintrittsdatum")
        self.tw_suchen.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Austrittsdatum")
        self.tw_suchen.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("mo")
        self.tw_suchen.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("di")
        self.tw_suchen.setHorizontalHeaderItem(8, colname)
        colname = QTableWidgetItem("mi")
        self.tw_suchen.setHorizontalHeaderItem(9, colname)
        colname = QTableWidgetItem("do")
        self.tw_suchen.setHorizontalHeaderItem(10, colname)
        colname = QTableWidgetItem("fr")
        self.tw_suchen.setHorizontalHeaderItem(11, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tw_suchen.setHorizontalHeaderItem(12, colname)
        colname = QTableWidgetItem("Änderung")
        self.tw_suchen.setHorizontalHeaderItem(13, colname)
        
        self.tw_suchen.setRowCount(1)
        sql = "SELECT * from kat_ausbilder WHERE concat(Familienname, Vorname, Telefon, Wochenstunden, Eintrittsdatum, Austrittsdatum, wt_mo, wt_di, wt_mi, wt_do, wt_fr) like'" + '%' + self.le_suche.text() + '%' "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  14):
                self.tw_suchen.setRowCount(zeile + 1)
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
                        
                    

                if s == 11:
                    fielditem = QTableWidgetItem("")
                    self.tw_suchen.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                                                
                if s < 7 or s >11:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.tw_suchen.setItem(zeile,  s,  fielditem)
                
            zeile += 1

        mycursor.close()
       
        self.tw_suchen.resizeColumnsToContents()
        self.tw_suchen.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
    
    @pyqtSlot()
    def on_pb_abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(int, int)
    def on_tw_suchen_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Achtung",  "Diese Funktion wird in kürze hinzugefügt!")
    
    @pyqtSlot(int, int)
    def on_tw_suchen_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Achtung",  "Diese Funktion wird in kürze hinzugefügt!")
        
#app = QApplication(sys.argv)
#ui = Ausbilder_suchen() #Name der bei der Anlage der Dialog-Klasse verwendet wurde
#ui.show()
#sys.exit(app.exec_())
