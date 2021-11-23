# -*- coding: utf-8 -*-

"""
Module implementing kat_presence.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem 
import os,  time
from pyreportjasper import JasperPy
from sub.XML.XML_Class import DBtoXML
from sub.presence.Ui_kat_presence import Ui_kat_presence
from other.database import Database
from sub.presence.kat_presence_suchen import kat_presence_suchen
class kat_presence(QDialog, Ui_kat_presence):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(kat_presence, self).__init__(parent)
        self.setupUi(self)
        self.cell_tw_anzeige()
    
    @pyqtSlot()
    def on_pb_suchen_clicked(self):
        self.suchen  = kat_presence_suchen(self)
        self.suchen.show()
    @pyqtSlot()
    def closeEvent(self, event):
        self.parent().show()
        
    @pyqtSlot()
    def on_pb_leeren_clicked(self):
        self.le_abwesenheitsgrund.setText("")
        self.le_kuerzel.setText("")
    @pyqtSlot()
    def cell_tw_anzeige(self):
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        self.tw_anzeige.setColumnCount(4)
#        print("nach ColumnCount")

#        print("nach HorizontalHeaderItem")
        colname = QTableWidgetItem("Kürzel")
#        print("nach colname Ausbildungsthema")
        self.tw_anzeige.setHorizontalHeaderItem(0, colname)
#        print("nach setHorizontalHeaderItem 2")
        colname = QTableWidgetItem("Abwesenheitsgrund")
        self.tw_anzeige.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Benutzername")
        self.tw_anzeige.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Änderung")
        self.tw_anzeige.setHorizontalHeaderItem(3, colname)



        self.tw_anzeige.setRowCount(1)
#        print("nach RowCount 1")
        sql = "SELECT Kürzel, Abwesenheitsgrund, Benutzername, Änderung FROM kat_presence"
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
            for s in range(0,  4):
                if s == 3:
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
    

        
    @pyqtSlot(int, int)
    def on_tw_anzeige_cellClicked(self, row, column):
        self.le_kuerzel.setText(self.tw_anzeige.item(row, 0).text())
        self.le_abwesenheitsgrund.setText(self.tw_anzeige.item(row, 1).text())
       
    @pyqtSlot()
    def on_pb_speichern_clicked(self):

        db = Database.get_instance(self)
        sql = "select * from kat_presence WHERE Kürzel = '" + self.le_kuerzel.text() + "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)

        if satz_len == 0:
            sql = "INSERT INTO kat_presence (Kürzel, Abwesenheitsgrund, Benutzername) \
            VALUES (%s, %s, %s)"
            val = (self.le_kuerzel.text(),  self.le_abwesenheitsgrund.text(), self.parent().label_eingeloggt_als.text())
            self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugabe 
        else:
            sql = "UPDATE kat_presence set Kürzel=%s, Abwesenheitsgrund=%s, Benutzername=%s" + " where Kürzel ='" + self.le_kuerzel.text() + "'"
            val = (self.le_kuerzel.text(),  self.le_abwesenheitsgrund.text(), self.parent().label_eingeloggt_als.text())
            self.INFO("Eintrag wurde in der Datenbank aktualisiert!",  "I")# info asugabe 
        db.insert(sql,  val)
        self.cell_tw_anzeige()
        self.le_abwesenheitsgrund.setText("")
        self.le_kuerzel.setText("")
    @pyqtSlot()
    def on_pb_loeschen_clicked(self):
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_presence WHERE Kürzel = '" + self.le_kuerzel.text() + "'"
        db.delete(sql)
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe 
        self.cell_tw_anzeige()
        self.le_abwesenheitsgrund.setText("")
        self.le_kuerzel.setText("")
    @pyqtSlot()
    def on_pb_hauptmenue_clicked(self):
        #print ("abc")
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pb_excel_clicked(self):
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "kat_presence")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            os.startfile("Excel\kat_presence.xlsx")
            self.INFO("Excel-Datei wurde erstellt.",  "I")
            
        except Exception as e:
            print(e)
            self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")
    
    @pyqtSlot()
    def on_pb_report_clicked(self):
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_presence")
        
            input_file = 'Reports/kat_presence.jasper'
            output = 'Reports/kat_presence'
            jasper = JasperPy()
            con={
            'driver':'generic',
            'jdbc_driver':'org.sqlite.JDBC',
            'jdbc_url':'jdbc:sqlite:kat.db'
            }
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])

            self.INFO("PDF-Datei wurde erstellt!",  "I")# info asugabe 
            
        except Exception:
            self.INFO("PDF-Datei wurde erstellt!",  "I")# info asugabe 
    
    @pyqtSlot()
    def on_pb_hilfe_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")

        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")


            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
