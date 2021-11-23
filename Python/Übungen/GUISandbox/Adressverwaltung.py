# -*- coding: utf-8 -*-
"""
Module implementing Hauptmaske.
"""
from PyQt5.QtCore import pyqtSlot, QTranslator,  Qt
from PyQt5.QtWidgets import QApplication,  QDialog,  QTableWidgetItem, QLabel, QMessageBox
from Ui_Adressverwaltung import Ui_Hauptmaske
import sys,  datetime
from PyQt5.QtGui import QPixmap      #für Fotos
from PyQt5.QtGui import QCursor        #QCursor für Umstellen des Cursors
from PyQt5.QtGui import QIcon           #Icons zuweisbar machen
from cv2 import *                                #modul fürs Foto-Erstellung
#
from tkinter import messagebox          #gibt eine Message-BOX aus
import mysql.connector                       #Verbindung zur MySQL-DB: (Modul installieren mit: pip install mysql-connector)
import Adressverwaltung_Suche           #Zweiter Dialog aus Qt
import csv                                          #Modul für CSV-Datei-Ausgabe: pip install opencv-python 
from pyreportjasper import JasperPy    #JasperPy (Modul installieren mit: pip install pyreportjasper)
import subprocess                               #Subprozess (hier fürs Öffnen der PDF-Datei)
class Hauptmaske(QDialog, Ui_Hauptmaske):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Hauptmaske, self).__init__(parent)
        self.setupUi(self)
#
#       Übersetzungsdatei festlegen
        self.translator = QTranslator()
        self.translator.load("i18n/Adressverwaltung_en.qm")
        app.installTranslator(self.translator)
#       /       
#         Funktionen die beim Programmstart (init) aufrufen werden
        self.DB_verbinden() #Verbindung zur DB herstellen
        self.Dialog_Felder_vorbelegen() # Funktionsaufruf um Dialog-Felder  wie ComboBoxen zu befüllen
        self.Dialog_Tabelle_anzeigen() # Funktion zur Anzeige aller Einträge der DB-Tabelle
#
        label_logo = QLabel(self) #QLabel muss oben importiert werden
        label_logo = QPixmap('Knapp_Logo.png') #Bild/Logo wird dem Label-Widget zugewiesen
        self.label_logo.setPixmap(label_logo)
#
#----------------------------------------------------------------------------------------------------------
#   Funktionen
    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
            messagebox.showerror("Fehler", MELDUNG)
            res = QMessageBox.critical(
                self,
                self.tr("Fehler"),
                MELDUNG,
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
            print(res)
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")

                res = QMessageBox.information(
                self,
                self.tr("Information"),
                MELDUNG, 
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
                print(res)
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
#                      messagebox.showinfo("Information", MELDUNG)
#
    def uebersetzen(self, sprach_kz): #umstellen der Sprachdatei
        app.removeTranslator(self.translator)
        self.translator.load("i18n//Adressverwaltung_" + sprach_kz + ".qm")
        app.installTranslator(self.translator)
 #       ui.retranslateUi(self)
#
    def DB_verbinden(self): #Verbindung zur DB-Herstellen
        DB_String = {
            'host' : 'localhost',
            'user' : 'root', 
            'password' : '',  
            'database' : 'test'
            }
        global mydb
#  
        try: # SQL-Verbindung herstellen, Fehlerbehandlung
            mydb = mysql.connector.connect(**DB_String)
        except: #Fehler-Abhandlung
            self.INFO("Es konnte keine Verbindung zur Server-Datenbank hergestellt werden!",  "F")
            exit(0)
#
    def Dialog_Felder_vorbelegen(self):
        #Befüllung der ComboBox 'TITEL_1, _2, _3'
        self.TITEL_1.addItem(' ')
        self.TITEL_2.addItem(' ')
        self.TITEL_3.addItem(' ')
        
        self.TITEL_1.addItem('Dr.')
        self.TITEL_2.addItem('Dr.')
        self.TITEL_3.addItem('Dr.')
        
        self.TITEL_1.addItem('Mag.')
        self.TITEL_2.addItem('Mag.')
        self.TITEL_3.addItem('Mag.')

        self.TITEL_1.addItem('Ing.')
        self.TITEL_2.addItem('Ing.')
        self.TITEL_3.addItem('Ing.')

        self.TITEL_1.addItem('Dipl.Ing.')
        self.TITEL_2.addItem('Dipl.Ing.')
        self.TITEL_3.addItem('Dipl.Ing.')

        #Befüllung der ComboBox 'LAND', lesen der Einträge aus DB-Tabelle "Länder"
        mycursor = mydb.cursor()
        mycursor.execute("SELECT länder.LAND FROM LÄNDER")
        werte = [] #leere Liste erstellen
        for i in mycursor:
            werte.append(i[0])         #[0] entfernt die geschwungenen Klammern
        self.LAND.addItems (werte) #Werte aus Liste in ComboBox übernehmen
        mycursor.close()
#        self.LAND.addItem('USA')               # statischen Wert hinzufügen

        #Befüllen der ComboBox ANZEIGE_SPRACHE für Übersetzung/Fremdsprache: import QIcon
        self.ANZEIGE_SPRACHE.addItem(QIcon('/_symbole/icons/flags/flggerm.ico'), 'Deutsch') 
        self.ANZEIGE_SPRACHE.addItem(QIcon('/_symbole/icons/flags/flguk.ico'), 'Englisch')
        self.ANZEIGE_SPRACHE.addItem(QIcon('/_symbole/icons/flags/flgfran.ico'), 'Französisch')
        self.ANZEIGE_SPRACHE.addItem(QIcon('/_symbole/icons/flags/flgitaly.ico'), 'Italienisch')
#        
    def Dialog_Tabelle_anzeigen(self):
        self.setCursor(Qt.WaitCursor)
        self.DB_verbinden() #Verbindung zur DB herstellen

#        Überschrift ausgeben
        self.Daten_Tabelle.setColumnCount(18)
        colname = QTableWidgetItem("Firmen-Name")
        self.Daten_Tabelle.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Familien-Name")
        self.Daten_Tabelle.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Vor-Name(n)")
        self.Daten_Tabelle.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Titel-1")
        self.Daten_Tabelle.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Titel-2")
        self.Daten_Tabelle.setHorizontalHeaderItem(4, colname)
        colname = QTableWidgetItem("Titel-3")
        self.Daten_Tabelle.setHorizontalHeaderItem(5, colname)
        colname = QTableWidgetItem("Strasse")
        self.Daten_Tabelle.setHorizontalHeaderItem(6, colname)
        colname = QTableWidgetItem("Haus-Nr")
        self.Daten_Tabelle.setHorizontalHeaderItem(7, colname)
        colname = QTableWidgetItem("Land")
        self.Daten_Tabelle.setHorizontalHeaderItem(8, colname)
        colname = QTableWidgetItem("LKZ")
        self.Daten_Tabelle.setHorizontalHeaderItem(9, colname)
        colname = QTableWidgetItem("PLZ")
        self.Daten_Tabelle.setHorizontalHeaderItem(10, colname)
        colname = QTableWidgetItem("Ort")
        self.Daten_Tabelle.setHorizontalHeaderItem(11, colname)
        colname = QTableWidgetItem("Telefon-Nr gesch.")
        self.Daten_Tabelle.setHorizontalHeaderItem(12, colname)
        colname = QTableWidgetItem("Handy-Nr gesch.")
        self.Daten_Tabelle.setHorizontalHeaderItem(13, colname)
        colname = QTableWidgetItem("eMail gesch.")
        self.Daten_Tabelle.setHorizontalHeaderItem(14, colname)
        colname = QTableWidgetItem("Geb.-Datum")
        self.Daten_Tabelle.setHorizontalHeaderItem(15, colname)
        colname = QTableWidgetItem("Kinder")
        self.Daten_Tabelle.setHorizontalHeaderItem(16, colname)
        colname = QTableWidgetItem("F")
        self.Daten_Tabelle.setHorizontalHeaderItem(17, colname)
#   
#       Befüllung aus DB-Tabelle 'adressenverwaltung'
        self.Daten_Tabelle.setRowCount(1)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM adressenverwaltung")
        zeile = 0
        for z in mycursor: #Zeilen auslesen und ausgeben
            for s in range(0, 18): #Spalten auslesen und ausgeben
                self.Daten_Tabelle.setRowCount(zeile+1)
                fielditem = QTableWidgetItem(str(z[s])) # konvertiert zu String
                self.Daten_Tabelle.setItem(zeile, s , fielditem)
            zeile += 1
#   
        mycursor.close()
#
        self.Daten_Tabelle.resizeColumnsToContents()
        self.Daten_Tabelle.resizeRowsToContents()
        self.setCursor(Qt.ArrowCursor)        
        self.INFO("Alle Adressen werden in Tabelle angezeigt",  "I")
#
#------------------------------------------------------------------------------------------------------------
#
    @pyqtSlot(str)
    def on_LAND_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
#        if self.LAND.currentText() == 'Austria': self.LKZ.setText('A') # Abfrage+Zuweisung über Text
        mycursor = mydb.cursor()
        sql_satz = [] #Initialisierung für Abfrage (Alternative zu Retur-Code)
        sql = 'SELECT LKZ FROM länder WHERE LAND = "' + self.LAND.currentText() + '"'
        mycursor.execute(sql)
        sql_satz = mycursor.fetchall()
        mycursor.close()
        satz_len = len(sql_satz)
        if satz_len == 0: # Wenn 0 wurde kein Eintrag gefunden
            self.LKZ.setText('?')
            self.INFO("Es konnte kein Eintrag für in Länder-DB gefunden werden!",  "F")
        else:
            self.LKZ.setText(sql_satz[0][0])
            self.INFO("Länder-KZ wird angezeigt.",  "I")
#        
    @pyqtSlot()
    def on_rb_privat_clicked(self):
        """
        Slot documentation goes here.
        """
        print('p0')
#
    @pyqtSlot(str)
    def on_ANZEIGE_SPRACHE_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        if self.ANZEIGE_SPRACHE.currentText() == 'Englisch':
            self.uebersetzen("en") #Funktion mit Parameter "en" wird aufgerufen
            self.INFO("Maske wird in englischer Sprache angezeigt.",  "I")
        if self.ANZEIGE_SPRACHE.currentText() == 'Deutsch':
            self.uebersetzen("de") #Funktion mit Parameter "de" wird aufgerufen
            self.INFO("Maske wird in deutscher Sprache angezeigt.",  "I")
            
#
    @pyqtSlot()
    def on_pB_Suche_clicked(self):
        """
        Slot documentation goes here.
        """
        self.suchefenster = Adressverwaltung_Suche.Suche_Dialog()
        self.suchefenster.show()
#        self.suchefenster.exec()
#    
    @pyqtSlot()
    def on_pb_speichern_clicked(self):
        """
        Slot documentation goes here.
        """
#
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))   #cursor wird hier auf wait gesetzt 
        self.pb_speichern.setEnabled(False)#danach wird der Button enabled

        self.DB_verbinden() #Verbindung zur DB herstellen
#      Datensatz in Tabelle einfügen
        mycursor = mydb.cursor()
#
#       prüfen ob Satz mit KEY bereits vorhanden ist
        sql_satz = [] #Initialisierung für Abfrage (Alternative zu Return-Code)
        sql = "select * from adressenverwaltung WHERE FIRMEN_NAME = '" + self.FIRMEN_NAME.text() + "' AND FAM_NAME = '" + self.FAM_NAME.text()  + "' AND VOR_NAMEN = '"  + self.VOR_NAMEN.text() + "'"
        mycursor.execute(sql)
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        #GEB_DATUM = (self.GEB_DATUM.text ()[6:]+"-"+self.GEB_DATUM.text ()[3:5]+"-"+self.GEB_DATUM.text ()[:2] ) #Hilfsfeld
        if satz_len == 0: # Wenn 0 wurde kein Eintrag gefunden
            sql = "INSERT INTO adressenverwaltung (FIRMEN_NAME, FAM_NAME, VOR_NAMEN, TITEL_1, TITEL_2, TITEL_3, STRASSE, HAUS_NR, LAND, LKZ, PLZ, ORT, TELNR_GESCH, HANDY_GESCH, EMAIL_GESCH, GEB_DATUM, ANZ_KINDER, FUEHRERSCHEIN) VALUES \
       (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.FIRMEN_NAME.text(), self.FAM_NAME.text(), self.VOR_NAMEN.text(),  self.TITEL_1.currentText(), self.TITEL_2.currentText(),  self.TITEL_3.currentText(), self.STRASSE.text(),  self.HAUS_NR.text(), self.LAND.currentText(), \
            self.LKZ.text(),  self.PLZ.text(),  self.ORT.text(),  self.TELNR_GESCH.text(),  self.HANDY_GESCH.text (),  self.EMAIL_GESCH.text (),  self.GEB_DATUM.text (),  self.ANZ_KINDER.value(),  self.FUEHRERSCHEIN.isChecked() )     
            self.INFO("schreiben=insert",  "I")
        else:
            sql = "UPDATE adressenverwaltung set TITEL_1=%s, TITEL_2=%s, TITEL_3=%s, STRASSE=%s, HAUS_NR=%s, LAND=%s, LKZ=%s, PLZ=%s, ORT=%s, TELNR_GESCH=%s, HANDY_GESCH=%s, EMAIL_GESCH=%s, GEB_DATUM=%s, ANZ_KINDER=%s, FUEHRERSCHEIN=%s" \
            +  " where FIRMEN_NAME = '"  + self.FIRMEN_NAME.text() + "' and FAM_NAME ='" + self.FAM_NAME.text() + "' and VOR_NAMEN ='" + self.VOR_NAMEN.text()  + "'"
            val = (self.TITEL_1.currentText(), self.TITEL_2.currentText(),  self.TITEL_3.currentText(), self.STRASSE.text(),  self.HAUS_NR.text(), self.LAND.currentText(), self.LKZ.text(),  self.PLZ.text(),  self.ORT.text(), self.TELNR_GESCH.text(),  \
            self.HANDY_GESCH.text (),  self.EMAIL_GESCH.text (),  self.GEB_DATUM.text (),  self.ANZ_KINDER.value(),  self.FUEHRERSCHEIN.isChecked()  )
            self.INFO("ändern=update",  "I")
        try:
            result  =  mycursor.execute(sql, val)
            print(result)
            mydb.commit() # SQL-Freigabe nach schreiben
            self.INFO("Datensatz wurde erfolgreich in ADRESSVERWALTUNG eingetragen/geändert",  "I")

            QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))    
            res = QMessageBox.information(
                self,
                self.tr("Erfolgreich"),
                self.tr("""Datensatz wurde erfolgreich eingetragen/geändert """),
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
            print(res)

        except mysql.connector.Error as error:
            print(result)
            print("Datensatz konnte nicht in ADRESSENVERWALTUNG eingetragen/geändert werden {}".format(error))
#            self.MELDUNG = "Datensatz konnte nicht in ADRESSENVERWALTUNG eingetragen/geändert werden {}".format(error))
            self.INFO("Datensatz konnte nicht in ADRESSENVERWALTUNG eingetragen/geändert werden",  "I")

            res = QMessageBox.critical(
                self,
                self.tr("FEHLER"),
                self.tr("""Datensatz konnte nicht eingetragen/geändert werden !"""))
            print(res)
            
        finally:
            #closing database connection.
            if(mydb.is_connected()):
                mycursor.close()
                mydb.close()
                print("MySQL Verbindung ist geschlossen")            
                self.pb_speichern.setEnabled(True)
#        
#        mycursor.close()
        self.Dialog_Tabelle_anzeigen() # Funktion zur Anzeige aller Einträge der DB-Tabelle
#
    @pyqtSlot(int, int)
    def on_Daten_Tabelle_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))    

#       print(self.Daten_Tabelle.item(row, 0).text())
        self.FIRMEN_NAME.setText(self.Daten_Tabelle.item(row, 0).text())
        self.FAM_NAME.setText(self.Daten_Tabelle.item(row, 1).text())
        self.VOR_NAMEN.setText(self.Daten_Tabelle.item(row, 2).text())
        self.TITEL_1.setCurrentText(self.Daten_Tabelle.item(row, 3).text())
        self.TITEL_2.setCurrentText(self.Daten_Tabelle.item(row, 4).text())
        self.TITEL_3.setCurrentText(self.Daten_Tabelle.item(row, 5).text())
        self.STRASSE.setText(self.Daten_Tabelle.item(row, 6).text())
        self.HAUS_NR.setText(self.Daten_Tabelle.item(row, 7).text())
        self.LAND.setCurrentText(self.Daten_Tabelle.item(row, 8).text())
        self.LKZ.setText(self.Daten_Tabelle.item(row, 9).text())
        self.PLZ.setText(self.Daten_Tabelle.item(row, 10).text())
        self.ORT.setText(self.Daten_Tabelle.item(row, 11).text())
        self.TELNR_GESCH.setText(self.Daten_Tabelle.item(row, 12).text())
        self.HANDY_GESCH.setText(self.Daten_Tabelle.item(row, 13).text())
        self.EMAIL_GESCH.setText(self.Daten_Tabelle.item(row, 14).text())
#        
        GEB_DATUM = datetime.datetime.strptime(self.Daten_Tabelle.item(row, 15).text(),  "%d.%m.%Y") #String in Datums-Format umwandeln
        self.GEB_DATUM.setDate(GEB_DATUM)
#
        ANZ_KINDER = int(self.Daten_Tabelle.item(row, 16).text())
        self.ANZ_KINDER.setValue(ANZ_KINDER)
#
        self.FUEHRERSCHEIN.setChecked(int(self.Daten_Tabelle.item(row, 17).text())) # ändert den Status der CheckBox
#

#         Foto anzeigen
        PFAD = 'D:/Python/Projekte/Adressverwaltung/BILDER' + '/' + self.Daten_Tabelle.item(row,  0).text() + self.Daten_Tabelle.item(row,  2).text() + self.Daten_Tabelle.item(row,  1).text() + ".jpg"
        self.FOTO.show()
        try:
            FOTO = QLabel(self)
            FOTO = QPixmap(PFAD)
            FOTO = FOTO.scaledToWidth(180)
            self.FOTO.setPixmap(FOTO)  
        except:
            self.INFO("Keine Fotodatei >" + PFAD + "< zu diesen Daten gefunden", "F")
#
        self.INFO("Angeklickte Daten werden zur Bearbeitung angezeigt",  "I")
        QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))    
#        
    @pyqtSlot()
    def on_pb_loeschen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.DB_verbinden() #Verbindung zur DB herstellen
#         Datensatz in Tabelle einfügen
        mycursor = mydb.cursor()
#
#         prüfen ob Satz mit KEY bereits vorhanden ist
        sql_satz = [] #Initialisierung für Abfrage (Alternative zu Retur-Code)
        sql = "select * from adressenverwaltung WHERE FIRMEN_NAME = '" + self.FIRMEN_NAME.text() + "' AND FAM_NAME = '" + self.FAM_NAME.text()  + "' AND VOR_NAMEN = '"  + self.VOR_NAMEN.text() + "'"
        mycursor.execute(sql)
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        if satz_len == 0: # Wenn 0 wurde kein Eintrag gefunden
            self.INFO("Es konnte kein Eintrag in der Daten-Tabelle gefunden werden!",  "F")
        else:
            sql = "delete from adressenverwaltung WHERE FIRMEN_NAME = '" + self.FIRMEN_NAME.text() + "' AND FAM_NAME = '" + self.FAM_NAME.text()  + "' AND VOR_NAMEN = '"  + self.VOR_NAMEN.text() + "'"

            filename = 'D:/Python/Projekte/Adressverwaltung/BILDER' + '/' + self.FIRMEN_NAME.text() + self.VOR_NAMEN.text() + self.FAM_NAME.text() +".jpg" # Name der Foto-Datei
            if os.path.exists(filename):
                os.remove(filename)
                self.FOTO.hide() #löscht die Anzeige des Fotos
            else:
              print("Die Foto-Datei ist nicht vorhanden")  

        try:
            result  =  mycursor.execute(sql)
            print(result)
            mydb.commit() # SQL-Freigabe nach schreiben
            print ("Datensatz wurde erfolgreich in ADRESSVERWALTUNG gelöscht")
        except mysql.connector.Error as error:
            print("Datensatz konnte nicht in ADRESSENVERWALTUNG gelöscht werden {}".format(error))
#
#        mycursor.close()
        self.Dialog_Tabelle_anzeigen() # Funktion zur Anzeige aller Einträge der DB-Tabelle
#    
    @pyqtSlot()
    def on_pB_CSV_EXPORT_clicked(self):
        """
        Slot documentation goes here.
        """
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor)) #Mauszeiger auf "Wait" umstellen
        self.CSV_DATEI_SCHRIEBEN()#        Funktionsaufruf zur Ausgabe der DB-Tabelle 'adressenverwaltung' in CSV-Datei
        QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor)) #Mauszeiger wieder auf "Pfeil" zurück setzen
        self.INFO("Alle Daten wurden in D:\Python\CSV\Adressenverwaltung.csv exportiert.",  "H")
#
    def CSV_DATEI_SCHRIEBEN(self):
        sql_satz = [] #Definition der Ausgabe-Zwischentabelle aus SQL-Abfrage
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM adressenverwaltung")
        sql_satz = mycursor.fetchall() #befüllen der Ausgabe-Zwischentabelle aus SQL-Abfrage
        mycursor.close()
#
###         sql_satz in Einezlfelder aufteilen und mit write schreiben (ohne Standard-CSV-Funktion)  
##        csv_out = open("D:\Python\CSV\Adressenverwaltung.csv","w") #öffnen der CSV-Datei
##        zeile = 0
##        for z in sql_satz: #Zeilen auslesen und ausgeben
##            
##            FIRMA_CSV = sql_satz[zeile][0]
##            FAM_NAME_CSV = sql_satz[zeile][1]   
##            VOR_NAMEN_CSV = sql_satz[zeile][2]   
##               
##            csv_out.write( FIRMA_CSV  + ";"
##                                + FAM_NAME_CSV + ";"
##                                + VOR_NAMEN_CSV +
##                                '\n' )
## 
##            zeile += 1
##        csv_out.close() #schließen der CSV-Datei
###         /  
#       Funktion für CVS-Ausgabe nutzen
        csvdatei="D:\Python\CSV\Adressenverwaltung.csv"
        try: 
            with open(csvdatei, 'w', newline="\n", encoding="cp1252") as csvfile:
                csvwriter = csv.writer(csvfile,  delimiter = ';',  quotechar = '"',  quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerows(sql_satz)
                csvfile.close() #schließen der CSV-Datei
                self.INFO("Alle Daten wurden in D:\Python\CSV\Adressenverwaltung.csv exportiert.",  "I")
        except:
            msb_return = QMessageBox.critical(
                self,
                self.tr("Fehler bei CSV-Ausgabe"),
                self.tr("""Die CSV-Datei konnte nicht erstellt werden!"""),
                QMessageBox.StandardButtons(
                    QMessageBox.Ok))
            print(msb_return) #Ausgabe in Konsole
#
    @pyqtSlot()
    def on_pB_Report_oeffnen_clicked(self):
        """
        Slot documentation goes here.
        """
#
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor)) #Mauszeiger auf "Wait" umstellen
#    
#        Ausgabe der DB-Tabelle 'adressenverwaltung' in CSV-Datei
        self.CSV_DATEI_SCHRIEBEN()
        self.INFO("Alle Daten wurden in D:\Python\CSV\Adressenverwaltung.csv exportiert, Report wird aufgerufen.",  "I")
        
#       Jasper-Report starten um PDF-Datei zu erzeugen    
        input_file = 'Adressenverwaltung.jrxml'
#           output = 'MyReports' # Ziel-/SUB-Ordner
        output = ''
        jasper = JasperPy()
        jasper.process(
        input_file,
        output_file=output,
        parameters={},
        db_connection={
            'driver':'generic', 
            'jdbc_driver':'sun.jdbc.odbc.JdbcOdbcDriver',
            'jdbc_url':'jdbc:odbc:Lehrlings-APP-CSV-Dateien'
        },
        locale='de_DE', 
        format_list=["pdf"]
        )
        self.INFO("Datei Adressenverwaltung.pdf wurde erstellt.",  "I")
#       / damit sollte im Verzeichnis die Datei 'Adressenverwaltung.pdf' erzeugt worden sein
#
#        anzeigen der PDF-Datei
        self.INFO("Datei Adressenverwaltung.pdf wird geöffnet.",  "I")
        subprocess.Popen ("Adressenverwaltung.pdf",  shell=True)
#    
        QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor)) #Mauszeiger wieder auf "Pfeil" zurück setzen
#          
        
    @pyqtSlot()
    def on_pb_Foto_erstellen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.pb_Foto_erstellen.setEnabled(False)
        res = QMessageBox.information(# der Text dient als Info für die Bedienung der Funktion
            self,
            self.tr("FOTO"),
            self.tr("""Bitte gerade in die Kamera schauen und ok-Button anklicken.

Drücken sie dann "S" um das Foto zu speichern oder "X" und "D" um abzubrechen."""),
            QMessageBox.StandardButtons(
                QMessageBox.Ok|
                QMessageBox.Cancel))

        if res == QMessageBox.Ok:# wenn auf ok gedrückt wurde 
            print(res)
            FOTO = self.FIRMEN_NAME.text() + self.VOR_NAMEN.text() + self.FAM_NAME.text() + ".jpg"# wie das Foto im Zielordner heißen soll 
            cam = cv2.VideoCapture(0)   # 0 -> index of camera
            img = cam.read()
            PFAD = 'D:/Python/Projekte/Adressverwaltung/BILDER'#Pfad in dem das Foto gespeichert werden soll 
            camera = cv2.VideoCapture(0)
            while True:
                return_value,image = camera.read()
               # img = cv2.cvtColor(image,cv2.COLOR_RGB2HLS)
                img = (image)
                cv2.imshow('image',img)
                if cv2.waitKey(1)& 0xFF == ord('s'): # wenn "S" gedrücht wurde, wird das Foto gespeichert 
                    try:
                        self.FOTO_delete() #Aufruf um vorheriges Foto das im Ordner eventuell vorhanden ist
                        cv2. imwrite(os.path.join(PFAD, FOTO),img) 
                    except :
                        print("kein Bild")
                        cv2. imwrite(os.path.join(PFAD, FOTO),img) 
                    break                                                                           # schließt dann die "KAMERA"l
                    res = QMessageBox.information(
                        self,
                        self.tr("GESICHERT"),
                        self.tr("""Ihr Bild wurde in " D:\Python\Projekte\Adressverwaltung\BILDER" gespeichert.

                                File = "Firmenname+Vorname+Nachname.jpg)"""))
                    print(res)
                    
                if cv2.waitKey(2)& 0xFF == ord('d'):#wenn d gedrückt wurde wird das Fenster geschlossen 
                    print("lololololol")
                    camera.release()
                    cv2.destroyAllWindows() 
#                    cv2.destroycam()           
                    break
                    self.INFO("Es wurde kein Foto erstellt!", "I")
            camera.release()
            cv2.destroyAllWindows()            
        self.pb_Foto_erstellen.setEnabled(True)
#
#         gerade erstelltes Foto anzeigen
        FOTO_DATEI = PFAD + '/' + FOTO
        self.FOTO.show()
        try:
            FOTO = QLabel(self)
            FOTO = QPixmap(FOTO_DATEI)
            FOTO = FOTO.scaledToWidth(180)
            self.FOTO.setPixmap(FOTO)  
        except:
            self.INFO("Keine Fotodatei >" + FOTO_DATEI + "< zu diesen Daten gefunden", "F")
#
#
    def FOTO_delete():#die Funktion ist notwendig um ein vorhandenes Foto einer Person zu löschen damit das neue Foto gespeichert wrden kann
        filename = self.FIRMEN_NAME.text() + self.VOR_NAMEN.text() + self.FAM_NAME.text() + ".jpg" # Name der Foto-Datei
        for filename in os.listdir(pfad_zum_ordner):# hier wird es im Ordner gesucht
            os.remove(filename)    # Datei löschen
#
# ---------------------------------------------------- ---------------------------------------------------------------      
# notwendig um Programm ausführen zu können   
#   
app = QApplication(sys.argv)
ui = Hauptmaske() #Name der bei der Anlage der Dialog-Klasse verwendet wurde
ui.show()
sys.exit(app.exec_())
#
