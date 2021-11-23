# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from tkinter import messagebox  #gibt eine Message-BOX aus

from other.database import Database

from sub.mainwindow.Ui_mainwindow import Ui_MainWindow

from sub.apprentice.apprentice_list import GuiApprenticeList
from sub.learningcontent.Lehrstoff import Lehrstoff
from sub.lapcontent.LAP_Themenkatalog import Themenkatalog
from sub.ausbildungsthemen.Unterrichtsthemen import Unterrichtsthemen
from sub.field.Fachrichtungen import Fachrichtungen
from sub.rooms.Raeume import Raeume
from sub.specialmodules.Spezialmodule import Spezialmodule
from sub.wochen_unterricht.Wochen_Unterricht import Wochen_Unterricht
from sub.rotation.Lehrlingseinteilungstabelle import Lehrlingseinteilungtabelle
from sub.trainer.Ausbilder import Ausbilder
from sub.bs.Bs import Bs
###############Hauptfenster###############

class gui_mainwindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(gui_mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.frameGeometry().width(), self.frameGeometry().height())
        self.statusBar().setSizeGripEnabled(False)
        self.label_eingeloggt_als.setText(self.parent().benutzername)
        self.INFO("Hauptfenster wurde geöffnet",  "I")# info asugabe

    def INFO(self,  MELDUNG,  INFO_STAT): #Zentrale Ausgabe von Infos/Meldungen
        self.lab_INFO.setText(MELDUNG) #Text aus MELDUNG übernehmen und ausgeben
        if INFO_STAT == "F": #Fehler
            self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,0,0) }")
            messagebox.showerror("Fehler", MELDUNG)
        else:
            if INFO_STAT == "H": #Hinweis
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(255,197,20) }")
                messagebox.showwarning("Hinweis/Warnung", MELDUNG)
            else:
                self.lab_INFO.setStyleSheet("QLabel { background-color : rgb(85,170,127) }")
    
    @pyqtSlot()
    def on_pushButton_lehrlinge_clicked(self):
        w = GuiApprenticeList(self)
        w.show()
        self.hide()
    
    @pyqtSlot()
    def on_pushButton_abmelden_clicked(self):
        self.back_to_login()
        
    @pyqtSlot()
    def on_pushButton_lehrberufe_clicked(self):
        w = Fachrichtungen(self)
        w.show()
        self.hide()
        
    @pyqtSlot()
    def on_pushButton_raeume_clicked(self):
        w = Raeume(self)
        w.show()
        self.hide()
        
    @pyqtSlot()
    def on_pushButton_lehrstoff_clicked(self):
        w = Lehrstoff(self)
        w.show()
        self.hide()
        
    @pyqtSlot()
    def on_pushButton_ausbilder_clicked(self):
        w = Ausbilder(self)
        w.show()
        self.hide()
        
    @pyqtSlot()    
    def on_pushButton_spezialmodule_clicked(self):
        w = Spezialmodule(self)
        w.show()
        self.hide()
        
    @pyqtSlot()
    def on_pushButton_LAP_Themekatalog_clicked(self):
        w = Themenkatalog(self)
        w.show()
        self.hide()
        
        
    def back_to_login(self):
        Database.log_out()
        self.parent().lineEdit_benutzername.setText("")
        self.parent().lineEdit_passwort.setText("")
        self.parent().show()
        self.close()
    
    @pyqtSlot()
    def on_pushButton_Wochen_U_clicked(self):
        """
        Slot documentation goes here.
        """
        w = Wochen_Unterricht(self)
        w.show()
        self.hide()        
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_LAP_Themenkatalog_clicked(self):
        """
        Slot documentation goes here.
        """
        w = Themenkatalog(self)
        w.show()
        self.hide()
    
    
    def closeEvent(self, event):
        self.back_to_login()
    
    @pyqtSlot()
    def on_pushButton_Unterrichtsthemen_clicked(self):
        """
        Slot documentation goes here.
        """
        w = Unterrichtsthemen(self)
        w.show()
        self.hide()
    
    @pyqtSlot()
    def on_pushButton_Berufsschulzeiten_clicked(self):
        """
        Slot documentation goes here.
        """
        w= Bs(self)
        w.show()
        self.hide()
    
    @pyqtSlot()
    def on_pB_Lehrlingseinteilung_clicked(self):
        """
        Slot documentation goes here.
        """
        w = Lehrlingseinteilungtabelle(self)
        w.show()
        self.hide()
