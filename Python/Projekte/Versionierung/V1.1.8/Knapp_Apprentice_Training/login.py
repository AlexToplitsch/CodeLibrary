from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QApplication, QMessageBox
from other.database import Database
from sub.mainwindow.mainwindow import gui_mainwindow
from sub.login.login_settings import LoginSettings
from users import Users
import sys
from configparser import ConfigParser
import bcrypt
from mysql.connector.locales.eng import client_error
from sub.login.Ui_login import Ui_Login
 
class Login(QDialog, Ui_Login):

    def __init__(self, parent=None):


        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.create_config()
        self.INFO("Melde dich an",  "I")# info asugabe 
        self.lineEdit_benutzername.setText("passwort2")
        self.lineEdit_passwort.setText("passwort2")
    def create_config(self):
        #Versucht hier eine Konfig-Datei zu öffnen
        try:


            with open("config.ini") as f:
                print("Open " + f)
                
            f.close()
        #Wenn die Konfigurationsdatei nicht verfügbar ist, wird eine erstellt
        except:
            config_object = ConfigParser()

            #Angenommen, wir benötigen zwei Abschnitte in der Konfigurationsdatei. Nennen wir sie USERINFO und SERVERCONFIG
            config_object["DATABASE"] = {
                "host": "10.33.35.171",
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
        #self.hide()#hide the current window
        self.setWindowOpacity(0.0)
    @pyqtSlot()
    def on_toolButton_nutzerverwaltung_clicked(self):
        #Button zum Öffnen der Einstellungen
        w = Users(self)
        w.show()#Öffnen das SettingGui
        #self.hide()#hide the current window
        self.setWindowOpacity(0.0)
        
    @pyqtSlot()
    def on_pushButton_anmelden_clicked(self):
        self.benutzername = self.lineEdit_benutzername.text()
        self.passwort = self.lineEdit_passwort.text()
        
        
        db = Database.get_instance(self)#verbindung zur Datenbank
        error = db.login_connect()
        
        if error == None:
            
            sql ="select * from kat_nutzer WHERE Benutzername = '" + self.benutzername + "'"
            #print("SQL Befehl")
            mycursor = db.select(sql)
            #print("mycursor set")
            #print(mycursor.statement)
            
            
            mycursor.execute(sql)
            #print("executed")
            sql_satz = mycursor.fetchall()
            
            satz_len = len(sql_satz)
            if satz_len == 0:
                print("Nutzer gibt es nicht")
                return "404"
            #========COMPARISON==========================
            storedSalt = sql_satz[0][3]
            storedPassword = sql_satz[0][2]
            #print(sql_satz[0])
            #print(storedSalt)
            
            #print("STORED SALT " + storedSalt)
            #print("STORED PASSWORD "+storedPassword)
            
            key = bcrypt.hashpw(self.passwort.encode(), storedSalt.encode()) #hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 50000, dklen=32)  # It is recommended to use at least 100,000 iterations of SHA-256 

            #print(key)
            #print(storedPassword.encode())
            
            if key == storedPassword.encode():
                print('You have logged in successfully!')
                db.permission = sql_satz[0][4]
            else:
                print('Something went wrong')
                return "ERROR"
            #print(storedSalt)
            
            #wenn es keine Fehler gibt:
            w = gui_mainwindow(self)
            
            w.show()
            w.raise_()
            w.activateWindow()
            #self.hide()
            self.setWindowOpacity(0.0)

#            self.showMinimized()
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
