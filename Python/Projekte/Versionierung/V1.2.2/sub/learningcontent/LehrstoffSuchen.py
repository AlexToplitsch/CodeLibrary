# -*- coding: utf-8 -*-

"""
Module implementing Lehrstoff_Suche.
"""

from PyQt5 import *
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import  *
from other.database import Database

from sub.learningcontent.Ui_LehrstoffSuchen import Ui_Lehrstoff_Suche


class Lehrstoff_Suche(QDialog, Ui_Lehrstoff_Suche):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrstoff_Suche, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(int, int)
    def on_tW_Lehrstoff_DB_cellClicked(self, row, column):
        
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        try:
            self.parent().cB_Ausbildungsthema.setCurrentText(self.tW_Lehrstoff_DB.item(row, 0).text())
            self.parent().le_Lehrstoff_ID.setText(self.tW_Lehrstoff_DB.item(row, 1).text())
            self.parent().le_Hauptthema.setText(self.tW_Lehrstoff_DB.item(row, 2).text())
            self.parent().cB_Verantwortlicher.setCurrentText(self.tW_Lehrstoff_DB.item(row, 4).text())
            self.parent().le_Lehrstoff.setText(self.tW_Lehrstoff_DB.item(row, 3).text())
            if self.tW_Lehrstoff_DB.item(row, 5).text() == "Dokument vorhanden!":
                self.parent().lbl_Dokumentpfad.setText("Dokument vorhanden!")
            else:
                self.parent().lbl_Dokumentpfad.setText("Kein Dokument vorhanden!")
            self.parent().sB_Stunden.setValue(int(self.tW_Lehrstoff_DB.item(row, 6).text()))
            self.parent().le_Hilfsmittel.setText(self.tW_Lehrstoff_DB.item(row, 7).text())
            
            i = -1
            run = True
            while run == True:
                try:
                    i += 1
                    if self.tW_Lehrstoff_DB.item(row, 8).text() == "0" or str(self.parent().cB_Reference.itemData((i))) == "None":
                        self.parent().INFO("In diesem Themenkatalog ist kein Referenzthema mit dieser ID bekannt! Wechseln Sie den Referenzfilter!",  "H")
                        run = False
                    if str(self.parent().cB_Reference.itemData(i)) == self.tW_Lehrstoff_DB.item(row, 8).text():
                        self.parent().cB_Reference.setCurrentIndex(i)
                        self.parent().INFO("Referenz ID wurde gefunden!",  "I")
                        run = False
                except Exception:
                    run = False
                    
        except Exception as e:
            print(e)
            self.tW_Lehrstoff_DB_Anzeigen()
    
    @pyqtSlot(int, int)
    def on_tW_Lehrstoff_DB_cellDoubleClicked(self, row, column):
        
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        try:
            self.parent().cB_Ausbildungsthema.setCurrentText(self.tW_Lehrstoff_DB.item(row, 0).text())
            self.parent().le_Lehrstoff_ID.setText(self.tW_Lehrstoff_DB.item(row, 1).text())
            self.parent().le_Hauptthema.setText(self.tW_Lehrstoff_DB.item(row, 2).text())
            self.parent().cB_Verantwortlicher.setCurrentText(self.tW_Lehrstoff_DB.item(row, 4).text())
            self.parent().le_Lehrstoff.setText(self.tW_Lehrstoff_DB.item(row, 3).text())
            if self.tW_Lehrstoff_DB.item(row, 5).text() == "Dokument vorhanden!":
                self.parent().self.lbl_Dokumentpfad.setText("Dokument vorhanden!")
            else:
                self.parent().self.lbl_Dokumentpfad.setText("Kein Dokument vorhanden!")
            self.parent().sB_Stunden.setValue(int(self.tW_Lehrstoff_DB.item(row, 6).text()))
            self.parent().le_Hilfsmittel.setText(self.tW_Lehrstoff_DB.item(row, 7).text())
            
            i = -1
            run = True
            while run == True:
                try:
                    i += 1
                    if self.tW_Lehrstoff_DB.item(row, 8).text() == "0" or str(self.parent().cB_Reference.itemData((i))) == "None":
                        self.parent().INFO("In diesem Themenkatalog ist kein Referenzthema mit dieser ID bekannt! Wechseln Sie den Referenzfilter!",  "H")
                        run = False
                    if str(self.parent().cB_Reference.itemData(i)) == self.tW_Lehrstoff_DB.item(row, 8).text():
                        self.parent().cB_Reference.setCurrentIndex(i)
                        self.parent().INFO("Referenz ID wurde gefunden!",  "I")
                        run = False
                except Exception:
                    run = False            
            
            self.close()
        except Exception:
            self.tW_Lehrstoff_DB_Anzeigen()
        
    @pyqtSlot()
    def on_pB_Suchen_clicked(self):
        
        """
        Slot documentation goes here.
        """
        self.tW_Lehrstoff_DB_Anzeigen(self.le_Suchbegriff.text())
        self.le_Suchbegriff.setText("")
        
    
    @pyqtSlot()
    def on_pB_Beenden_clicked(self):
        
        """
        Slot documentation goes here.
        """
        self.hide()
        
    def tW_Lehrstoff_DB_Anzeigen(self, f1 = ""):
        
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tW_Lehrstoff_DB.setColumnCount(11)
        #colfachgebiet = QTableWidgetItem("ID")
        #self.tW_Lehrstoff_DB.setHorizontalHeaderItem(0, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Ausbildungsthema")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(0, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Lehrstoff_ID")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(1, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Hauptthema")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(2, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Lehrstoff")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(3, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Verantwortlicher")        
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(4, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Dokument")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(5, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Stunden")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(6, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Hilfsmittel")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(7, colfachgebiet)
        colfachgebiet = QTableWidgetItem("LAP-Referenz-ID")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(8, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Benutzer")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(9, colfachgebiet)
        colfachgebiet = QTableWidgetItem("Änderung")
        self.tW_Lehrstoff_DB.setHorizontalHeaderItem(10, colfachgebiet)
        
        self.tW_Lehrstoff_DB.setRowCount(1)
        
        db = Database.get_instance(self)

        if f1 != "":
            sql = "select * from kat_lehrstoff where concat(Ausbildungsthema, Lehrstoff_ID, Hauptthema, Lehrstoff, Verantwortlicher, Hilfsmittel) like '"+ '%' + f1 + '%' "'"
        else:
            sql = "select * from kat_lehrstoff"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        
        zeile = 0 
        for z in mycursor:
            for s in range(1,  12):
                self.tW_Lehrstoff_DB.setRowCount(zeile + 1)
                fielditem = QTableWidgetItem(str(z[s]))
                if s == 6:
                    if str(z[s]) == "None" or str(z[s]) == "b'0'" or str(z[s]) == "b' '":
                        fielditem = QTableWidgetItem("Kein Dokument vorhanden!")
                    else:
                        fielditem = QTableWidgetItem("Dokument vorhanden!")
                self.tW_Lehrstoff_DB.setItem(zeile,  s-1,  fielditem)
            zeile+=1
                
        mycursor.close()
        
        self.tW_Lehrstoff_DB.resizeColumnsToContents()
        self.tW_Lehrstoff_DB.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
        
    def keyPressEvent(self,  event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
