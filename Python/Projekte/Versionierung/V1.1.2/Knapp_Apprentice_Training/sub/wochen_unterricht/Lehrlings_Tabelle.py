# -*- coding: utf-8 -*-

"""
Module implementing Lehrlings_Tabelle.
"""

from PyQt5.QtCore import*
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from other.database import Database
from sub.wochen_unterricht.Ui_Lehrlings_Tabelle import Ui_Dialog


class Lehrlings_Tabelle(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrlings_Tabelle, self).__init__(parent)
        self.setupUi(self)
        self.cell_tw_anzeige()
        global row
        row = 1
    
    @pyqtSlot()
    def on_pushButton_hinzufuegen_clicked(self):
        """
        Slot documentation goes here.
        """
        checked_list = [] 
        for i in range(self.tableWidget_lehrlinge_liste.rowCount()):
            #print(self.tableWidget.rowCount())
            if self.tableWidget_lehrlinge_liste.item(i, 3).checkState() == Qt.Checked:
                checked_list.append([i,3])
                print(self.tableWidget_lehrlinge_liste.item(i,3-1).text())
                fielditem= QTableWidgetItem(self.parent().te_vorschau.item(4,  0).text()+"- "+self.tableWidget_lehrlinge_liste.item(i,3-1).text())
                self.parent().te_vorschau.setItem(4, 0, fielditem)
            else:
                pass
        print(checked_list)
        self.parent().show()
        self.close()
 
#       
#        self.cb_montag.setChecked(self.tw_anzeige.item(row,  7).checkState())
#        self.cb_Dienstag.setChecked(self.tw_anzeige.item(row,  8).checkState())
#        self.cb_Mittwoch.setChecked(self.tw_anzeige.item(row,  9).checkState())
#        self.cb_Donnerstag.setChecked(self.tw_anzeige.item(row,  10).checkState())
#        self.cb_Freitag.setChecked(self.tw_anzeige.item(row,  11).checkState())
#       
#        if self.tableWidget_lehrlinge_liste.item(row,  3).checkState()==Qt.Checked:
#            print("______________________________________________")
#        
#        if self.tableWidget_lehrlinge_liste.item(row,3).checkState() == Qt.Checked:
#       # fielditem=QTableWidgetItem(self.parent().te_vorschau.item(3,  0).text()+" "+self.tableWidget_lehrlinge_liste.item(row, 1).text()+" "+self.tableWidget_lehrlinge_liste.item(row,  2).text())
#        fielditem=QTableWidgetItem(self.tableWidget_lehrlinge_liste.item(1, 3).checkState())
#        self.parent().te_vorschau.setItem(2, 0, fielditem)
#        
#            
        # TODO: not implemented yet
       #raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().show()
        self.close()
 

    def cell_tw_anzeige(self):
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tableWidget_lehrlinge_liste.setColumnCount(4)
        colname = QTableWidgetItem("Personalnummer")
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Vorname")
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Nachname")
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Hinzufügen")        
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(3, colname)
        
        self.tableWidget_lehrlinge_liste.setRowCount(1)
        sql = "SELECT * FROM kat_list"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0
        for z in mycursor:
            for s in range(0,  4):
                self.tableWidget_lehrlinge_liste.setRowCount(zeile + 1)
                if s == 3:
                    fielditem = QTableWidgetItem("")
                    self.tableWidget_lehrlinge_liste.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Checked)
                                                
                if s < 3 or s >3:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.tableWidget_lehrlinge_liste.setItem(zeile,  s,  fielditem)
                
            zeile += 1

        mycursor.close()
       
        self.tableWidget_lehrlinge_liste.resizeColumnsToContents()
        self.tableWidget_lehrlinge_liste.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        
    def closeEvent(self, event):
        self.parent().show()
        
