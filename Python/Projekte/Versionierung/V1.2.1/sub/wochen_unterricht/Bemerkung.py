# -*- coding: utf-8 -*-

"""
Module implementing Bemerkung.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from other.database import Database


from sub.wochen_unterricht.Ui_Bemerkung import Ui_Dialog


class Bemerkung(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Bemerkung, self).__init__(parent)
        self.setupUi(self)
        
        
        
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
    
    @pyqtSlot()
    def on_pushButton_Speichern_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Gruppen_Speichern()

    
    
    def Gruppen_Speichern(self):
        #self.Ermittelung_der_Nummer_Des_Tages()
        db = Database.get_instance(self)
        sql = "select * from kat_wochen_unterricht_fussbemerkungen WHERE Woche = '" + self.KW_l.text()+ "'"
        mycursor = db.select(sql)
        if mycursor == "backtologin":
            self.back_to_login()
            return        
        sql_satz = []
        sql_satz = mycursor.fetchall()
        satz_len = len(sql_satz)
        print("vor if")
        #vorschau= self.te_vorschau.item(0, 0).text()+"\n "+self.te_vorschau.item(1, 0).text()+"\n "+ self.te_vorschau.item(2, 0).text()+"\n "+self.te_vorschau.item(3, 0).text()+"\n "+self.te_vorschau.item(4, 0).text()
        if satz_len == 0:
            print("im if 1")
                #+self.Wochen_Tag.text()+") \
            sql = "INSERT INTO kat_wochen_unterricht_fussbemerkungen (Woche, 1A, 1B, 2A, 2B, 3A, 3B,4A,4B,Homeoffice,BS)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val =(self.parent().label_jahr.text()+self.parent().te_KW.text(),self.lineEdit_1A.text(),self.lineEdit_1B.text(),self.lineEdit_2A.text(),self.lineEdit_2B.text(),self.lineEdit_3A.text(),self.lineEdit_3B.text(),self.lineEdit_4A.text(),self.lineEdit_4B.text(), self.lineEdit_Homeoffice.text(), self.lineEdit_BS.text())
            db.insert(sql,  val)
            print("im if 2")

        else:
            print("im else")
            sql = "UPDATE kat_wochen_unterricht_fussbemerkungen set 1A=%s, 1B=%s, 2A=%s, 2B=%s,3A=%s,3B=%s,4A=%s,4B=%s,Homeoffice=%s,BS=%s,Benutzer=%s,Aenderung=%s WHERE Woche = '" + self.KW_l.text() + "'"
            val = (self.lineEdit_1A.text(),self.lineEdit_1B.text(),self.lineEdit_2A.text(),self.lineEdit_2B.text(),self.lineEdit_3A.text(),self.lineEdit_3B.text(),self.lineEdit_4A.text(),self.lineEdit_4B.text(), self.lineEdit_Homeoffice.text(), self.lineEdit_BS.text(),"root","2020-12-14 09:05:42")
            db.insert(sql,  val)
    
    
  
    @pyqtSlot()
    def on_pushButton_generieren_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.Gruppen_Generieren_1A()
        self.Gruppen_Generieren_2A()
        self.Gruppen_Generieren_3A()
        self.Gruppen_Generieren_4A()
        self.Gruppen_Generieren_1B()
        self.Gruppen_Generieren_2B()
        self.Gruppen_Generieren_3B()
        self.Gruppen_Generieren_4B()
        #self.BS_Anwesenheit_Generieren()


    def BS_Anwesenheit_Generieren(self):
        anfang_der_Woche=self.parent().tableWidget_Wochen_Plan.horizontalHeaderItem(0).text()
        datum1, datum=anfang_der_Woche.split(" ")
        
        jahr, monat,  tag = datum.split(".")
        
        datum= tag+"."+monat+"."+jahr
        print(datum)
        self.lineEdit_BS.setText("")

        
        db = Database.get_instance(self)
      #  sql = "SELECT * FROM kat_wochen_unterricht WHERE Woche='" + self.label_jahr.text()+self.te_KW.text() +"' and Tag='" + str(spalte) + "' and Zeile='" + w.Row.text() + "'" # sql-Befehl
        select_= "SELECT PERS_NR FROM kat_berufsschulzeit WHERE VonDatum<='"+datum+"' and Bisdatum >='"+datum+"'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
        #print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        
        if satz_len != 0:
            for i in range(satz_len):
                if self.lineEdit_BS.text()=="":
                    self.lineEdit_BS.setText(self.lineEdit_BS.text()+str(inhalt[i][0])+"."+str(inhalt[i][1]))
                else:
                    self.lineEdit_BS.setText(self.lineEdit_BS.text()+", "+str(inhalt[i][0])+"."+str(inhalt[i][1]))



    def Gruppen_Generieren_1A(self):
        
        self.lineEdit_1A.setText("")

        
        db = Database.get_instance(self)
      #  sql = "SELECT * FROM kat_wochen_unterricht WHERE Woche='" + self.label_jahr.text()+self.te_KW.text() +"' and Tag='" + str(spalte) + "' and Zeile='" + w.Row.text() + "'" # sql-Befehl
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='1A'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
        print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        
        if satz_len != 0:

            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]
                if self.lineEdit_1A.text()=="":
                    self.lineEdit_1A.setText(self.lineEdit_1A.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_1A.setText(self.lineEdit_1A.text()+", "+str(inhalt[i][1])+"."+vorname)
    
    def Gruppen_Generieren_1B(self):
        self.lineEdit_1B.setText("")
  
        
        db = Database.get_instance(self)
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='1B'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
#        print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        if satz_len != 0:
            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]                
                if self.lineEdit_1B.text()=="":
                    self.lineEdit_1B.setText(self.lineEdit_1B.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_1B.setText(self.lineEdit_1B.text()+", "+str(inhalt[i][1])+"."+vorname)

    def Gruppen_Generieren_2A(self):
        self.lineEdit_2A.setText("")
      
        
        db = Database.get_instance(self)
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='2A'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
     #   print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        if satz_len != 0:
            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]                      
                if self.lineEdit_2A.text()=="":
                    self.lineEdit_2A.setText(self.lineEdit_2A.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_2A.setText(self.lineEdit_2A.text()+", "+str(inhalt[i][1])+"."+vorname)

    def Gruppen_Generieren_2B(self):
        self.lineEdit_2B.setText("")
      
        
        
        db = Database.get_instance(self)
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='2B'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
    #    print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        if satz_len != 0:
            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]                      
                if self.lineEdit_2B.text()=="":
                    self.lineEdit_2B.setText(self.lineEdit_2B.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_2B.setText(self.lineEdit_2B.text()+", "+str(inhalt[i][1])+"."+vorname)

    def Gruppen_Generieren_3A(self):
        self.lineEdit_3A.setText("")
      
        db = Database.get_instance(self)
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='3A'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
  #      print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        if satz_len != 0:
            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]    
                if self.lineEdit_3A.text()=="":
                    self.lineEdit_3A.setText(self.lineEdit_3A.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_3A.setText(self.lineEdit_3A.text()+", "+str(inhalt[i][1])+"."+vorname)                    
    
    def Gruppen_Generieren_3B(self):
        self.lineEdit_3B.setText("")
         
        
        db = Database.get_instance(self)
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='3B'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
  #      print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        if satz_len != 0:
            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]   
                if self.lineEdit_3B.text()=="":
                    self.lineEdit_3B.setText(self.lineEdit_3B.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_3B.setText(self.lineEdit_3B.text()+", "+str(inhalt[i][1])+"."+vorname)
    def Gruppen_Generieren_4A(self):
        self.lineEdit_4A.setText("")
    
        db = Database.get_instance(self)
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='4A'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
 #       print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        if satz_len != 0:
            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]   
                if self.lineEdit_4A.text()=="":
                    self.lineEdit_4A.setText(self.lineEdit_4A.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_4A.setText(self.lineEdit_4A.text()+", "+str(inhalt[i][1])+"."+vorname)
    def Gruppen_Generieren_4B(self):
        self.lineEdit_4B.setText("")               
        db = Database.get_instance(self)
        select_= "SELECT Vorname, Nachname FROM kat_lehrlinge WHERE Gruppe='4B'"
        mycursor = db.select(select_)
        inhalt=[]
        inhalt = mycursor.fetchall()
  #      print("-----"+str(inhalt[0][0]))
        satz_len = len(inhalt)
        if satz_len != 0:
            for i in range(satz_len):
                vorname_= str(inhalt[i][0])
                vorname= vorname_[0]  
                if self.lineEdit_4B.text()=="":
                    self.lineEdit_4B.setText(self.lineEdit_4B.text()+str(inhalt[i][1])+"."+vorname)
                else:
                    self.lineEdit_4B.setText(self.lineEdit_4B.text()+", "+str(inhalt[i][1])+"."+vorname)                    
                    



