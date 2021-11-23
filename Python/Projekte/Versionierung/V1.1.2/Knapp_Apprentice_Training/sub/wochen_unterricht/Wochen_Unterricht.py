# -*- coding: utf-8 -*-

"""
Module implementing Wochen_Unterricht.
"""
import datetime
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
#from hinzufuegen_Plan import hinzufügen
from sub.wochen_unterricht.hinzufuegen_Plan import hinzufügen
from sub.wochen_unterricht.Ui_Wochen_Unterricht import Ui_Dialog
from other.database import Database


class Wochen_Unterricht(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Wochen_Unterricht, self).__init__(parent)
        self.setupUi(self)
        self.te_KW.setText(str(datetime.date.today().isocalendar()[1]))
        print (datetime.date.today().isocalendar()[1])
       
        d1 = datetime.date.today().strftime("%Y")
        self.label_jahr.setText("- "+d1)
        print(d1)
        self.twData_anzeigen()
    
    def twData_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        self.tableWidget_Wochen_Plan.setColumnCount(5)
        colname = QTableWidgetItem("Mo")
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Di")
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Mi")
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Do")
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Fr")
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(4, colname)
        
        
        self.tableWidget_Wochen_Plan.setRowCount(1)
        sql = "SELECT * FROM kat_wochenplan"
        mycursor = db.select(sql)
        if mycursor == "backtolgin":
            self.back_to_login()
            return
            
        zeile = 0
        for z in mycursor: 
            for s in range(0, 5):
                self.tableWidget_Wochen_Plan.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tableWidget_Wochen_Plan .setItem(zeile,  s,  fielditem)
            zeile += 1
        
        mycursor.close()
        
        self.tableWidget_Wochen_Plan.resizeColumnsToContents()
        self.tableWidget_Wochen_Plan.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        #self.INFO("Alle Adressen werden in Tabelle angezeigt",  "I")
    
    
    
    
    @pyqtSlot()
    def on_pushButton_hauptmenue_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pushButton_excel_ausgabe_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(int, int)
    def on_tableWidget_Wochen_Plan_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        w = hinzufügen(self)
        w.show()#Öffnen das SettingGui
        w.Wochen_Tag.setText("mo")
        print(self.tableWidget_Wochen_Plan.horizontalHeaderItem(column).text())
        w.Wochen_Tag.setText(self.tableWidget_Wochen_Plan.horizontalHeaderItem(column).text())
        grid=self.tableWidget_Wochen_Plan.item(row,  column)
        print(grid)
        self.hide()#hide the current window
        # TODO: not implemented yet
       #raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_befor_KW_clicked(self):
        """
        Slot documentation goes here.
        """
        kw = int(self.te_KW.text())
        before = kw -1
        self.te_KW.setText(str(before))
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_next_KW_clicked(self):
        """
        Slot documentation goes here.
        """
        
        kw = int(self.te_KW.text())
        next = kw +1
        self.te_KW.setText(str(next))
        
    def closeEvent(self, event):
        self.parent().show()
        
