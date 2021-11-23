from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QDialog,  QTableWidgetItem,  QTableWidget, QHeaderView,  QAbstractItemView
from datetime import date
from dateutil.relativedelta import relativedelta

from other.database import Database

from sub.apprentice.Ui_apprentice_list import Ui_ApprenticeList

from sub.apprentice.apprentice_add import GuiApprenticeAdd
from sub.apprentice.apprentice_manager import GuiApprenticeManager



class GuiApprenticeList(QDialog, Ui_ApprenticeList):
    
    def __init__(self, parent):
        
        super(GuiApprenticeList, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.frameGeometry().width(), self.frameGeometry().height())
        self.db_auslesen()
    
    def db_auslesen(self):
        
        #Tabelle leeren
        self.tableWidget_lehrlinge_liste.clear()
        
        #Tabellen Überschriften Hinzufügen!
        self.tableWidget_lehrlinge_liste.setColumnCount(5)
        colname = QTableWidgetItem("Personalnummer")
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(0, colname)
        colname = QTableWidgetItem("Vorname")
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(1, colname)
        colname = QTableWidgetItem("Nachname")
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(2, colname)
        colname = QTableWidgetItem("Lehrberuf")
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(3, colname)
        colname = QTableWidgetItem("Lehrjahr")
        
        #Tabelle Designen!
        self.tableWidget_lehrlinge_liste.setHorizontalHeaderItem(4, colname)
        self.tableWidget_lehrlinge_liste.verticalHeader().setVisible(False)
        self.tableWidget_lehrlinge_liste.setShowGrid(False)
        self.tableWidget_lehrlinge_liste.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_lehrlinge_liste.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_lehrlinge_liste.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_lehrlinge_liste.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget_lehrlinge_liste.horizontalHeader().setHighlightSections(False)

        
        #Datenbank Klasse aufrufen
        db = Database.get_instance(self)
        
        #Suchfilter
        filter = self.comboBox_suchfilter.currentText()
        suche = self.lineEdit_suchen.text()
        
        if  suche == "":
            sql = "SELECT Personalnummer,Vorname,Nachname,Lehrberuf,Lehrbeginn FROM kat_lehrlinge"
            cursor = db.select(sql)
            
        elif filter == "Lehrjahr":
            
            today = date.today()
            diffdate1 = date.today() - relativedelta(years=int(suche))
            diffdate2 = date.today() - relativedelta(years=int(suche)-1)

            sql = "SELECT Personalnummer,Vorname,Nachname,Lehrberuf,Lehrbeginn FROM kat_lehrlinge WHERE lehrbeginn >= '"+ str(diffdate1) +"' and lehrbeginn <='"+ str(diffdate2) +"'"
            cursor = db.select(sql)
            
        else:
            
            sql = "SELECT (Personalnummer,Vorname,Nachname,Lehrberuf,Lehrbeginn) FROM kat_lehrlinge WHERE "+ filter +" LIKE '%"+ str(suche) +"%'"
            cursor = db.select(sql)
            
        if cursor == "backtologin":
                self.back_to_login()
                return
        
        #Werte aus der DB holen und richtig formatiert in Variablen speichern
        zeile=0;
        for z in cursor: #Zeile für Zeile auslesen und ausgeben
            
            #Lehrjahr filter
            y, m, d = str(z[4])[0:4], str(z[4])[5:7], str(z[4])[8:10]
            today = date.today()
            ty, tm, td = str(today)[0:4], str(today)[5:7], str(today)[8:10]
            
            if ty > y:
                lj = int(ty) - int(y)
                if tm > m and td > d:
                    lj = int(ty) - int(y) + 1
            else:
                lj = 1
            
            #Werte in Variablen speichern
            personalnummer = QTableWidgetItem(str(z[0]))
            personalnummer.setTextAlignment(Qt.AlignHCenter)
            vorname = QTableWidgetItem(str(z[1]))
            vorname.setTextAlignment(Qt.AlignHCenter)
            nachname = QTableWidgetItem(str(z[2]))
            nachname.setTextAlignment(Qt.AlignHCenter)
            lehrjahr = QTableWidgetItem(str(lj))
            lehrjahr.setTextAlignment(Qt.AlignHCenter)
            lehrberuf = QTableWidgetItem(str(z[3]))
            lehrberuf.setTextAlignment(Qt.AlignHCenter)
            
            #Zeile Counter
            self.tableWidget_lehrlinge_liste.setRowCount(zeile+1)
            
            #Werte in die Tabellen Zeilen 
            self.tableWidget_lehrlinge_liste.setItem(zeile, 0 , personalnummer)
            self.tableWidget_lehrlinge_liste.setItem(zeile, 1 , vorname)
            self.tableWidget_lehrlinge_liste.setItem(zeile, 2 , nachname)
            self.tableWidget_lehrlinge_liste.setItem(zeile, 3, lehrberuf)
            self.tableWidget_lehrlinge_liste.setItem(zeile, 4 , lehrjahr)
            
            zeile+=1
        
        #Zeilenanzahl ausgeben
        self.label_anzahl_lehrlinge.setText(str(zeile))
        
    @pyqtSlot(int, int)
    def on_tableWidget_lehrlinge_liste_cellClicked(self, row, column):
        
        #Button "Lehrling öffnen" altiviern
        self.pushButton_lehrling_oeffnen.setEnabled(True)
        
        #Personalnummer des ausgewählten für die weiterverwendung in anderen Klassen in einer globalen variable speichern
        self.personalnummerweitergabe = self.tableWidget_lehrlinge_liste.item(row, 0).text()
    
    def on_pushButton_aktualisieren_clicked(self):
        self.db_auslesen()
    
    @pyqtSlot()
    def on_pushButton_lehrling_hinzufuegen_clicked(self):
        w = GuiApprenticeAdd(self)
        w.show()
        self.hide()
        
    @pyqtSlot()
    
    def on_pushButton_hauptmenue_clicked(self):
        self.parent().setWindowOpacity(1.0)
        self.close()
        
    def closeEvent(self, event):
    
    #self.parent().show()
        self.parent().setWindowOpacity(1.0)
        self.close()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.parent().setWindowOpacity(1.0)
            self.close()
    
    @pyqtSlot()
    def on_pushButton_lehrling_oeffnen_clicked(self):
        w = GuiApprenticeManager(self)
        w.show()
        self.hide()
        
    def back_to_login(self):
        self.parent().back_to_login()
        self.close()
