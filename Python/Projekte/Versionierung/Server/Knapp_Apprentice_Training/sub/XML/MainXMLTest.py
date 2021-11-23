from XML_Class import DBtoXML
import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='root',
    passwd='', db='test')
    
DBtoXML.MakeXML(list, conn, "tabelle")
