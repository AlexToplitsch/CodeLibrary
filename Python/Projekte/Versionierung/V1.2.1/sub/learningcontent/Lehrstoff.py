# -*- coding: utf-8 -*-

"""
Module implementing Lehrstoff.
"""
from sub.XML.XML_Class import DBtoXML 
from PyQt5 import *
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import  *
from other.database import Database
from sub.learningcontent.Ui_Lehrstoff import Ui_Dialog
from sub.learningcontent.LehrstoffSuchen import Lehrstoff_Suche

import time
import os
import tempfile
from pyreportjasper import JasperPy




class Lehrstoff(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrstoff, self).__init__(parent)
        self.setupUi(self)
        self.comboboxen_befuellen()
        self.tW_Datenbank_Anzeigen()
        self.binaryData = None
        self.file = ""
             
             
    @pyqtSlot()
    def on_pB_Abbrechen_clicked(self):
        """
        Methode um Lehrstofffenster zu schließen und Hauptmenufenster zu öffnen
        """
        self.parent().show()
        self.close()
    
    
    @pyqtSlot()
    def on_pB_Speichern_clicked(self):
        """
        Methode um DB-Tabelle kat_lehrstoff zu befüllen oder zu aktualisieren
        """
        if self.cB_Ausbildungsthema.currentText() == "Alle Anzeigen":
            self.INFO("Bei 'Ausbildungsthema' wurde nichts ausgewählt!",  "H")
            return
        if self.cB_Verantwortlicher.currentText() == "Alle Anzeigen":
            self.INFO("Bei 'Verantwortlichr' wurde nichts ausgewählt!",  "H")
            return
            
        try:
            #datentabelle befüllen
            db = Database.get_instance(self)
            sql =  "select * from kat_lehrstoff WHERE Ausbildungsthema = '" + self.cB_Ausbildungsthema.currentText() + "' AND Lehrstoff_ID = '" +self.le_Lehrstoff_ID.text()+"'"
            mycursor = db.select(sql)
            
            if mycursor == "backtologin":
                self.back_to_login()
                return
            
            sql_satz = []
            sql_satz =  mycursor.fetchall()
            satz_len = len(sql_satz)
            if satz_len == 0:
                sql = "INSERT INTO kat_lehrstoff (Ausbildungsthema, Lehrstoff_ID, Hauptthema, Lehrstoff, Verantwortlicher, Dokument, Stunden, Hilfsmittel, LAPThemenID, Benutzer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.cB_Ausbildungsthema.currentText(),  self.le_Lehrstoff_ID.text(), self.le_Hauptthema.text(),  self.le_Lehrstoff.text(), self.cB_Verantwortlicher.currentText(), self.binaryData,  self.sB_Stunden.value(), self.le_Hilfsmittel.text(), self.cB_Reference.itemData(self.cB_Reference.currentIndex()), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in die Datenbank gespeichert",  "I")
            else: 
                sql = "UPDATE kat_lehrstoff set Hauptthema=%s, Lehrstoff=%s, Verantwortlicher=%s, Dokument=%s, Stunden=%s, Hilfsmittel=%s, LAPThemenID=%s, Benutzer=%s" + " WHERE Ausbildungsthema='" + self.cB_Ausbildungsthema.currentText() + "' AND Lehrstoff_ID='" + self.le_Lehrstoff_ID.text()+"'"
                val = (
                self.le_Hauptthema.text(), self.le_Lehrstoff.text(), self.cB_Verantwortlicher.currentText(), self.binaryData,  self.sB_Stunden.value(), self.le_Hilfsmittel.text(),  self.cB_Reference.itemData(self.cB_Reference.currentIndex()), self.parent().label_eingeloggt_als.text())
                self.INFO("Eintrag wurde in der Datenbank aktualisiert." ,  "I")
            db.insert(sql, val)
            self.clearFields()
        except Exception as e:
                print(e)
                self.INFO("Eintrag konnte nicht aktualisiert werden!",  "F")

        self.tW_Datenbank_Anzeigen()


    @pyqtSlot()
    def on_pB_Loeschen_clicked(self):
        """
        Methode um ausgewählte Zeile aus DB-Tabelle zu löschen
        """
        db = Database.get_instance(self)
        try:
            sql = "DELETE FROM kat_lehrstoff WHERE Ausbildungsthema='" + self.cB_Ausbildungsthema.currentText()+ "'AND Lehrstoff_ID = '" + self.le_Lehrstoff_ID.text() + "'"
            db.delete(sql)
            self.tW_Datenbank_Anzeigen()
            self.INFO("Ausgewählter Eintrag wurde aus der Datenbank gelöscht.",  "I")
        except Exception:
            self.INFO("Ausgewählter Eintrag konnte nicht aus der Datenbank gelöscht werden.",  "F")

    
    @pyqtSlot()
    def on_pB_Hilfe_clicked(self):
        """
        Slot documentation goes here
        """
        QMessageBox.information(
        self,
        self.tr("Hilfe"),
        self.tr("""Die Hilfefunktion wird demnächst Hinzugefügt!"""))
        
    
    @pyqtSlot(int, int)
    def on_tW_Datenbank_cellClicked(self, row, column):
        """
        Methode um alle Lineedit, Comboboxen, etc. mit den ausgewählten werten zu befüllen.
        """
        try:
            self.cB_Ausbildungsthema.setCurrentText(self.tW_Datenbank.item(row, 0).text())
            self.le_Lehrstoff_ID.setText(self.tW_Datenbank.item(row, 1).text())
            self.le_Hauptthema.setText(self.tW_Datenbank.item(row,  2).text())
            self.le_Lehrstoff.setText(self.tW_Datenbank.item(row, 3).text())
            self.cB_Verantwortlicher.setCurrentText(self.tW_Datenbank.item(row, 4).text())
            self.lbl_Dokumentpfad.setText(self.tW_Datenbank.item(row, 5).text())
            self.sB_Stunden.setValue(int(self.tW_Datenbank.item(row, 6).text()))
            self.le_Hilfsmittel.setText(self.tW_Datenbank.item(row, 7).text())
            i = -1
            run = True
            while run == True:
                try:
                    i += 1
                    print(i)
                    print(str(self.cB_Reference.itemData((i))))
                    print(self.tW_Datenbank.item(row, 8).text())
                    if str(self.cB_Reference.itemData(i)) == self.tW_Datenbank.item(row, 8).text():
                        self.cB_Reference.setCurrentIndex(i)
                        run = False
                    if self.tW_Datenbank.item(row, 8).text() == "0":
                        return
                    
                except Exception as e:
                    print(e)
                    run = False
        except Exception:
            self.tW_Datenbank_Anzeigen()
                
    
    @pyqtSlot()
    def on_pB_Suchen_clicked(self):
        """
        Slot documentation goes here
        """
        self.searchWindow = Lehrstoff_Suche(self)
        self.searchWindow.show()


    @pyqtSlot()
    def on_tB_Dokument_Suchen_clicked(self):
        """
        Methode um ein Dokument aus einer Directory (Explorer-Suche) einzfügen
        """
        self.file = ""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,  "Wählen Sie ein PDF-Dokument aus!", "/",  "PDF Files (*.pdf)", options=options)
        self.file = fileName
        if fileName != None or fileName != "":
            try:
                self.setCursor(Qt.WaitCursor)
                with open(fileName, 'rb') as file:
                        self.binaryData = file.read()
                        if len(str(os.path.basename(fileName))) <= 30:
                            self.lbl_Dokumentpfad.setText(str(os.path.basename(fileName)))
                        else: 
                            self.lbl_Dokumentpfad.setText(str(os.path.basename(fileName))[:15]+ "..." + str(os.path.basename(fileName)[-11:]))
                self.setCursor(Qt.ArrowCursor)
            except Exception:
                self.setCursor(Qt.ArrowCursor)
        
        
    @pyqtSlot()
    def on_pB_Excel_clicked(self):
        """
        Methode um HTML Datei zu erstellen
        """
        try:
            db = Database.get_instance(self)
            DBtoXML.MakeXML(db, "kat_lehrstoff")
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            os.startfile("Excel\kat_lehrstoff.xlsx")
            self.setCursor(Qt.ArrowCursor)
            self.INFO("Excel-Datei wurde erstellt.",  "I")
            
        except Exception:
            self.INFO("Excel Datei konnte nicht erstellt werden: ",  "F")


    @pyqtSlot()
    def on_pB_Report_clicked(self):
        """
        Methode um PDF-Datei aufzurufen
        """
        try:
            db = Database.get_instance(self)
            db.writeSQLite("kat_lehrstoff")
            
            input_file = 'Reports\kat_lehrstoff.jasper'
            output = 'Reports\kat_lehrstoff'
            jasper = JasperPy()
            con={
                'driver':'generic',
                'jdbc_driver':'"org.sqlite.JDBC"',
                'jdbc_url':'jdbc:sqlite:kat.db'
            }
            
            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            os.startfile("Reports\kat_lehrstoff.pdf")
            self.setCursor(Qt.ArrowCursor)
            self.INFO("PDF-Datei wurde erstellt.",  "I")
        except Exception:
            self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
        
        
#    @pyqtSlot(str)
#    def on_cB_Ausbildungsthema_currentTextChanged(self, p0):
#        """
#        Slot documentation goes here.
#        
#        @param p0 DESCRIPTION
#        @type str
#        """
#        if p0 == "Alle Anzeigen":
#          self.clearFields()
#          
#        self.tW_Datenbank_Anzeigen("Ausbildungsthema", p0)
    
    
#    @pyqtSlot(str)
#    def on_cB_Verantwortlicher_currentTextChanged(self, p0):
#        """
#        Slot documentation goes here.
#        
#        @param p0 DESCRIPTION
#        @type str
#        """
#        if p0 == "Alle Anzeigen":
#            self.clearFields()
#        self.tW_Datenbank_Anzeigen("Verantwortlicher", p0)


    @pyqtSlot()
    def on_pB_ClearFields_clicked(self):
        """
        Slot documentation goes here.
        """
        self.clearFields()
        
        
    @pyqtSlot(str)
    def on_cB_Filter_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.referenz_cB_befüllen()
        
    
    @pyqtSlot()
    def on_pB_Dok_Anzeigen_clicked(self):
        """
        Nimmt das Dokument aus der Datenbanktabelle/ aus dem D
        """
        try:
            if self.lbl_Dokumentpfad.text() == "Dokument vorhanden!":
                db = Database.get_instance(self)
                sql = "select Dokument from kat_lehrstoff WHERE Lehrstoff = '" + self.le_Lehrstoff.text() + "'"
                mycursor = db.select(sql)
                document = mycursor.fetchone()[0]
                with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
                    f.write(document)
                    os.startfile(f.name)
                return
                
            elif self.lbl_Dokumentpfad.text() == "Kein Dokument vorhanden!":
                self.INFO("Für dieses Thema ist keine Datei vorhanden!.",  "H")
                return
                
            elif self.lbl_Dokumentpfad.text() == "":
                self.INFO("Kein Dokument ausgewählt!.",  "H")
                return
                
            if self.file != None or fileName != "":
                    os.startfile(self.file)
                    
        except Exception:
           pass
            
    
    def cB_Ausbildungsthema_befuellen(self):
        #befüllen der ComboBox "cB_Ausbildungsthema" aus der DB kat_fachgebiete
        
        db = Database.get_instance(self)
        sql = "SELECT kat_ausbildungsthemen.Ausbildungsthema FROM kat_ausbildungsthemen"
        mycursor = db.select(sql)
        rows = mycursor.fetchall()
        if mycursor == "backtologin":
            self.back_to_login()
            return
        self.cB_Ausbildungsthema.addItem("Alle Anzeigen")
        for i in rows:
            self.cB_Ausbildungsthema.addItem(i[0])
    
    
    def cB_Verantwortlicher_befuellen(self):
        #befüllen der ComboBox "cB_Verantwortlicher" aus der DB kat_ausbilder
        db = Database.get_instance(self)
        sql = "SELECT kat_ausbilder.Familienname FROM kat_ausbilder"
        mycursor = db.select(sql)
        rows2 = mycursor.fetchall()
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        self.cB_Verantwortlicher.addItem("Alle Anzeigen")
        for i in rows2:
            self.cB_Verantwortlicher.addItem(i[0])
            
    
    def cB_Filter_befuellen(self):
        #befüllen der Combobox "cB_Filter aus der der DB-Tabelle kat_fachrichtung
        db = Database.get_instance(self)
        sql = "SELECT KAT_fachrichtungen.Bezeichnung FROM KAT_fachrichtungen"
        mycursor = db.select(sql)
    
        if mycursor == "backtologin":
            self.back_to_login()
            return
            
        rows = mycursor.fetchall()
        self.cB_Filter.addItem("Alle Anzeigen")
        for i in rows:
            self.cB_Filter.addItem(i[0])
        
        
    def comboboxen_befuellen(self):
        """
        Methode für das Befüllen der Combobox aus den Datenbanktabellen kat_fachgebiete und
        kat_ausbilder
        """
        self.cB_Ausbildungsthema_befuellen()
        self.cB_Verantwortlicher_befuellen()
        self.cB_Filter_befuellen()
        self.referenz_cB_befüllen()
        
        
    def referenz_cB_befüllen(self):
        try:
            self.cB_Reference.clear()
            db = Database.get_instance(self)
            if self.cB_Filter.currentText() == "Alle Anzeigen":
                sql = "SELECT id, Themen_ID, Thema FROM kat_lap_themenkatalog"
            else: 
                sql = "SELECT id, Themen_ID, Thema FROM kat_lap_themenkatalog WHERE Fachrichtung = '" +self.cB_Filter.currentText()+"'"              #dazu noch eine on_current-textChanged (von der neuen CB) funktion wo die referenz_cb_befüllen methode aufgerufen wird
            mycursor = db.select(sql)
            rows = mycursor.fetchall()
            if mycursor == "backtologin":
                self.back_to_login()
                return
            for i in rows:
                self.cB_Reference.addItem(str(i[1]) + ": " + i[2],  i[0])
        except Exception:
            pass

    def tW_Datenbank_Anzeigen(self):
        """
        Methode um das Tablewidget aus der DB-Tabelle kat_lehrstoff zu befüllen
        """
        self.setCursor(Qt.WaitCursor)
        db = Database.get_instance(self)
        #überschriften setzen
        self.tW_Datenbank.setColumnCount(11)
        colname = QTableWidgetItem("Ausbildungsthema")
        self.tW_Datenbank.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Lehrstoff_ID")
        self.tW_Datenbank.setHorizontalHeaderItem(1,  colname)
        colname = QTableWidgetItem("Hauptthema")
        self.tW_Datenbank.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Lehrstoff")
        self.tW_Datenbank.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Verantwortlicher")
        self.tW_Datenbank.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Dokument")
        self.tW_Datenbank.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Stunden")
        self.tW_Datenbank.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("Hilfsmittel")
        self.tW_Datenbank.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("LAP-Referenz-ID")
        self.tW_Datenbank.setHorizontalHeaderItem(8, colname)
        colname = QTableWidgetItem("Benutzer")
        self.tW_Datenbank.setHorizontalHeaderItem(9, colname)
        colname = QTableWidgetItem("Änderung")
        self.tW_Datenbank.setHorizontalHeaderItem(10, colname)
        
        self.tW_Datenbank.setRowCount(1)

        sql = "select * from kat_lehrstoff"
            
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return
        zeile = 0 
     
        for z in mycursor:
            for s in range(1,  12):
                self.tW_Datenbank.setRowCount(zeile + 1)
                fielditem = QTableWidgetItem(str(z[s]))
                if s == 6:
                    if str(z[s]) != "None":
                        fielditem = QTableWidgetItem("Dokument vorhanden!")
                    else:
                        fielditem = QTableWidgetItem("Kein Dokument vorhanden!")
                self.tW_Datenbank.setItem(zeile,  s-1,  fielditem)
            zeile+=1
                
        mycursor.close()
        
        self.tW_Datenbank.resizeColumnsToContents()
        self.tW_Datenbank.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)
        
    def back_to_login(self):
        """
        Methode um bei Verbindungsabbruch zur DB 
        """
        self.parent().back_to_login()
        self.close()


    def clearFields(self):
        self.cB_Ausbildungsthema.setCurrentText("Alle Anzeigen")
        self.le_Lehrstoff_ID.setText("")
        self.cB_Verantwortlicher.setCurrentText("Alle Anzeigen")
        self.le_Hauptthema.setText("")
        self.le_Lehrstoff.setText("")
        self.lbl_Dokumentpfad.setText("")
        self.sB_Stunden.setValue(0)
        self.le_Hilfsmittel.setText("")
        
    
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
    
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")


    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
        
        
    def keyPressEvent(self,  event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
    
