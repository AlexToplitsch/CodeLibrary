# -*- coding: utf-8 -*-

"""
Module implementing Fachabteilungen.
"""

#from pyreportjasper import JasperPy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from xml.dom.minidom import *
import os
from other.database import Database
from sub.XML.XML_Class import DBtoXML
from sub.departments.Ui_Fachabteilung import Ui_Fachabteilungen
from sub.departments import Fachabteilungen_Suche

class Fachabteilungen(QDialog, Ui_Fachabteilungen):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Fachabteilungen, self).__init__(parent)
        self.setupUi(self)
        self.twAnzeige()
    
    def closeEvent(self, event):
        """
        Schließt das im Moment geöffnete Fenster(Fachrichtungen)
        """
        
        #self.parent().show()
        self.parent().setWindowOpacity(1.0)
        self.close()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
            
    
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        """
        Funktion für die Info-Zeile
        """
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
                
    def twAnzeige(self):
        """
        Methode zum befüllen der Spalten aus der Datenbank ins QTableWidget
        """
        db = Database.get_instance(self)
        self.setCursor(Qt.WaitCursor)
        
        self.tableWidget.setColumnCount(17)
        colname=QTableWidgetItem("Fachabteilung")
        self.tableWidget.setHorizontalHeaderItem(0,  colname)
        colname=QTableWidgetItem("Bezeichnung")
        self.tableWidget.setHorizontalHeaderItem(1,  colname)
        colname=QTableWidgetItem("Gebäude")
        self.tableWidget.setHorizontalHeaderItem(2,  colname)
        colname=QTableWidgetItem("Stock")
        self.tableWidget.setHorizontalHeaderItem(3,  colname)
        colname=QTableWidgetItem("Abteilungsleiter")
        self.tableWidget.setHorizontalHeaderItem(4,  colname)
        colname=QTableWidgetItem("AL-Tel-Nr.")
        self.tableWidget.setHorizontalHeaderItem(5,  colname)
        colname=QTableWidgetItem("AL-E-Mail")
        self.tableWidget.setHorizontalHeaderItem(6,  colname)
        colname=QTableWidgetItem("Ansprechperson")
        self.tableWidget.setHorizontalHeaderItem(7,  colname)
        colname=QTableWidgetItem("AP-Tel-Nr.")
        self.tableWidget.setHorizontalHeaderItem(8,  colname)
        colname=QTableWidgetItem("AP-E-Mail")
        self.tableWidget.setHorizontalHeaderItem(9,  colname)
        colname=QTableWidgetItem("Mo")
        self.tableWidget.setHorizontalHeaderItem(10,  colname)
        colname=QTableWidgetItem("Di")
        self.tableWidget.setHorizontalHeaderItem(11,  colname)
        colname=QTableWidgetItem("Mi")
        self.tableWidget.setHorizontalHeaderItem(12,  colname)
        colname=QTableWidgetItem("Do")
        self.tableWidget.setHorizontalHeaderItem(13,  colname)
        colname=QTableWidgetItem("Fr")
        self.tableWidget.setHorizontalHeaderItem(14,  colname)
        colname=QTableWidgetItem("Benutzername")
        self.tableWidget.setHorizontalHeaderItem(15,   colname)
        colname=QTableWidgetItem("Änderungsdatum")
        self.tableWidget.setHorizontalHeaderItem(16,  colname)
        self.tableWidget.setRowCount(1)
        
        sql = "SELECT FachabteilungAbk, FachabteilungBez, Gebäude, Stock, Abteilungsleiter, AL_Tel_Nr, AL_E_Mail, Ansprechsperson, AP_Tel_Nr, AP_E_Mail, wo_mo, wo_di, wo_mi, wo_do, wo_fr, Benutzer, Aenderung FROM kat_fachabteilungen"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile=0
        for z in mycursor:
            for s in range(0, 17):
                self.tableWidget.setRowCount(zeile+1)
                if s == 10:
                    fielditem = QTableWidgetItem("")
                    self.tableWidget.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 11:
                    fielditem = QTableWidgetItem("")
                    self.tableWidget.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 12:
                    fielditem = QTableWidgetItem("")
                    self.tableWidget.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 13:
                    fielditem = QTableWidgetItem("")
                    self.tableWidget.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s == 14:
                    fielditem = QTableWidgetItem("")
                    self.tableWidget.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(z[s]) == "1":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                if s < 10 or s > 14:
                    fielditem = QTableWidgetItem(str(z[s]))
                    self.tableWidget.setItem(zeile, s, fielditem)
            zeile += 1  
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        mycursor.close()
    
    @pyqtSlot()
    def on_btSpeichern_clicked(self):
        """
        Das Klickevent on_btSpeichern_clicked speichert die eingegebenen Daten in die Datenbank
        Diese werden dann mithilfe der Methode self.twAnzeigen() im QTableWidget aktualisiert.
        """
        if self.leFachabteilungabk.text() == "":
            self.twAnzeige()
        else: 
            db = Database.get_instance(self)
            sql= "select * from kat_fachabteilungen WHERE Fachabteilungabk='" + self.leFachabteilungabk.text() +"'"
            mycursor = db.select(sql)
            if mycursor == "backtologin":
                self.back_to_login
                return
            sql_satz = []

            sql_satz = mycursor.fetchall()
            satz_len = len(sql_satz)
            if satz_len == 0:
                sql = "INSERT INTO kat_fachabteilungen (Fachabteilungabk, Fachabteilungbez, Gebäude, Stock, Abteilungsleiter ,AL_Tel_Nr ,AL_E_Mail, Ansprechsperson, AP_Tel_Nr, AP_E_Mail, wo_mo, wo_di, wo_mi, wo_do, wo_fr, Benutzer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.leFachabteilungabk.text(), self.leFachabteilungbez.text(), self.leGebaeude.text(), self.leStock.text(), self.leAbteilungsleitername.text(), self.leAbteilungsleitertel.text(), self.leAbteilungsleitermail.text(),  self.leAnsprechspersonname.text(), self.leAnsprechspersontel.text(), self.leAnsprechspersonmail.text(), self.cbMo.isChecked(), self.cbDi.isChecked(), self.cbMi.isChecked(),  self.cbDo.isChecked(), self.cbFr.isChecked(), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in die Datenbank gespeichert! ",  "I")
            else:
                sql = "UPDATE kat_fachabteilungen SET fachabteilungbez=%s, gebäude=%s, stock=%s, abteilungsleiter=%s ,AL_Tel_Nr=%s, AL_E_Mail=%s, Ansprechsperson=%s, AP_Tel_Nr=%s, AP_E_Mail=%s, wo_mo=%s, wo_di=%s, wo_mi=%s, wo_do=%s, wo_fr=%s, Benutzer=%s WHERE fachabteilungabk = '" + self.leFachabteilungabk.text() + "'"
                val = (self.leFachabteilungbez.text(), self.leGebaeude.text(), self.leStock.text(), self.leAbteilungsleitername.text(), self.leAbteilungsleitertel.text(), self.leAbteilungsleitermail.text(),  self.leAnsprechspersonname.text(), self.leAnsprechspersontel.text(), self.leAnsprechspersonmail.text(), self.cbMo.isChecked(), self.cbDi.isChecked(), self.cbMi.isChecked(),  self.cbDo.isChecked(), self.cbFr.isChecked(), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in der Datenbank aktualisiert! ",  "I")
                
            db.insert(sql, val)
            self.leFachabteilungabk.setText("")
            self.leFachabteilungbez.setText("")
            self.leGebaeude.setText("")
            self.leStock.setText("")
            self.leAbteilungsleitername.setText("")
            self.leAbteilungsleitermail.setText("")
            self.leAbteilungsleitertel.setText("")
            self.leAnsprechspersonname.setText("")
            self.leAnsprechspersonmail.setText("")
            self.leAnsprechspersontel.setText("")
            self.leAnsprechspersonname.setText("")
            self.cbMo.setChecked(Qt.Unchecked)
            self.cbDi.setChecked(Qt.Unchecked)
            self.cbMi.setChecked(Qt.Unchecked)
            self.cbDo.setChecked(Qt.Unchecked)
            self.cbFr.setChecked(Qt.Unchecked)
            self.twAnzeige()

    @pyqtSlot(int, int)
    def on_tableWidget_cellClicked(self, row, column):
        """
        Übernimmt die angeklickte Zeile aus dem TableWidget in die lineEdits
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """ 
        self.leFachabteilungabk.setText(self.tableWidget.item(row, 0).text())
        self.leFachabteilungbez.setText(self.tableWidget.item(row, 1).text())
        self.leGebaeude.setText(self.tableWidget.item(row, 2).text())
        self.leStock.setText(self.tableWidget.item(row, 3).text())
        self.leAbteilungsleitername.setText(self.tableWidget.item(row, 4).text())
        self.leAbteilungsleitertel.setText(self.tableWidget.item(row, 5).text())
        self.leAbteilungsleitermail.setText(self.tableWidget.item(row, 6).text())
        self.leAnsprechspersonname.setText(self.tableWidget.item(row, 7).text())
        self.leAnsprechspersontel.setText(self.tableWidget.item(row, 8).text())
        self.leAnsprechspersonmail.setText(self.tableWidget.item(row, 9).text())
        self.cbMo.setChecked(self.tableWidget.item(row,  10).checkState())
        self.cbDi.setChecked(self.tableWidget.item(row,  11).checkState())
        self.cbMi.setChecked(self.tableWidget.item(row,  12).checkState())
        self.cbDo.setChecked(self.tableWidget.item(row,  13).checkState())
        self.cbFr.setChecked(self.tableWidget.item(row,  14).checkState())
        
    @pyqtSlot()
    def on_btCSV_clicked(self):
        """
        Erstellt eine Pdf aus der gezeigten Tabelle aus der Datenbank
        """
        self.INFO("Report Funktion wird noch hinzugefügt",  "I")
     
    @pyqtSlot()
    def on_btClear_clicked(self):
        """
        Cleart die Einträge aus den lineEdits und den Checkboxen
        """
        self.leFachabteilungabk.setText("")
        self.leFachabteilungbez.setText("")
        self.leGebaeude.setText("")
        self.leStock.setText("")
        self.leAbteilungsleitername.setText("")
        self.leAbteilungsleitermail.setText("")
        self.leAbteilungsleitertel.setText("")
        self.leAnsprechspersonname.setText("")
        self.leAnsprechspersonmail.setText("")
        self.leAnsprechspersontel.setText("")
        self.leAnsprechspersonname.setText("")
        self.cbMo.setChecked(Qt.Unchecked)
        self.cbDi.setChecked(Qt.Unchecked)
        self.cbMi.setChecked(Qt.Unchecked)
        self.cbDo.setChecked(Qt.Unchecked)
        self.cbFr.setChecked(Qt.Unchecked)
    @pyqtSlot()
    def on_btAbbrechen_clicked(self):
        """
        Schließt das aktuell offene Fenster(Fachabteilungen) und öffnet das mainwindow
        """
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_btExcel_clicked(self):
        """
        Öffnet und aktualisiert die Excel Datei
        """
        self.INFO("Excel-Datei wurde erstellt.",  "I")
        db = Database.get_instance(self)
        DBtoXML.MakeXML(db, "kat_fachabteilungen")
        
        os.startfile("Excel\kat_fachabteilungen.xlsx")
    @pyqtSlot()
    def on_btSuchen_clicked(self):
        """
        Öffnet einen Suche-Dialog
        """
        self.suchefenster = Fachabteilungen_Suche.Fachabteilungen_Suche(self)
        self.suchefenster.show()
    
    @pyqtSlot()
    def on_btLoeschen_clicked(self):
        """
        Löscht einen Eintrag aus der Datenbank
        """
        db = Database.get_instance(self)
        sql = "DELETE FROM kat_fachabteilungen WHERE fachabteilungabk = '" + self.leFachabteilungabk.text() + "'"
        db.delete(sql)
        self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht!",  "I")# info asugabe
        self.twAnzeige()
    
    @pyqtSlot()
    def on_btHilfe_clicked(self):
        """
        Hier wird eine Hilfe-Pdf geöffnet
        """
        
        self.INFO("Hilfe-Funktion wird noch Hinzugefügt! ",  "I")
