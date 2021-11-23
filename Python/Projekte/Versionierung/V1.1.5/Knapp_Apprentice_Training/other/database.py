import mysql.connector
import configparser
import os
import sqlite3
from sqlite3 import Error
class Database:
    
    #Private Variablen, welche für die DB Connection benötigt werden!
    __benutzername = ""
    __passwort = ""
    __host = ""
    __databasename = "kat"
    __instance = None
    permission = ""
    
    @staticmethod
    def get_instance(parent):
        if Database.__instance == None:
            Database(parent)
        return Database.__instance
    
    def __init__(self,  parent):
        if Database.__instance != None:
            raise Exception ("This class is a Singleton!")
        else:
            config = configparser.ConfigParser()
            config.sections()
            test=config.read('config.ini')
            print(test)
            print(config['DATABASE']['host'])
            #Benutzername und Passwort für die Wiederverwendung in eine Globale Variable schreiben.
            Database.__benutzername = parent.benutzername
            Database.__passwort = parent.passwort
            Database.__instance = self
            Database.__host=config['DATABASE']['host']
        self.toSQLite()   
    #Funktion um den Login zu prüfen und die Gruppe/Rechte des Users abzuspeichern
    def login_connect(self):
        
        try:
            
            self.con = mysql.connector.connect(user=Database.__benutzername, password=Database.__passwort,
                        host=Database.__host,
                        database='')
            
            self.cursor = self.con.cursor()

            #Zum rechte der User abfragen:
            #Gruppe/Rechte des Users auslesen und für die Verwendung anderer Klassen in eine Globale Variable schreiben.
            #self.cursor.execute("SELECT usergroup FROM pma__users WHERE username='" + Database.__benutzername +'"')
            #for z in self.cursor:
                #Database.__permission =   z[0].decode("utf-8") 
            
            self.cursor.close()
            self.con.close()
            
        except mysql.connector.Error as err:
            Database.__instance = None
            return err.errno
    
    #Funktion um eine Verbindung zur DB herzustellen.
    def connect(self):
        
        try:
            self.con = mysql.connector.connect(user=Database.__benutzername, password=Database.__passwort,
                        host=Database.__host,
                        database=Database.__databasename)
            
        except mysql.connector.Error as err:
            return err.errno
            
        self.cursor = self.con.cursor()
        
        
    def insert (self, sql, val):
        
        error = self.connect()
        if error != None:
            return "backtologin"
            
        try:
            self.cursor.execute(sql, val)
            self.con.commit()
            
        except mysql.connector.Error as err:
            return err.errno
        
        self.cursor.close()
        self.con.close()

    def select(self, sql):
        
        error = self.connect()
        if error != None:
            return "backtologin"
        
        try:
            self.cursor.execute(sql)
            return self.cursor
            
        except mysql.connector.Error as err:
            print ("error")
            return err.errno
            
        self.cursor.close()
        self.con.close()
    
    def delete(self, sql):
        
        error = self.connect()
        if error != None:
            return "backtologin"
        
        try:
            self.cursor.execute(sql)
            self.con.commit()
            
        except mysql.connector.Error as err:
            return err.errno
            
        self.cursor.close()
        self.con.close()
        
    def toSQLite(self):
            print(os.listdir('.//'))
            if 'kat.db'not in os.listdir('.//'):
                command = 'mysql2sqlite -f "kat.db" -d "' + self.__databasename +'" -u "' + self.__benutzername +'" -p "' + self.__passwort +'" -h "' + self.__host +'"'
                print(command)
                os.popen(command)    
    
    def writeSQLite(self, table,  condition=""):
        if condition != "":
            condition = " WHERE " + condition

        try:
            conn = sqlite3.connect("kat.db")
            print(sqlite3.version)
            
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM " + table)
            conn.commit()
            
            sqlcursor = self.select("SELECT * FROM " + table + condition)
            rows = sqlcursor.fetchall()
            print(rows)
            
            sqlcursor = self.select("SHOW columns FROM " + table)
            columns = sqlcursor.fetchall()
            print(columns)
            columnCount = len(columns)
            #Anpassung
            values = "values ("
            for x in range(0, columnCount):
                values += "?"
                if x != columnCount - 1:
                    values += ","
                    
            values += ")"
            
            print(values)
            sqliteCommand = "insert into " + table + " " + values
            print(sqliteCommand)
            cursor.executemany(sqliteCommand,  rows)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
                
    @staticmethod
    def log_out():
        Database.__instance = None