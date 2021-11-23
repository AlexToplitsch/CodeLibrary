# -*- coding: utf-8 -*-

"""
Module implementing Wochen_Unterricht.
"""
import datetime
from datetime import timedelta
from PyQt5.QtCore import pyqtSlot, QTime, Qt
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
#from hinzufuegen_Plan import hinzufügen
from sub.wochen_unterricht.hinzufuegen_Plan import hinzufügen
from sub.wochen_unterricht.Ui_Wochen_Unterricht import Ui_Wochen_unterricht
from sub.wochen_unterricht.Kopieren import Kopieren
from other.database import Database
from pyreportjasper import JasperPy
import time
import os


class Wochen_Unterricht(QDialog, Ui_Wochen_unterricht):
    """
    Class documentation goes here.
    """
    today = None
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Wochen_Unterricht, self).__init__(parent)
        self.setupUi(self)
        self.te_KW.setText(str(datetime.datetime.today().isocalendar()[1]))
        self.today = datetime.datetime.today()
       
        d1 = datetime.datetime.today().strftime("%Y")
        self.label_jahr.setText(d1+"-")
        self.twData_anzeigen()
    

    
    @pyqtSlot()
    def on_pushButton_hauptmenue_clicked(self):
        """
        Slot documentation goes here.
        """
        self.parent().setWindowOpacity(1.0)
        self.close()

    
    @pyqtSlot()
    def on_pushButton_excel_ausgabe_clicked(self):
        """
        Slot documentation goes here.
        """
        self.Leere_Tage_befuellen()
        self.on_pb_report_clicked()
        
        self.Leere_Tage()
        
        # TODO: not implemented yet
       # raise NotImplementedError

    
        
        
        
        
        
    
    
    @pyqtSlot(int, int)
    def on_tableWidget_Wochen_Plan_cellClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        db = Database.get_instance(self)
    
        w = hinzufügen(self)
        w.show()#Öffnen das SettingGui
        
        
        w.Row.setText(str(row+1))
        w.Wochen_Tag.setText("mo")
#        print(self.tableWidget_Wochen_Plan.horizontalHeaderItem(column).text())
        w.Wochen_Tag.setText(self.tableWidget_Wochen_Plan.horizontalHeaderItem(column).text())
        #grid=self.tableWidget_Wochen_Plan.item(row,  column)     

        if w.Wochen_Tag.text().find("Montag") != -1:
            spalte=1
        if w.Wochen_Tag.text().find("Dienstag") != -1: 
            spalte=2        
        if w.Wochen_Tag.text().find("Mittwoch") != -1: 
            spalte=3        
        if w.Wochen_Tag.text().find("Donnerstag") != -1: 
            spalte=4        
        if w.Wochen_Tag.text().find("Freitag") != -1: 
            spalte=5
    
        sql = "SELECT * FROM kat_wochen_unterricht WHERE Woche='" + self.label_jahr.text()+self.te_KW.text() +"' and Tag='" + str(spalte) + "' and Zeile='" + w.Row.text() + "'" # sql-Befehl
        mycursor = db.select(sql)
        inhalt = mycursor.fetchall()
        if inhalt == "backtologin":
            self.back_to_login()
            return
            
        for a in inhalt : 
#            print(str(a[1])+" "+str(a[2])+""+str(a[3])+" "+str(a[4])+" "+str(a[5])+" "+str(a[6])+" "+str(a[7])+" "+str(a[8])+" "+str(a[9])+" "+str(a[10])+" "+str(a[11])+" "+str(a[12]))
#            try:
            fielditem = QTableWidgetItem(a[3])
            w.te_vorschau.setItem(2, 0, fielditem)
                        
            fielditem = QTableWidgetItem(a[7])
            w.te_vorschau.setItem(3, 0, fielditem)

            fielditem = QTableWidgetItem(a[6])
            w.te_vorschau.setItem(1, 0, fielditem)

            fielditem = QTableWidgetItem(a[4] + " " + a[5])
            w.te_vorschau.setItem(0, 0, fielditem)
            
            von, bis= str(a[3]).split("-")
            von_h, von_m= von.split(":")
            bis_h, bis_m= bis.split(":")
            
            w.timeEdit_von.setTime(QTime(int(von_h), int(von_m)))
            w.timeEdit_bis.setTime(QTime(int(bis_h), int(bis_m)))
           # w.timeEdit_von.setTime(von)
            #w.timeEdit_bis.setTime(bis)
            

#            a = 'pw try oks Key 1.0.0 (120) tst kw'
#            b = a[a.find('Key'):a.find(')')+1]
#            print (b)
    
            index = w.comboBox_Unterrichtsthema.findText(str(a[4]))
            w.comboBox_Unterrichtsthema.setCurrentIndex(index)

            index = w.comboBox_Ausbilder.findText(str(a[5]))
            w.comboBox_Ausbilder.setCurrentIndex(index)

            index = w.comboBox_Raum.findText(str(a[6]))
            w.comboBox_Raum.setCurrentIndex(index)
            
            index = w.comboBox_Thema1.findText(str(a[10]))
            w.comboBox_Thema1.setCurrentIndex(index)

            index = w.comboBox_Thema2.findText(str(a[11]))
            w.comboBox_Thema2.setCurrentIndex(index)

            index = w.comboBox_Thema3.findText(str(a[12]))
            w.comboBox_Thema3.setCurrentIndex(index)
            
            

        self.setWindowOpacity(0.0)#hide the current window
    


            
    @pyqtSlot()
    def on_pushButton_befor_KW_clicked(self):
        """
        Slot documentation goes here.
        """
        kw = int(self.te_KW.text())
        before = kw -1
        self.te_KW.setText(str(before))
        self.kontrolle_der_Woche()
        self.twData_anzeigen()
        self.today -= timedelta(7)     # self.kalenderwoche(name, next)
        print("Today: " + str(self.today))       # self.getDateRangeFromWeek(int(name),int(self.te_KW.text()) )
        self.week_range(self.today)


    @pyqtSlot()
    def on_pushButton_next_KW_clicked(self):
        """
        Slot documentation goes here.
        """
        
        kw = int(self.te_KW.text())
        next = kw +1
        self.te_KW.setText(str(next))
        self.kontrolle_der_Woche()
        self.twData_anzeigen()
        self.today += timedelta(7)     # self.kalenderwoche(name, next)
        print("Today: " + str(self.today))
        #self.getDateRangeFromWeek(int(name),int(self.te_KW.text()) )
        self.week_range(self.today)

    
    @pyqtSlot()
    def on_pushButton_copy_clicked(self):
        """
        Slot documentation goes here.
        """
        
        w = Kopieren(self)
        w.show()#Öffnen das SettingGui
        self.setWindowOpacity(0.0)#hide the current window
        
        
    def closeEvent(self, event):
        self.parent().setWindowOpacity(1.0)
        self.close()  
    def on_pb_report_clicked(self):
        try:
            db=Database.get_instance(self)
            db.writeSQLite("kat_wochen_unterricht", "Woche='"+self.label_jahr.text()+self.te_KW.text()+"'")
            input_file='Reports/kat_wochen_unterricht.jasper'
            output='Reports/kat_wochen_unterricht'
            jasper = JasperPy()
            con={
            'driver':'generic', 
            'jdbc_driver':'org.sqlite.JDBC', 
            'jdbc_url':'jdbc:sqlite:kat.db'
            }
            jasper.process(input_file, output_file=output, db_connection=con, format_list=["pdf"])
            
            self.setCursor(Qt.WaitCursor)
            time.sleep(2)
            self.setCursor(Qt.ArrowCursor)
            
            os.startfile("Reports\kat_wochen_unterricht.pdf")
            
        except Exception:
            print("Fehler")
            
            
    def getDateRangeFromWeek(self, p_year,p_week):

 

        Montag = datetime.datetime.strptime(f'1.W{int(p_week )}.{p_year}', "%w.W%W.%Y").date()
        Dienstag = datetime.datetime.strptime(f'2.W{int(p_week )}.{p_year}', "%w.W%W.%Y").date()
        Mittwoch = datetime.datetime.strptime(f'3.W{int(p_week )}.{p_year}', "%w.W%W.%Y").date()
        Donnerstag = datetime.datetime.strptime(f'4.W{int(p_week )}.{p_year}', "%w.W%W.%Y").date()
        Freitag = datetime.datetime.strptime(f'5.W{int(p_week )}.{p_year}', "%w.W%W.%Y").date()
        print( str(Montag)+"    "+ str(Dienstag)+"    "+ str(Mittwoch)+"    "+ str(Donnerstag)+"    "+ str(Freitag))
        colname = QTableWidgetItem("Montag "+ str(Montag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(0, colname)
        
        colname = QTableWidgetItem("Dienstag "+ str(Dienstag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(1, colname)        
        colname = QTableWidgetItem("Mittwoch "+ str(Mittwoch))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Donnerstag "+ str(Donnerstag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Freitag "+ str(Freitag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(4, colname)      

    def week_range(self, date):
        # isocalendar calculates the year, week of the year, and day of the week.
        # dow is Mon = 1, Sat = 6, Sun = 7
        year, week, dow = date.isocalendar()
        
        # Find the first day of the week.
        if dow == 1:
            # Since we want to start with Sunday, let's test for that condition.
            Montag = date
        else:
            # Otherwise, subtract `dow` number days to get the first day
            Montag = date - timedelta(dow - 1) 

     

        # Now, add 6 for the last day of the week (i.e., count up to Saturday)
        #end_date = Montag + timedelta(6)
        
        Dienstag= Montag + timedelta(1)
        Mittwoch= Montag + timedelta(2)
        Donnerstag= Montag + timedelta(3)
        Freitag= Montag + timedelta(4)
        
        Montag = Montag.strftime("%Y.%m.%d")
        Dienstag = Dienstag.strftime("%Y.%m.%d")
        Mittwoch = Mittwoch.strftime("%Y.%m.%d")
        Donnerstag = Donnerstag.strftime("%Y.%m.%d")
        Freitag = Freitag.strftime("%Y.%m.%d")
        
        colname = QTableWidgetItem("Montag "+ str(Montag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Dienstag "+ str(Dienstag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(1, colname)        
        colname = QTableWidgetItem("Mittwoch "+ str(Mittwoch))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Donnerstag "+ str(Donnerstag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Freitag "+ str(Freitag))
        self.tableWidget_Wochen_Plan.setHorizontalHeaderItem(4, colname)      


#Call function to get dates range 
    def twData_anzeigen(self):
        """
        Anzeige der Daten aus der Datenbank im Programm.
        """

        #print (datetime.date(2021, 2, 3).isoweekday())
#        print (datetime.date.isocalendar(self.te_KW.text()).date()[1])
        self.tableWidget_Wochen_Plan.clear()
        db = Database.get_instance(self)
        self.tableWidget_Wochen_Plan.setColumnCount(5)
       # self.getDateRangeFromWeek(int(name),int(self.te_KW.text()) )
        self.week_range(self.today)#getDateRangeFromWeek('2019','1')

        
        self.tableWidget_Wochen_Plan.setRowCount(1)
        
        #mycursor = mydb.cursor()
        #mycursor = mydb.cursor()
        mycursor = db.select("SELECT * FROM kat_wochen_unterricht where Woche='"+self.label_jahr.text()+self.te_KW.text()+"'" )# sql befehl auf die ganze "adressenverwaltung" tabelle 
        self.tableWidget_Wochen_Plan.setRowCount(20) #konstante Anzahl von Zeilen in Tabelle
        for z in mycursor : 
            for s in range(0, 14): #Anzahl der Felder=Spalten
                fielditem = QTableWidgetItem(str(z[4])+" "+str(z[5])+"\n"+str(z[6])+"\n"+str(z[3])+"\n"+str(z[7])+"\n"+str(z[8]))
                fielditem.setTextAlignment(4)
                line = int(z[2]) -1
                if s == 1:
                    if str(z[s]) == "1": #Monatg
                        self.tableWidget_Wochen_Plan.setItem(line, 0,  fielditem)
                if s == 1:
                    if str(z[s]) == "2": #Dienstag
                        self.tableWidget_Wochen_Plan.setItem(line,  1,  fielditem)
                if s == 1:
                    if str(z[s]) == "3": #Mittwoch
                        self.tableWidget_Wochen_Plan.setItem(line,  2,  fielditem)
                if s == 1:
                    if str(z[s]) == "4": #Donnerstag
                        self.tableWidget_Wochen_Plan.setItem(line,  3,  fielditem)
                if s == 1:
                    if str(z[s]) == "5": #Freitag
                        self.tableWidget_Wochen_Plan.setItem(line,  4,  fielditem)
#       
        mycursor.close()#cursor wird geschlossen
        self.tableWidget_Wochen_Plan.resizeColumnsToContents()
        self.tableWidget_Wochen_Plan.resizeRowsToContents()       
        header_h= self.tableWidget_Wochen_Plan.horizontalHeader()
        header_v= self.tableWidget_Wochen_Plan.verticalHeader()
        for i in range(20):
            header_h.resizeSection(i, 240)
            header_v.resizeSection(i, 150)       
            self.tableWidget_Wochen_Plan.setColumnWidth(100000, 100000)
           

    
    def kontrolle_der_Woche(self):
        if self.te_KW.text() == "0" :
            self.te_KW.setText("53")
            buggy_name = self.label_jahr.text()
            name = buggy_name[:-1]
            ergebnis= int(name) -1
            self.label_jahr.setText(str(ergebnis)+"-")
            
        if self.te_KW.text() =="54":
            self.te_KW.setText("1")
            buggy_name = self.label_jahr.text()
            name = buggy_name[:-1]
            ergebnis= int(name) +1
            self.label_jahr.setText(str(ergebnis)+"-")
        
    
    
    def Leere_Tage(self):
        #pass
        db = Database.get_instance(self)

        for i in range(1, 5):

            print("")
#            
            print("Spalte: "+str(i))
            sql = "select * from kat_wochen_unterricht WHERE Woche = '" + self.label_jahr.text()+self.te_KW.text() + "' and Tag='"+str(i)+"' and Unterrichtsthema=' '"
            mycursor = db.select(sql)

            
            sql_satz = []
            sql_satz = mycursor.fetchall()
            satz_len = len(sql_satz)
            #vorschau= self.te_vorschau.item(0, 0).text()+"\n "+self.te_vorschau.item(1, 0).text()+"\n "+ self.te_vorschau.item(2, 0).text()+"\n "+self.te_vorschau.item(3, 0).text()+"\n "+self.te_vorschau.item(4, 0).text()
            

            if satz_len != 0:
                sql = "Delete from kat_wochen_unterricht WHERE Woche= '" + self.label_jahr.text()+self.te_KW.text() + "' and Tag='"+str(i)+"' and Unterrichtsthema=' '"
                db.delete(sql)
            
        
            #mycursor.close()
    

    def Leere_Tage_befuellen(self):
        db = Database.get_instance(self)
        #i=1
        for i in range(1, 6):
            print(i)
        
        
            
            print("Spalte: "+str(i))
            sql = "select * from kat_wochen_unterricht WHERE Woche = '" + self.label_jahr.text()+self.te_KW.text() + "' and Tag='"+str(i)+"'"
            mycursor = db.select(sql)

            
            sql_satz = []
            sql_satz = mycursor.fetchall()
            satz_len = len(sql_satz)
            #vorschau= self.te_vorschau.item(0, 0).text()+"\n "+self.te_vorschau.item(1, 0).text()+"\n "+ self.te_vorschau.item(2, 0).text()+"\n "+self.te_vorschau.item(3, 0).text()+"\n "+self.te_vorschau.item(4, 0).text()
            print("--------"+str(satz_len)+"-------------")
            

            if satz_len == 0:
                leer=" "
                row=1
                    #+self.Wochen_Tag.text()+") \
                sql = "INSERT INTO kat_wochen_unterricht (Woche, Tag, Zeile, Unterrichtsthema)  VALUES (%s,%s,%s,%s)"
                val =(self.label_jahr.text()+self.te_KW.text(),i,row, leer)
                print("wurde insertet___________________________________________")
                db.insert(sql,  val)
           # self.INFO("Eintrag wurde in die Datenbank gespeichert!",  "I")# info asugab
    def keyPressEvent(self, event):
            if event.key() == Qt.Key_Escape:
                self.parent().setWindowOpacity(1.0)
                self.close()
