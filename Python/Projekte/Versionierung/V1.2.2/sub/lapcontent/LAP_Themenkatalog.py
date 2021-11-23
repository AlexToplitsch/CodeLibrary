# -*- coding: utf-8 -*-

"""
Module implementing Themenkatalog.
"""
from sub.XML.XML_Class import DBtoXML
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem,  QMessageBox
from sub.lapcontent.LAP_Suche import LAP_Themenkatalog_Suche
from sub.lapcontent.Ui_LAP_Themenkatalog import Ui_Dialog_Themenkatalog
from other.database import Database
import os, time
from pyreportjasper import JasperPy


class Themenkatalog(QDialog, Ui_Dialog_Themenkatalog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Themenkatalog, self).__init__(parent)
        self.setupUi(self)
        self.combobox_befüllen()
        
        
        
    @pyqtSlot()
    def on_pB_Hilfe_clicked(self):
        
        """
        Slot documentation goes here
        """
        QMessageBox.information(
        self,
        self.tr("Hilfe"),
        self.tr("""Die Hilfefunktion wird demnächst Hinzugefügt!"""))
    
    
    
    @pyqtSlot()
    def on_pB_Abbrechen_clicked(self):
        
        """
        Methode um Lehrstofffenster zu schließen und Hauptmenufenster zu öffnen
        """
        self.parent().show()
        self.close()
    
    
    
    @pyqtSlot(int, int)
    def on_tW_Db_Themenkatalog_cellClicked(self, row, column):
        
        """
        Methode um das Tablewidget aus der DB-Tabelle KAT_lap_themenkatalog zu befüllen
        """
        #QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        try:
            self.cB_Fachrichtung.setCurrentText(self.tW_Db_Themenkatalog.item(row, 0).text())
            self.le_Themen_ID.setText(self.tW_Db_Themenkatalog.item(row, 1).text())
            self.le_Hauptthema.setText(self.tW_Db_Themenkatalog.item(row, 2).text())
            self.le_Thema.setText(self.tW_Db_Themenkatalog.item(row, 3).text())
            self.cB_Ausbilder.setCurrentText(self.tW_Db_Themenkatalog.item(row, 4).text())
            self.le_lehrjahr.setText(self.tW_Db_Themenkatalog.item(row, 5).text())
            self.le_bs_jahr.setText(self.tW_Db_Themenkatalog.item(row, 6).text())
        except Exception as e:
            print(e)
            self.tW_Db_Themenkatalog_Anzeigen()
    
    
    
    @pyqtSlot()
    def on_pB_Speichern_clicked(self):
        
        """
        Methode um DB-Tabelle KAT_lap_themenkatalog zu befüllen oder zu aktualisieren
        """
        
        if self.cB_Fachrichtung.currentText() == "Alle Anzeigen":
            self.INFO("Bei Fachrichtung wurde nichts ausgewählt!",  "H")
            return
        if self.cB_Ausbilder.currentText() == "Alle Anzeigen":
            self.INFO("Bei Ausbilder wurde nichts ausgewählt!",  "H")
            return
        #datentabelle befüllen
        db = Database.get_instance(self)
        sql = "select * from KAT_lap_themenkatalog WHERE Fachrichtung = '" + self.cB_Fachrichtung.currentText() + "' AND Themen_ID = '" + self.le_Themen_ID.text() + "'"
        mycursor = db.select(sql)
        
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        if satz_len == 0:
            try:
                sql = "INSERT INTO KAT_lap_themenkatalog (Fachrichtung,Themen_ID, Hauptthema, Thema, Ausbilder, Lehrjahr, BS_Lehrjahr, Benutzer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.cB_Fachrichtung.currentText(),  self.le_Themen_ID.text(),self.le_Hauptthema.text(),   self.le_Thema.text(),  self.cB_Ausbilder.currentText(),  self.sB_Lehrjahr.value(), self.sB_BS_Jahr.value(), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in die Datenbank gespeichert",  "I")
                self.clearFields()
            except Exception:
                self.INFO("Eintrag konnte nicht in die Datenbank gespeichert werden",  "F")

        else:
            try:
                sql = "UPDATE KAT_lap_themenkatalog set Hauptthema=%s, Thema=%s, Ausbilder=%s, Lehrjahr=%s, BS_Lehrjahr=%s, Benutzer=%s" + " WHERE Fachrichtung = '" + self.cB_Fachrichtung.currentText() + "' AND Themen_ID = '" + self.le_Themen_ID.text() + "'"
                val = (self.le_Hauptthema.text(), self.le_Thema.text(),  self.cB_Ausbilder.currentText(),  self.sB_Lehrjahr.value(), self.sB_BS_Jahr.value(), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in der Datenbank aktualisiert." ,  "I")
                self.clearFields()
            except Exception:
                self.INFO("Eintrag konnte nicht in der Datenbank aktualisiert werdeb." ,  "F")

        mycursor = db.insert(sql, val)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        self.tW_Db_Themenkatalog_Anzeigen()
    
    
    
    @pyqtSlot()
    def on_pB_Suchen_clicked(self):
        
        """
        Slot documentation goes here
        """
        self.searchWindow = LAP_Themenkatalog_Suche(self)
        self.searchWindow.show()



    @pyqtSlot()
    def on_pB_Loeschen_clicked(self):
    
        """
        Methode um ausgewählte Zeile aus DB-Tabelle zu löschen
        """
        try:
            db = Database.get_instance(self)
            sql = "DELETE FROM kat_lap_themenkatalog WHERE Fachrichtung='" + self.cB_Fachrichtung.currentText()+ "'AND Themen_ID = '" + self.le_Themen_ID.text() + "'"
            mycursor = db.delete(sql)
            if mycursor == "backtologin":
                self.back_to_login()
                return
            self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht.",  "I")
        except Exception:
             self.INFO("Ausgewählter Eintrag konnte nicht aus der Datenbank gelöscht werden.",  "F")
        self.tW_Db_Themenkatalog_Anzeigen()
    
    
    
    @pyqtSlot(str)
    def on_cB_Fachrichtung_currentTextChanged(self, p0):
        
        self.tW_Db_Themenkatalog_Anzeigen()
    
    
    
    @pyqtSlot(str)
    def on_cB_Ausbilder_currentTextChanged(self, p0):

        self.tW_Db_Themenkatalog_Anzeigen()
    
    
    
    @pyqtSlot()
    def on_pB_Report_clicked(self):
        
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_lehrstoff")
            
            input_file = 'Reports\kat_lap_themenkatalog.jasper'
            output = 'Reports\kat_lap_themenkatalog'
            jasper = JasperPy()
            con={
                'driver':'generic',
                'jdbc_driver':'"org.sqlite.JDBC"',
                'jdbc_url':'jdbc:sqlite:kat.db'
            }
            
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            
            os.startfile("Reports\kat_lap_themenkatalog.pdf")
            self.INFO("PDF-Datei wurde erstellt.",  "I")
        except Exception:
            self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
    
    
    
    @pyqtSlot()
    def on_pB_Excel_clicked(self):
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "KAT_lap_themenkatalog")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            os.startfile("Excel\kat_lap_themenkatalog.xlsx")
            self.INFO("Excel-Datei wurde erstellt.",  "I")
        except Exception:
            self.INFO("Excel Datei konnte nicht erstellt werden!",  "F")
    
    
    
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
    def on_pB_ClearFields_clicked(self):
        """
        Slot documentation goes here.
        """
        self.clearFields()
        self.tW_Db_Themenkatalog_Anzeigen()


    def combobox_befüllen(self):
        
        """
        Methode für das Befüllen der Combobox aus den Datenbanktabellen KAT_fachrichtungen und
        KAT_ausbilder
        """
         
        self.cB_Fachrichtung_befuellen()
        self.cB_Ausbilder_befuellen()
        

      
    def cB_Fachrichtung_befuellen(self):
        #befüllen der ComboBox "cB_Fachrichtung" aus der DB KAT_fachrichtungen
        db = Database.get_instance(self)
        sql = "SELECT COUNT(*), Fachrichtung FROM kat_lap_themenkatalog GROUP BY Fachrichtung HAVING COUNT(*) > 1"
        mycursor = db.select(sql)
        
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        rows = mycursor.fetchall()
        print(rows)
        for i in rows:
            self.cB_Fachrichtung.addItem(str(i[1]))
    
    
    def cB_Ausbilder_befuellen(self):
        #befüllen der ComboBox "cB_Ausbilder" aus der DB KAT_ausbilder
        db = Database.get_instance(self)
        sql = "SELECT COUNT(*), Ausbilder FROM kat_lap_themenkatalog GROUP BY Ausbilder HAVING COUNT(*) > 1"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        rows = mycursor.fetchall()
        for i in rows:
            self.cB_Ausbilder.addItem(str(i[1]))
    
    def clearFields(self):
        
        self.cB_Fachrichtung.setCurrentText("")
        self.le_Themen_ID.setText("")
        self.le_Hauptthema.setText("")
        self.le_Thema.setText("")
        self.cB_Ausbilder.setCurrentText("")
        self.sB_Lehrjahr.setValue(0)
        self.sB_BS_Jahr.setValue(0)


    def tW_Db_Themenkatalog_Anzeigen(self):
        
        self.setCursor(Qt.WaitCursor)
        
        #überschriften setzen
        self.tW_Db_Themenkatalog.setColumnCount(9)
        #colname = QTableWidgetItem("ID")
        #self.tW_Db_Themenkatalog.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Fachrichtung")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Themen_ID")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Hauptthema")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Thema")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Ausbilder")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Lehrjahr")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("BS_Lehrjahr")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("Änderung")
        self.tW_Db_Themenkatalog.setHorizontalHeaderItem(8, colname)
        
        self.tW_Db_Themenkatalog.setRowCount(1)
        
        db = Database.get_instance(self)
        
        if self.cB_Ausbilder.currentText() != "" and self.cB_Fachrichtung.currentText() == "":
            sql =  "select Fachrichtung,Themen_ID,Hauptthema,Thema,Ausbilder,Lehrjahr,BS_Lehrjahr,Benutzer,Änderung from KAT_lap_themenkatalog WHERE Ausbilder= '" + self.cB_Ausbilder.currentText() + "'"
        elif self.cB_Ausbilder.currentText() == "" and self.cB_Fachrichtung.currentText() != "":
            sql =  "select Fachrichtung,Themen_ID,Hauptthema,Thema,Ausbilder,Lehrjahr,BS_Lehrjahr,Benutzer,Änderung from KAT_lap_themenkatalog WHERE Fachrichtung= '" + self.cB_Fachrichtung.currentText() + "'"
        else:
            sql = "select Fachrichtung,Themen_ID,Hauptthema,Thema,Ausbilder,Lehrjahr,BS_Lehrjahr,Benutzer,Änderung from KAT_lap_themenkatalog WHERE Ausbilder= '" + self.cB_Ausbilder.currentText() + "' AND Fachrichtung= '" + self.cB_Fachrichtung.currentText() + "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        
        zeile = 0 
        for z in mycursor:
            for s in range(0,  9):
                self.tW_Db_Themenkatalog.setRowCount(zeile + 1)
                fielditem = QTableWidgetItem(str(z[s]))
                self.tW_Db_Themenkatalog.setItem(zeile,  s,  fielditem)
            zeile+=1
                
        mycursor.close()
        
        self.tW_Db_Themenkatalog.resizeColumnsToContents()
        self.tW_Db_Themenkatalog.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
    
    
    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
        
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
        
    def keyPressEvent(self,  event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
    