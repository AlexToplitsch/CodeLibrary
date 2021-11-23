from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QApplication, QMessageBox
from other.database import Database
from sub.mainwindow.mainwindow import gui_mainwindow
from sub.login.login_settings import LoginSettings
import sys
from configparser import ConfigParser

from sub.login.Ui_login import Ui_Login
 
class Login(QDialog, Ui_Login):

    def __init__(self, parent=None):


        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.create_config()
        self.INFO("Melde dich an",  "I")# info asugabe 

    def create_config(self):
        #Versucht hier eine Konfig-Datei zu öffnen
        try:


            with open("config.ini") as f:
                print("Open  ")
                
            f.close()
        #Wenn die Konfigurationsdatei nicht verfügbar ist, wird eine erstellt
        except:
            config_object = ConfigParser()

            #Angenommen, wir benötigen zwei Abschnitte in der Konfigurationsdatei. Nennen wir sie USERINFO und SERVERCONFIG
            config_object["DATABASE"] = {
                "host": "127.0.0.1",
                "database": "kat",
            }

            #Schreiben Sie die obigen Abschnitte in die Datei config.ini
            with open('config.ini', 'w') as conf:
                config_object.write(conf)
                
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
    def on_toolButton_einstellungen_clicked(self):
        #Button zum Öffnen der Einstellungen
        w = LoginSettings(self)
        w.show()#Öffnen das SettingGui
        self.hide()#hide the current window
        
    @pyqtSlot()
    def on_pushButton_anmelden_clicked(self):
        self.benutzername = self.lineEdit_benutzername.text()
        self.passwort = self.lineEdit_passwort.text()
        
        
        db = Database.get_instance(self)#verbindung zur Datenbank
        error = db.login_connect()
        
        if error == None:
            #wenn es keine Fehler gibt:
            w = gui_mainwindow(self)
            w.show()
            self.hide()
        else:
            #wenn es einen Fehler gibt
            print(error)
            print("Konnte keine Verbindung zur Datenbank herstellen!")
            self.INFO("Konnte keine Verbindung zur Datenbank herstellen!",  "F")# info asugabe             
            #Ausgabe einer Messagebox
            messageBox = QMessageBox(self)
            messageBox.setWindowTitle("Fehler")
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setText("Es konnte keine Verbindung zur Datenbank hergestellt werden!")
            messageBox.addButton("Okay", QMessageBox.NoRole) 
            messageBox.exec_()
        
        



app = QApplication(sys.argv)
ui = Login() #Name that was used when creating the dialog class
ui.show()
sys.exit(app.exec_())
