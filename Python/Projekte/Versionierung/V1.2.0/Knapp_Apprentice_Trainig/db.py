import os
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")

#Get the USERINFO section
database = config_object["DATABASE"]
        
__databasename = database["database"]
__host = database["host"]
os.popen('mysql2sqlite -f "kat.db" -d "' + __databasename +'" -u "' + "root" +'" -p "' + "knapp22" +'" -h "' + __host +'" -q')