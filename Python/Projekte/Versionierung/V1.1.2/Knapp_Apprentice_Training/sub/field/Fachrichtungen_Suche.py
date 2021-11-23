# -*- coding: utf-8 -*-

"""
Module implementing Suche_Dialog.
"""
from other.database import Database
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *

from sub.field.Ui_Fachrichtungen_Suche import Ui_Suche_Dialog



class Suche_Dialog(QDialog, Ui_Suche_Dialog):
    """
    Class documentation goes here.
    """
    def closeEvent(self, event):
        self.parent().show()
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Suche_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.initDatabase()
        #self.initTableview()
        
    def initDatabase(self):
        self.mydb = Database.get_instance(self)
        
    @pyqtSlot()
    def on_btSuchen_clicked(self):
        
        wf = "Fachrichtung"
        f = self.leFachrichtungabk2.text()
        wb = "Bezeichnung"
        b = self.leFachrichtungbez2.text()
        if f != "" and b == "":
            self.tw_Anzeigen_suche(wf, f)
        elif f != "" and b !="":
            self.tw_Anzeigen_suche(wf, f, wb, b)
        elif f == "" and b !="":
            self.tw_Anzeigen_suche(wb, b)
        else:
            self.tw_Anzeigen_suche
    
    def tw_Anzeigen_suche(self,  wf = "",  f="", wb="",  b=""):
        self.setCursor(Qt.WaitCursor)
        self.twAnzeige_suche.setColumnCount(5)
        colname=QTableWidgetItem("Fachrichtung")
        self.twAnzeige_suche.setHorizontalHeaderItem(0,  colname)
        colname=QTableWidgetItem("Bezeichnung")
        self.twAnzeige_suche.setHorizontalHeaderItem(1,  colname)
        colname=QTableWidgetItem("Lehrjahre")
        self.twAnzeige_suche.setHorizontalHeaderItem(2,  colname)
        colname=QTableWidgetItem("Benutzername")
        self.twAnzeige_suche.setHorizontalHeaderItem(3,  colname)
        colname=QTableWidgetItem("Änderungsdatum")
        self.twAnzeige_suche.setHorizontalHeaderItem(4,  colname)
        
        self.twAnzeige_suche.setRowCount(1)
        db = Database.get_instance(self)
        
        if f != "" and b == "":
            print("if")
            sql="select fachrichtung, bezeichnung, lehrjahre, benutzername, aenderungsdatum from KAT_fachrichtungen WHERE " + wf + " LIKE '"+ f +"'"
        elif f != "" and b !="":
            print("elseif")
            sql = "select fachrichtung, bezeichnung, lehrjahre, benutzername, aenderungsdatum from KAT_fachrichtungen WHERE " + wf + " LIKE '"+ f + "' AND " + wb + " LIKE '" + b + "'"
        else :
            print("else")
            sql = "select fachrichtung, bezeichnung, lehrjahre, benutzername, aenderungsdatum from KAT_fachrichtungen"
        print(sql)
        mycursor = db.select(sql)
        
        if mycursor == "backtologin":
            self.back_to_login
            return
        zeile=0
        for z in mycursor:
            for s in range(0, 5):
                self.twAnzeige_suche.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.twAnzeige_suche.setItem(zeile, s, fielditem)
            zeile+=1
        
        self.twAnzeige_suche.resizeColumnsToContents()
        self.twAnzeige_suche.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
        
    @pyqtSlot(QModelIndex)    
    def on_twAnzeige_suche_doubleClicked(self, index):
        
        self.hide()
    
    @pyqtSlot(int, int)
    def Suchen(self):
        pass
    def on_twAnzeige_suche_cellClicked(self, row, column):
        self.parent().leFachrichtungabk.setText(self.twAnzeige_suche.item(row,  1).text())
        self.parent().leFachrichtungbez.setText(self.twAnzeige_suche.item(row,  2).text())
        self.parent().sbLehrjahre.setValue(float(self.twAnzeige_suche.item(row,  3).text()))
    def initTableview(self):
        if self.mydb.open():
#        try:
            self.mydb.open()
            self.sqlmodel = QSqlTableModel(self, self.mydb)
            self.sqlmodel.setTable("apprentice_fachrichtungen")
            self.sqlmodel.select()
            self.tableView_db.setModel(self.sqlmodel)
#            self.tableView_db.show() #zeigt den Inhalt der Tabelle an
            print("Daten der Tabelle werden angezeigt")
        else:
#        except Exception as err:
            print("Kann nicht zu Datenbank verbinden.")
#            print (str(err))
            
    @pyqtSlot()
    def on_pB_BEENDEN_clicked(self):
        """
        Slot documentation goes here.
        """
        self.hide() #schließen des aktuellen Dialogs

#app = QDialog(sys.argv)
#ui = Suche_Dialog()
#ui.show()
#sys.exit(app.exec_())
