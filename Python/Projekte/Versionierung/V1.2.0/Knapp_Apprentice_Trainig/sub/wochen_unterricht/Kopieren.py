# -*- coding: utf-8 -*-

"""
Module implementing Kopieren.
"""
from other.database import Database
import datetime
from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from sub.wochen_unterricht.Ui_Kopieren import Ui_Dialog


class Kopieren(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Kopieren, self).__init__(parent)
        self.setupUi(self)
        d1 = datetime.date.today().strftime("%Y")
        self.label_jahr.setText(d1+"-")
        self.label_jahr_E.setText(d1+"-")
        self.te_KW.setText(str(datetime.date.today().isocalendar()[1]))
        self.te_KW_E.setText(str(datetime.date.today().isocalendar()[1]))
        self.twData_anzeigen_K()
        self.twData_anzeigen_E()



    def twData_anzeigen_K(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        self.tableWidget_copy.clear()
        db = Database.get_instance(self)
        self.tableWidget_copy.setColumnCount(5)
        colname = QTableWidgetItem("Montag")
        self.tableWidget_copy.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Dienstag")
        self.tableWidget_copy.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Mittwoch")
        self.tableWidget_copy.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Donnerstag")
        self.tableWidget_copy.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Freitag")
        self.tableWidget_copy.setHorizontalHeaderItem(4, colname)
        
        self.tableWidget_copy.setRowCount(1)
        
        #mycursor = mydb.cursor()
        #mycursor = mydb.cursor()
        mycursor = db.select("SELECT * FROM kat_wochen_unterricht where Woche='"+self.label_jahr.text()+self.te_KW.text()+"'" )# sql befehl auf die ganze "adressenverwaltung" tabelle 
        self.tableWidget_copy.setRowCount(20) #konstante Anzahl von Zeilen in Tabelle
        for z in mycursor : 
            for s in range(0, 14): #Anzahl der Felder=Spalten
                fielditem = QTableWidgetItem(str(z[4])+" "+str(z[5])+"\n"+str(z[6])+"\n"+str(z[3])+"\n"+str(z[7])+"\n"+str(z[8]))
                fielditem.setTextAlignment(4)
                line = int(z[2]) -1
                if s == 1:
                    if str(z[s]) == "1": #Monatg
                        self.tableWidget_copy.setItem(line, 0,  fielditem)
                if s == 1:
                    if str(z[s]) == "2": #Dienstag
                        self.tableWidget_copy.setItem(line,  1,  fielditem)
                if s == 1:
                    if str(z[s]) == "3": #Mittwoch
                        self.tableWidget_copy.setItem(line,  2,  fielditem)
                if s == 1:
                    if str(z[s]) == "4": #Donnerstag
                        self.tableWidget_copy.setItem(line,  3,  fielditem)
                if s == 1:
                    if str(z[s]) == "5": #Freitag
                        self.tableWidget_copy.setItem(line,  4,  fielditem)
#       
        mycursor.close()#cursor wird geschlossen
        self.tableWidget_copy.resizeColumnsToContents()
        self.tableWidget_copy.resizeRowsToContents()       
        header_h= self.tableWidget_copy.horizontalHeader()
        header_v= self.tableWidget_copy.verticalHeader()
        for i in range(20):
            header_h.resizeSection(i, 140)
            header_v.resizeSection(i, 100)       
            self.tableWidget_copy.setColumnWidth(100000, 100000)
            
    def twData_anzeigen_E(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """
        self.tableWidget_E.clear()
        db = Database.get_instance(self)
        self.tableWidget_E.setColumnCount(5)
        colname = QTableWidgetItem("Montag")
        self.tableWidget_E.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Dienstag")
        self.tableWidget_E.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Mittwoch")
        self.tableWidget_E.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Donnerstag")
        self.tableWidget_E.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Freitag")
        self.tableWidget_E.setHorizontalHeaderItem(4, colname)
        
        self.tableWidget_E.setRowCount(1)
        
        #mycursor = mydb.cursor()
        #mycursor = mydb.cursor()
        mycursor = db.select("SELECT * FROM kat_wochen_unterricht where Woche='"+self.label_jahr_E.text()+self.te_KW_E.text()+"'" )# sql befehl auf die ganze "adressenverwaltung" tabelle 
        self.tableWidget_E.setRowCount(20) #konstante Anzahl von Zeilen in Tabelle
        for z in mycursor : 
            for s in range(0, 14): #Anzahl der Felder=Spalten
                fielditem = QTableWidgetItem(str(z[4])+" "+str(z[5])+"\n"+str(z[6])+"\n"+str(z[3])+"\n"+str(z[7])+"\n"+str(z[8]))
                fielditem.setTextAlignment(4)
                line = int(z[2]) -1
                if s == 1:
                    if str(z[s]) == "1": #Monatg
                        self.tableWidget_E.setItem(line, 0,  fielditem)
                if s == 1:
                    if str(z[s]) == "2": #Dienstag
                        self.tableWidget_E.setItem(line,  1,  fielditem)
                if s == 1:
                    if str(z[s]) == "3": #Mittwoch
                        self.tableWidget_E.setItem(line,  2,  fielditem)
                if s == 1:
                    if str(z[s]) == "4": #Donnerstag
                        self.tableWidget_E.setItem(line,  3,  fielditem)
                if s == 1:
                    if str(z[s]) == "5": #Freitag
                        self.tableWidget_E.setItem(line,  4,  fielditem)
#       
        mycursor.close()#cursor wird geschlossen
        self.tableWidget_E.resizeColumnsToContents()
        self.tableWidget_E.resizeRowsToContents()       
        header_h= self.tableWidget_E.horizontalHeader()
        header_v= self.tableWidget_E.verticalHeader()
        for i in range(20):
            header_h.resizeSection(i, 140)
            header_v.resizeSection(i, 100)       
            self.tableWidget_E.setColumnWidth(100000, 100000)
            
            
            
    @pyqtSlot()
    def on_pushButton_vor_clicked(self):
        """
        Slot documentation goes here.
        """
        kw = int(self.te_KW.text())
        before = kw -1
        self.te_KW.setText(str(before))
        self.twData_anzeigen_K()
    
    @pyqtSlot()
    def on_pushButton_weiter_clicked(self):
        """
        Slot documentation goes here.
        """
        kw = int(self.te_KW.text())
        weiter = kw +1
        self.te_KW.setText(str(weiter))
        self.twData_anzeigen_K()
    
    @pyqtSlot()
    def on_pushButton_vor_E_clicked(self):
        """
        Slot documentation goes here.
        """
        kw = int(self.te_KW_E.text())
        before = kw -1
        self.te_KW_E.setText(str(before))
        self.twData_anzeigen_E()
        
    
    
    @pyqtSlot()
    def on_pushButton_weiter_E_clicked(self):
        """
        Slot documentation goes here.
        """
        kw = int(self.te_KW_E.text())
        weiter = kw +1
        self.te_KW_E.setText(str(weiter))
        self.twData_anzeigen_E()
    
    @pyqtSlot()
    def on_pushButton_copy_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        db = Database.get_instance(self)
      #  sql = "SELECT * FROM kat_wochen_unterricht WHERE Woche='" + self.label_jahr.text()+self.te_KW.text() +"' and Tag='" + str(spalte) + "' and Zeile='" + w.Row.text() + "'" # sql-Befehl
        select_= "SELECT Tag, Zeile, von_bis, Unterrichtsthema, Ausbilder, Platz_Raum,Klassen,Lehrlinge,Informationen,Ausbildungsthema_1,Ausbildungsthema_2,Ausbildungsthema_3,Benutzer,Aenderung,Datum FROM kat_wochen_unterricht WHERE Woche='"+self.label_jahr.text()+self.te_KW.text() +"'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
        print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        for i in range(satz_len):
           # select_= "SELECT Tag, Zeile, von_bis, Unterrichtsthema,Ausbilder, Platz_Raum, Klassen, Lehrlinge,Informationen,Ausbildungsthema_1,Ausbildungsthema_2,Ausbildungsthema_3,Benutzer,Aenderung FROM kat_wochen_unterricht WHERE Woche'"+self.label_jahr.text()+self.te_KW.text()+"'"
            #+self.Wochen_Tag.text()+") \
            sql = "INSERT INTO kat_wochen_unterricht (Woche, Tag, Zeile, von_bis, Unterrichtsthema, Ausbilder, Platz_Raum,Klassen,Lehrlinge,Informationen,Ausbildungsthema_1,Ausbildungsthema_2,Ausbildungsthema_3,Benutzer,Aenderung,Datum)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val =(self.label_jahr_E.text()+self.te_KW_E.text(),str(inhalt[i][0]),str(inhalt[i][1]),str(inhalt[i][2]),str(inhalt[i][3]),str(inhalt[i][4]),str(inhalt[i][5]),str(inhalt[i][6]),str(inhalt[i][7]),str(inhalt[i][8]),str(inhalt[i][9]),str(inhalt[i][10]),str(inhalt[i][11]),str(inhalt[i][12]),str(inhalt[i][13]),str(inhalt[i][14]))
           # val =(self.parent().label_jahr.text()+self.parent().te_KW.text(),str(spalte),self.Row.text(),self.timeEdit_von.text()+"-"+self.timeEdit_bis.text(),self.comboBox_Unterrichtsthema.currentText(),self.comboBox_Ausbilder.currentText(),self.comboBox_Raum.currentText(),self.te_vorschau.item(3, 0).text(),self.te_vorschau.item(4, 0).text(),self.le_information.text(),self.comboBox_Thema1.currentText(),self.comboBox_Thema2.currentText(),self.comboBox_Thema3.currentText(),"root","2020-12-14 09:05:42", datum)


            db.insert(sql,  val)
            print("-----"+str(inhalt[i]))
            print("-----"+str(val))

        # self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugab
            
        self.twData_anzeigen_E()
        inhalt=""
       # mycursor.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
    
    @pyqtSlot()
    def on_pushButton_abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().setWindowOpacity(1.0)
        self.close()

    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()
