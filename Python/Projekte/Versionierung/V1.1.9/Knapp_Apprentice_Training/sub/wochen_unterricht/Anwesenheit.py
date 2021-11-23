# -*- coding: utf-8 -*-

"""
Module implementing anwesenheit.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from other.database import Database
from sub.wochen_unterricht.Ui_Anwesenheit import Ui_Dialog


class anwesenheit(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(anwesenheit, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_Speichern_Abwesenheit.setEnabled(False)
        self.twData_anzeigen()
        self.checkBox_Alle_Anwesend.setCheckState(Qt.Checked)
        
        
    def twData_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """

        self.tableWidget.clear()
        db = Database.get_instance(self)
        self.tableWidget.setColumnCount(3)
        colname = QTableWidgetItem("Name")
        self.tableWidget.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Anwesend ")
        self.tableWidget.setHorizontalHeaderItem(1, colname)        
        colname = QTableWidgetItem("Grund der Abwesenheit ")
        self.tableWidget.setHorizontalHeaderItem(2, colname)

        if self.parent().Wochen_Tag.text().find("Montag") != -1:
            spalte=1
        if self.parent().Wochen_Tag.text().find("Dienstag") != -1: 
            spalte=2        
        if self.parent().Wochen_Tag.text().find("Mittwoch") != -1: 
            spalte=3        
        if self.parent().Wochen_Tag.text().find("Donnerstag") != -1: 
            spalte=4        
        if self.parent().Wochen_Tag.text().find("Freitag") != -1: 
            spalte=5
            
        print(self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text())
        print(str(spalte))
        print(self.parent().Row.text())
        sql= "SELECT Woche,Tag,Zeile from kat_wochen_unterricht where Woche='"+self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"'and Tag='"+str(spalte)+"'and Zeile='"+self.parent().Row.text()+"'" 
        mycursor = db.select(sql)
        for i in mycursor : 
            test=str(i[0])+"-"+str(i[1])+"-"+str(i[2])
            
            print(test)
     
    
        mycursor = db.select("SELECT Name,Anwesend,AbwesenheitsGrund FROM kat_anwesenheit_abwesenheit where ID_Woche='"+test+"'")
        self.tableWidget.setRowCount(3) #konstante Anzahl von Zeilen in Tabelle
        zeile = 0

        for i in mycursor : 
            for s in range(0, 3):
                fielditem = QTableWidgetItem(i[s])
                self.tableWidget.setRowCount(zeile+1)
                self.tableWidget.setItem(zeile, s , fielditem)
                if s == 1:
                    fielditem = QTableWidgetItem("")
                    self.tableWidget.setItem(zeile, s, fielditem)
                    fielditem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    if str(i[s]) == "ja":
                        fielditem.setCheckState(Qt.Checked)
                    else:
                        fielditem.setCheckState(Qt.Unchecked)
                                                
                if s < 1 or s >1:
                    fielditem = QTableWidgetItem(str(i[s]))
                    self.tableWidget.setItem(zeile,  s,  fielditem)                
                
                
            zeile +=1# damit es eine Zeile weiter geht (ist eigentlich das gleiche wie "\n"
#       
        mycursor.close()#cursor wird geschlossen
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()       

            
            
    @pyqtSlot(int)
    def on_checkBox_Alle_Anwesend_stateChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type int
        """
        db = Database.get_instance(self)
        nein = "nein"
        ja = "ja"
        self.pushButton_Speichern_Abwesenheit.setEnabled(True)
        if self.parent().Wochen_Tag.text().find("Montag") != -1:
            spalte=1
        if self.parent().Wochen_Tag.text().find("Dienstag") != -1: 
            spalte=2        
        if self.parent().Wochen_Tag.text().find("Mittwoch") != -1: 
            spalte=3        
        if self.parent().Wochen_Tag.text().find("Donnerstag") != -1: 
            spalte=4        
        if self.parent().Wochen_Tag.text().find("Freitag") != -1: 
            spalte=5        
        sql = "select * from kat_anwesenheit_abwesenheit  WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"' and Name='"+self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text()+"'" 
        mycursor = db.select(sql)
        print(sql)
        print(mycursor)
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        for i in range(satz_len):
           # select_= "SELECT Tag, Zeile, von_bis, Unterrichtsthema,Ausbilder, Platz_Raum, Klassen, Lehrlinge,Informationen,Ausbildungsthema_1,Ausbildungsthema_2,Ausbildungsthema_3,Benutzer,Aenderung FROM kat_wochen_unterricht WHERE Woche'"+self.label_jahr.text()+self.te_KW.text()+"'"
            #+self.Wochen_Tag.text()+") \


            if self.checkBox_Alle_Anwesend.checkState() == Qt.Checked:
                sql = "UPDATE kat_anwesenheit_abwesenheit set Anwesend=%s" + " WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"'" 
                print(sql)
                val = (ja )
                print(val)
                db.insert(sql,  val)
                print("CHECKED")
                    
            if self.checkBox_Alle_Anwesend.checkState() ==Qt.Unchecked:
                sql = "UPDATE kat_anwesenheit_abwesenheit set Anwesend=%s" + " WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"'"
                print(sql)
                val = (nein )
                print(val)
                db.insert(sql,  val)
                print("Unchecked")
        
        
    
#        if self.checkBox_Alle_Anwesend.checkState() == Qt.Checked:
#
#            for i in range(self.tableWidget.rowCount()):                
#                self.tableWidget.item(i, 1).setCheckState(Qt.Checked)
#                    
#            
#                self.on_tableWidget_cellClicked(i, 1)
##        else:
##            res = QMessageBox.question(
##                self,
##                self.tr("Voreinstellungen löschen?"),
##                self.tr("""Wenn Sie jetzt auf  'ok' klicken, werden die Voreinstellungen gelöscht und alle Checkboxen werden auf 'Nicht angeklickt' gesetzt. Wenn Sie die Voreinstellungen beibehalten wollen klicken Sie auf 'Speichern'"""),
##                QMessageBox.StandardButtons(
##                    QMessageBox.Abort |
##                    QMessageBox.Ok |
##                    QMessageBox.Save))
##            print(res)
##            
##            if res == QMessageBox.Ok: 
##                for i in range(self.tableWidget.rowCount()):                
##                    self.tableWidget.item(i, 1).setCheckState(Qt.Unchecked)
##            if res == QMessageBox.Save: 
##                self.twData_anzeigen()
#
#
#            
##        self.parent().show()
##        self.close()
# 
    
    @pyqtSlot()
    def on_pushButton_Speichern_Abwesenheit_clicked(self):
        """
        Slot documentation goes here.
        """
        
        if self.parent().Wochen_Tag.text().find("Montag") != -1:
            spalte=1
        if self.parent().Wochen_Tag.text().find("Dienstag") != -1: 
            spalte=2        
        if self.parent().Wochen_Tag.text().find("Mittwoch") != -1: 
            spalte=3        
        if self.parent().Wochen_Tag.text().find("Donnerstag") != -1: 
            spalte=4        
        if self.parent().Wochen_Tag.text().find("Freitag") != -1: 
            spalte=5
            
     
        db = Database.get_instance(self)
        sql = "select * from kat_anwesenheit_abwesenheit  WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"' and Name='"+self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text()+"'" 
        mycursor = db.select(sql)
        print(sql)
        print(mycursor)

        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        print(sql_satz)
        print(satz_len)
        if satz_len == 0:
            
            print("---------------------------------------------------------------------------------------------------------------")
            
        else:
            sql = "UPDATE kat_anwesenheit_abwesenheit set AbwesenheitsGrund=%s, Name=%s" + " WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"' and Name='"+self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text()+"'" 
            print(sql)
            val = (self.comboBox_Abwesenheit.currentText(), self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text())
            print(val)
            db.insert(sql,  val)
    
    @pyqtSlot()
    def on_pushButton_Abbrechen_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().setWindowOpacity(1.0)
        self.close()
    
    @pyqtSlot()
    def on_pushButton_Speichern_clicked(self):
        """
        Slot documentation goes here.
        """
        #self.parent().show()
        self.parent().setWindowOpacity(1.0)
        self.close()
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close() 
    def keyPressEvent(self, event):
            if event.key() == Qt.Key_Escape:
                self.parent().setWindowOpacity(1.0)
                self.close()
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """


        db = Database.get_instance(self)

        vorname, nachname=self.tableWidget.item(row,  0).text().split(" ")
        self.lineEdit_Vorname.setText(vorname)
        self.lineEdit_Nachname.setText(nachname)
        self.comboBox_Abwesenheit.setCurrentText(self.tableWidget.item(row,  2).text())
        self.pushButton_Speichern_Abwesenheit.setEnabled(True)
        if self.parent().Wochen_Tag.text().find("Montag") != -1:
            spalte=1
        if self.parent().Wochen_Tag.text().find("Dienstag") != -1: 
            spalte=2        
        if self.parent().Wochen_Tag.text().find("Mittwoch") != -1: 
            spalte=3        
        if self.parent().Wochen_Tag.text().find("Donnerstag") != -1: 
            spalte=4        
        if self.parent().Wochen_Tag.text().find("Freitag") != -1: 
            spalte=5        

        if self.tableWidget.item(row, 1).checkState() == Qt.Checked:
            sql = "select * from kat_anwesenheit_abwesenheit  WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"' and Name='"+self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text()+"'" 
            mycursor = db.select(sql)
            print(sql)
            print(mycursor)
            sql_satz = []
            sql_satz = mycursor.fetchall()
            satz_len = len(sql_satz)
            #vorschau= self.te_vorschau.item(0, 0).text()+"\n "+self.te_vorschau.item(1, 0).text()+"\n "+ self.te_vorschau.item(2, 0).text()+"\n "+self.te_vorschau.item(3, 0).text()+"\n "+self.te_vorschau.item(4, 0).text()
            if satz_len != 0:
                sql = "UPDATE kat_anwesenheit_abwesenheit set Name=%s, Anwesend=%s" + " WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"' and Name='"+self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text()+"'" 
                print(sql)
                val = (self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text(),"ja" )
                print(val)
                db.insert(sql,  val)
                print("CHECKED")
                
        if self.tableWidget.item(row, 1).checkState() == Qt.Unchecked:
            sql = "UPDATE kat_anwesenheit_abwesenheit set Name=%s, Anwesend=%s" + " WHERE ID_Woche = '" +self.parent().parent().label_jahr.text()+self.parent().parent().te_KW.text()+"-"+str(spalte)+"-"+self.parent().Row.text()+"' and Name='"+self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text()+"'" 
            print(sql)
            val = (self.lineEdit_Vorname.text()+" "+self.lineEdit_Nachname.text(),"nein" )
            print(val)
            db.insert(sql,  val)
            print("Unchecked")

            
#        db.insert(sql,  val)
#        self.twData_anzeigen()
