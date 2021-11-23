# -*- coding: utf-8 -*-

"""
Module implementing Unterrichtsthemen.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem,  QMessageBox
from sub.ausbildungsthemen.Ui_Unterrichtsthemen import Ui_Unterrichtsthemen
from other.database import Database
from sub.XML.XML_Class import DBtoXML
from pyreportjasper import JasperPy
import time,  os
from sub.ausbildungsthemen.Unterrichtsthemen_suchen import Unterrichtsthemen_suchen

class Unterrichtsthemen(QDialog, Ui_Unterrichtsthemen):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Unterrichtsthemen, self).__init__(parent)
        self.setupUi(self)
        self.cell_tw_anzeige()
        self.cb_ausbilder_befuellen()
        self.cb_ausbilder.setCurrentText("")
    
    @pyqtSlot(int, int)
    def on_tw_anzeige_cellClicked(self, row, column):
        self.le_name.setText(self.tw_anzeige.item(row, 1).text())
        self.cb_ausbilder.setCurrentText(self.tw_anzeige.item(row, 2).text())
    
    @pyqtSlot()
    def closeEvent(self, event):
        self.parent().show()
        
    @pyqtSlot()
    def on_pb_excel_clicked(self):
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "kat_unterrichtsthemen")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            os.startfile("Excel\kat_unterrichtsthemen.xlsx")
            self.INFO("Excel-Datei wurde erstellt.",  "I")
            
        except Exception as e:
            print(e)
            self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")
    
    @pyqtSlot()
    def on_pb_back_clicked(self):
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pb_delete_clicked(self):
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_ausbildungsthemen WHERE Ausbildungsthema = '" + self.le_name.text() + "'"
        db.delete(sql)
        self.cell_tw_anzeige()
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe 
    
    @pyqtSlot()
    def on_pb_report_clicked(self):
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_ausbildungsthemen")
        
            input_file = 'Reports/kat_unterrichtsthemen.jasper'
            output = 'Reports/kat_unterrichtsthemen'
            jasper = JasperPy()
            con={
            'driver':'generic',
            'jdbc_driver':'org.sqlite.JDBC',
            'jdbc_url':'jdbc:sqlite:kat.db'
            }
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])

            self.INFO("PDF-Datei wurde erstellt!",  "I")# info asugabe 
            os.startfile("Reports\kat_unterrichtsthemen.pdf")
            
        except Exception:
            self.INFO("PDF-Datei wurde erstellt!",  "I")# info asugabe 

        
    def cb_ausbilder_befuellen(self):
        db = Database.get_instance(self)
        sql = "SELECT Familienname FROM kat_ausbilder"
        mycursor = db.select(sql)
        ausbilder=[]
        for i in mycursor:
            ausbilder.append(i[0])
        self.cb_ausbilder.addItems(ausbilder)
        self.cb_ausbilder.addItem("")
        
    def cell_tw_anzeige(self):
        
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
#        print("nach Qt.WaitCursor")
        #überschriften setzen
        self.tw_anzeige.setColumnCount(5)
#        print("nach ColumnCount")
        colname = QTableWidgetItem("ID")
#        print("nach colname ID")
        self.tw_anzeige.setHorizontalHeaderItem(0, colname)
#        print("nach HorizontalHeaderItem")
        colname = QTableWidgetItem("Ausbildungsthema")
#        print("nach colname Ausbildungsthema")
        self.tw_anzeige.setHorizontalHeaderItem(1, colname)
#        print("nach setHorizontalHeaderItem 2")
        colname = QTableWidgetItem("Ausbilder")
        self.tw_anzeige.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Benutzername")
        self.tw_anzeige.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Änderungsdatum")
        self.tw_anzeige.setHorizontalHeaderItem(4, colname)



        self.tw_anzeige.setRowCount(1)
#        print("nach RowCount 1")
        sql = "SELECT * FROM kat_ausbildungsthemen"
#        print("nach Select")
        mycursor = db.select(sql)
        #mycursor.fetchall()
#        print("nach db.select")
        if mycursor == "backtologin":
#            print("nach mycursor backtologin")
            self.back_to_login()
#            print("nach self.backtologin")
            return
#            print("nach return")
        zeile = 0
        #print("nach Zeile = 0")
        for z in mycursor:
            #print("for z in mycursor")
            for s in range(0,  5):
                if s == 4:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.tw_anzeige.setItem(zeile,  s,  fielditem)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tw_anzeige.setRowCount(zeile+1)
                self.tw_anzeige.setItem(zeile,s ,fielditem)
            zeile += 1
            #print("in range")
            # self.tw_anzeige.setRowCount(zeile + 1)
            #print("setRowCount(zeile + 1")
        mycursor.close()
        #print("mycursor.close")
        self.tw_anzeige.resizeColumnsToContents()
        #print("1")
        self.tw_anzeige.resizeRowsToContents()
        #print("2")
        self.setCursor(Qt.ArrowCursor)
        #print("3")
    
    @pyqtSlot()
    def on_pb_hilfe_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pb_suchen_clicked(self):
        self.suchen  = Unterrichtsthemen_suchen(self)
        self.suchen.show()
    
    @pyqtSlot()
    def on_pb_speichern_clicked(self):


        db = Database.get_instance(self)
        sql = "select * from kat_ausbildungsthemen WHERE Ausbildungsthema = '" + self.le_name.text() + "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)

        if satz_len == 0:
            sql = "INSERT INTO kat_ausbildungsthemen (Ausbildungsthema, Ausbilder, Benutzername) \
            VALUES (%s, %s, %s)"
            val = (self.le_name.text(),  self.cb_ausbilder.currentText(), self.parent().label_eingeloggt_als.text())
            self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugabe 
        else:
            sql = "UPDATE kat_ausbildungsthemen set Ausbildungsthema=%s, Ausbilder=%s, Benutzername=%s" + " where Ausbildungsthema ='" + self.le_name.text() + "'"
            val = (self.le_name.text(),  self.cb_ausbilder.currentText(), self.parent().label_eingeloggt_als.text())
            self.INFO("Eintrag wurde in der Datenbank aktualisiert!",  "I")# info asugabe
        ct = self.cb_ausbilder.currentText()
        if ct == "":
            self.INFO("Eintrag konnte nicht gespeichert werden!",  "F")
            messageBox = QMessageBox(self)
            messageBox.setWindowTitle("Fehler")
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setText("Bitte geben Sie einen gültigen Ausbilder an!")
            messageBox.addButton("Okay", QMessageBox.NoRole) 
            messageBox.exec_()# info asugabe 
        else:
            db.insert(sql,  val)
            self.cell_tw_anzeige()
        
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")

            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
                

        
    @pyqtSlot()
    def on_pb_leeren_clicked(self):
        self.le_name.setText("")
        self.cb_ausbilder.setCurrentText("")


