from shutil import copyfile
import os, subprocess

if __name__ == "__main__":
    f = open("C://Users//toplitsc//Desktop//demofile2.bat", "w")
    f.write('@echo off\n'+
            'setlocal enabledelayedexpansion\n' +
            '\nset windowExists=0\n'+
            'echo !windowExists!\n'+
            'tasklist /fi "IMAGENAME eq cmd.exe" /fi "WINDOWTITLE eq katUpdate" |find "keine" >nul || set windowExists=1\n'+
            'echo schaise: !windowExists!\n'+
            '\ntitle katUpdate\n'+
            'echo set\n'+
            '\nif !windowExists! == 0 (\n'+
            '\tif exist "kat.db" (\n'+
            '\t\tdel "kat.db"\n'+
            '\t)\n'+
            ')\n'+
            'if !windowExists! == 0 (\n'+
            '\tmysql2sqlite -f "kat.db" -d "kat" -u "root" -p "knapp22" -h "10.33.35.171" -q\n'+
            ') else (\n'+
            '\techo katdb nicht gemacht\n'+
            ')')
    f.close()
    subprocess.call([r'C:\Users\toplitsc\Desktop\demofile2.bat'])
