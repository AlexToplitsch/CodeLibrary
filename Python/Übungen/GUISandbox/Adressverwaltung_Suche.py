# -*- coding: utf-8 -*-

"""
Module implementing Suche_Dialog.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QDialog
from Ui_Adressverwaltung_Suche import Ui_Dialog

class Suche_Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Suche_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.initDatabase()
        self.initTableview()
        
    def initDatabase(self):
        self.mydb = QSqlDatabase.addDatabase("QMYSQL")
        self.mydb.setHostName("localhost")
        self.mydb.setUserName("root")
        self.mydb.setPassword("")
        self.mydb.setDatabaseName("test")
#  
    def initTableview(self):
        if self.mydb.open():
#        try:
            self.mydb.open()
            self.sqlmodel = QSqlTableModel(self, self.mydb)
            self.sqlmodel.setTable("adressenverwaltung")
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
        self.close() #schließen des aktuellen Dialogs

#app = QDialog(sys.argv)
#ui = Suche_Dialog()
#ui.show()
#sys.exit(app.exec_())
