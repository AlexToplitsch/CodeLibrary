# -*- coding: utf-8 -*-

"""
Module implementing Lehrlingseinteilungtabelle.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QMessageBox, QTableWidgetItem  
from sub.rotation.Ui_Lehrlingseinteilungstabelle import Ui_Dialog
from sub.rotation.Lehrlingseinteilung import Lehrlingseinteilung_App
from sub.XML.XML_Class import DBtoXML
from other.database import Database

import datetime
import os, time
from pyreportjasper import JasperPy


class Lehrlingseinteilungtabelle(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Lehrlingseinteilungtabelle, self).__init__(parent)
        self.setupUi(self)
        self.twData_anzeigen()
        
        self.actualDate = str(datetime.datetime.now().date())
        self.date1 = int(self.actualDate[:4])
        self.date2 = self.date1 - 1
    
    @pyqtSlot()
    def on_pB_leftArrow_clicked(self):
        """
        Slot documentation goes here.
        """
        self.date1 -= 1
        self.date2 -= 1
        self.lbl_Ausbildungsjahr.setText(str(self.date2) +"/" + str(self.date1))
        self.setCursor(Qt.WaitCursor)
        self.twData_anzeigen()
        self.setCursor(Qt.ArrowCursor)
    
    @pyqtSlot()
    def on_pB_rightArrow_clicked(self):
        """
        Slot documentation goes here.
        """
        self.date1 += 1
        self.date2 += 1
        self.lbl_Ausbildungsjahr.setText(str(self.date2) +"/" + str(self.date1))
        self.setCursor(Qt.WaitCursor)
        self.twData_anzeigen()
        self.setCursor(Qt.ArrowCursor)
    
    @pyqtSlot(int, int)
    def on_tW_Lehrlingseinteilung_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        self.w = Lehrlingseinteilung_App(self)
        self.w.setAusbildungswoche(column)
        self.w.setZeile(self.tW_Lehrlingseinteilung.item(row, 0).text() + ": " + self.tW_Lehrlingseinteilung.item(row, 1).text())
        self.w.show()
        print(row,  column)

    
    @pyqtSlot()
    def on_pB_Mainmenu_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pB_Export_Data_clicked(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(
            self,
            self.tr("Hilfe"),
            self.tr("""Die Exportfunktion wird demnächst Hinzugefügt!"""))
        
    #        try:
    #            db = Database.get_instance(self)
    #            db.writeSQLite("kat_einteilung", "Ausbildungsjahr=" + self.lbl_Ausbildungsjahr.text())
    #            
    #            input_file = 'Reports\Lehrlingseinteilung.jasper'
    #            output = 'Reports\Lehrlingseinteilung'
    #            jasper = JasperPy()
    #            con={
    #                'driver':'generic',
    #                'jdbc_driver':'"org.sqlite.JDBC"',
    #                'jdbc_url':'jdbc:sqlite:kat.db'
    #            }
    #            
    #            jasper.process(input_file,  output_file=output,  db_connection=con,  format_list=["pdf"])
    #            self.setCursor(Qt.WaitCursor)
    #            time.sleep(2)
    #            self.setCursor(Qt.ArrowCursor)
    #            
    #            os.startfile("Reports\Lehrlingseinteilung.pdf")
    #            self.INFO("PDF-Datei wurde erstellt.",  "I")
    #        except Exception:
    #            self.INFO("Report Datei konnte nicht erstellt werden: ",  "F")
        
    
    @pyqtSlot()
    def on_pB_Help_clicked(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(
            self,
            self.tr("Hilfe"),
            self.tr("""Die Hilfefunktion wird demnächst Hinzugefügt!"""))
        
        
    def twData_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """   
#---------------------------------------------------------set Columnheader------------------------------------------------------------------------------------------ 
        self.tW_Lehrlingseinteilung.removeRow(0)
        self.tW_Lehrlingseinteilung.setColumnCount(59)
        colname = QTableWidgetItem("Lehrling")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("P-Nr.")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Beruf")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Lj")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Berufsschule")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Ausbildungsjahr")
        self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(5, colname)
        kw = 34
        for i in range(6, 60):
            if kw == 54:
                kw = 1
            colname = QTableWidgetItem("KW " +str(kw))
            self.tW_Lehrlingseinteilung.setHorizontalHeaderItem(i,  colname)
            kw = kw + 1
            
        
        
      
#----------------------------------------------------------------------ersten 5 spalten befüllen--------------------------------------------------------------------------------------
        self.tW_Lehrlingseinteilung.setRowCount(1)
        db = Database.get_instance(self)
        mycursor = db.select("SELECT Vorname, Nachname, Personalnummer, Lehrberuf, Lehrbeginn from kat_lehrlinge") 
        zeile = 0
        for z in mycursor:
            self.tW_Lehrlingseinteilung.setRowCount(zeile + 1)
            
            fielditem = QTableWidgetItem(str(z[0]) + " " + str(z[1]))
            self.tW_Lehrlingseinteilung.setItem(zeile,  0,  fielditem)
            
            fielditem = QTableWidgetItem(str(z[2]))
            self.tW_Lehrlingseinteilung.setItem(zeile,  1,  fielditem)
            
            fielditem = QTableWidgetItem(str(z[3]))
            self.tW_Lehrlingseinteilung.setItem(zeile,  2,  fielditem)
    
            fielditem = QTableWidgetItem(str(self.getLehrjahr(str(z[4]))))
            self.tW_Lehrlingseinteilung.setItem(zeile,  3,  fielditem)
            zeile += 1
                
#---------------------------------------------------------------------- spalten je nach Einträge, updaten oder hinzufügen ----------------------------------------------------------------------------

        temp_zeile = zeile
        
        mycursor = db.select("SELECT * FROM kat_einteilung where Ausbildungsjahr = '" + self.lbl_Ausbildungsjahr.text() +"'" )
        for z in mycursor: 
            if self.tW_Lehrlingseinteilung.findItems(str(z[2]),  Qt.MatchExactly) != []: #sieht nach ob ein Eintrag mit der Anzeige im Tablewidget übereinstimmt
               for s in range(0, zeile): #sucht nach dem übereinstimmenden Eintrag im Tablewidget
                    if str(z[2]) == str(self.tW_Lehrlingseinteilung.item(s, 1).text()):#bei Übereinstimmung von den Personalnummern werden die Fielditems aktualisiert
                        for i in range(0,  59):#fielditems werden aktualisiert
                            fielditem = QTableWidgetItem(str(z[i+1]))
                            self.tW_Lehrlingseinteilung.setItem(s, i, fielditem)
                        break #bei fund for-schleife abbrechen
            else:
                for i in range(0,  59):
                    fielditem = QTableWidgetItem(str(z[i+1]))
                    self.tW_Lehrlingseinteilung.setItem(temp_zeile,  i,  fielditem)
            
        mycursor.close()#cursor wird geschlossen
        self.tW_Lehrlingseinteilung.resizeColumnsToContents()
        self.tW_Lehrlingseinteilung.resizeRowsToContents()  
        self.tW_Lehrlingseinteilung.sortItems(3,  order=Qt.AscendingOrder)
        
        
    def getLehrjahr(self, eintrittsdatum):
        
        eintritt_jahr = str(eintrittsdatum)[:4]
        eintritt_monat = str(eintrittsdatum)[5:7]
        eintritt_tag = str(eintrittsdatum)[8:10]
        dt_now = str(datetime.datetime.now())
        dt_jahr = dt_now[:4]
        dt_monat = dt_now[5:7]
        dt_tag = dt_now[8:10]
        LJ = int(dt_jahr) - int(eintritt_jahr)
        if int(eintritt_monat) < int(dt_monat):
            LJ += 1
        elif int(eintritt_monat) == int(dt_monat) and int(eintritt_tag) <= int(dt_tag):
            LJ += 1
        return LJ
            
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
        
    def keyPressEvent(self,  event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
