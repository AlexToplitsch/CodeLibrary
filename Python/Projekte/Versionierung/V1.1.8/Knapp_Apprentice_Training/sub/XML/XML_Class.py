#import mysql.connector
from other.database import Database
from xml.dom.minidom import *
from xml.etree.ElementTree import Element, SubElement
import xml.etree.ElementTree as ET

class DBtoXML:
    
    def MakeXML(db, table):
        records="SELECT * FROM " + table
        rows = db.select(records).fetchall()
        
        columns="SHOW columns FROM " + table
        
        
        #cursor.execute("SHOW columns FROM " + table)
        listOfNames = [column[0] for column in db.select(columns).fetchall()]
        tree = ET.ElementTree("tree")
        top = Element('root')
        for row in rows:
            list = []
            record = SubElement(top,'Record')
            #Elemente für Record erstellen
            
            for x in range(0, len(listOfNames)):
                list.append(SubElement(record, listOfNames[x]))
                list[x].text = str(row[x])
                #list[x] = SubElement(record, listOfNames[x])
            #Text bzw. Value für die Elemente definieren

        tree._setroot(top)
        tree.write("XMLFiles/" + table + ".xml",  encoding= "UTF-8",  xml_declaration=True)
        #Umwandlung in korrekt formatierten Text
        """rough_string = ElementTree.tostring(top, encoding='utf-8',method='xml')
        pretty_string = parseString(rough_string)
        print(pretty_string.toprettyxml(indent="  "))
        #Als Datei schreiben
        xmlfile = open("XMLFiles/" + table + ".xml", "w")
        xmlfile.write(pretty_string.toprettyxml(" "))
        xmlfile.close()"""
