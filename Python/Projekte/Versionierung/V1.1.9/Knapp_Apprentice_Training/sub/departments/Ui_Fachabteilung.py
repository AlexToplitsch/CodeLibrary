# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\V 1.9 KAT(19.01.2021)\Knapp_Apprentice_Training\sub\departments\Fachabteilung.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Fachabteilungen(object):
    def setupUi(self, Fachabteilungen):
        Fachabteilungen.setObjectName("Fachabteilungen")
        Fachabteilungen.resize(797, 703)
        Fachabteilungen.setMinimumSize(QtCore.QSize(797, 703))
        font = QtGui.QFont()
        font.setPointSize(10)
        Fachabteilungen.setFont(font)
        Fachabteilungen.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Fachabteilungen)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Fachabteilungen)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(775, 321))
        self.groupBox.setObjectName("groupBox")
        self.lblfachabteilungabk = QtWidgets.QLabel(self.groupBox)
        self.lblfachabteilungabk.setGeometry(QtCore.QRect(80, 41, 131, 21))
        self.lblfachabteilungabk.setObjectName("lblfachabteilungabk")
        self.lblgebeaude = QtWidgets.QLabel(self.groupBox)
        self.lblgebeaude.setGeometry(QtCore.QRect(78, 106, 91, 21))
        self.lblgebeaude.setObjectName("lblgebeaude")
        self.lblfachabteilungbez = QtWidgets.QLabel(self.groupBox)
        self.lblfachabteilungbez.setGeometry(QtCore.QRect(50, 73, 121, 21))
        self.lblfachabteilungbez.setObjectName("lblfachabteilungbez")
        self.leFachabteilungabk = QtWidgets.QLineEdit(self.groupBox)
        self.leFachabteilungabk.setGeometry(QtCore.QRect(170, 41, 71, 22))
        self.leFachabteilungabk.setObjectName("leFachabteilungabk")
        self.leStock = QtWidgets.QLineEdit(self.groupBox)
        self.leStock.setGeometry(QtCore.QRect(170, 140, 70, 22))
        self.leStock.setObjectName("leStock")
        self.leFachabteilungbez = QtWidgets.QLineEdit(self.groupBox)
        self.leFachabteilungbez.setGeometry(QtCore.QRect(170, 73, 171, 22))
        self.leFachabteilungbez.setObjectName("leFachabteilungbez")
        self.lblstock = QtWidgets.QLabel(self.groupBox)
        self.lblstock.setGeometry(QtCore.QRect(100, 141, 71, 21))
        self.lblstock.setObjectName("lblstock")
        self.leGebaeude = QtWidgets.QLineEdit(self.groupBox)
        self.leGebaeude.setGeometry(QtCore.QRect(170, 105, 70, 22))
        self.leGebaeude.setObjectName("leGebaeude")
        self.btCSV = QtWidgets.QPushButton(self.groupBox)
        self.btCSV.setGeometry(QtCore.QRect(587, 280, 93, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btCSV.sizePolicy().hasHeightForWidth())
        self.btCSV.setSizePolicy(sizePolicy)
        self.btCSV.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btCSV.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/reporting_noun_report_document_file_icon_148360.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btCSV.setIcon(icon)
        self.btCSV.setObjectName("btCSV")
        self.btAbbrechen = QtWidgets.QPushButton(self.groupBox)
        self.btAbbrechen.setGeometry(QtCore.QRect(379, 280, 115, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btAbbrechen.sizePolicy().hasHeightForWidth())
        self.btAbbrechen.setSizePolicy(sizePolicy)
        self.btAbbrechen.setMinimumSize(QtCore.QSize(115, 0))
        self.btAbbrechen.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btAbbrechen.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/log-out_icon-icons.com_50106.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btAbbrechen.setIcon(icon1)
        self.btAbbrechen.setObjectName("btAbbrechen")
        self.btExcel = QtWidgets.QPushButton(self.groupBox)
        self.btExcel.setEnabled(True)
        self.btExcel.setGeometry(QtCore.QRect(494, 280, 93, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btExcel.sizePolicy().hasHeightForWidth())
        self.btExcel.setSizePolicy(sizePolicy)
        self.btExcel.setMaximumSize(QtCore.QSize(115, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btExcel.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/microsoft_excel_icon_132212.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btExcel.setIcon(icon2)
        self.btExcel.setObjectName("btExcel")
        self.btSuchen = QtWidgets.QPushButton(self.groupBox)
        self.btSuchen.setGeometry(QtCore.QRect(0, 280, 93, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btSuchen.sizePolicy().hasHeightForWidth())
        self.btSuchen.setSizePolicy(sizePolicy)
        self.btSuchen.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btSuchen.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/searchmagnifierinterfacesymbol1_79893.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSuchen.setIcon(icon3)
        self.btSuchen.setObjectName("btSuchen")
        self.btLoeschen = QtWidgets.QPushButton(self.groupBox)
        self.btLoeschen.setGeometry(QtCore.QRect(286, 280, 93, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btLoeschen.sizePolicy().hasHeightForWidth())
        self.btLoeschen.setSizePolicy(sizePolicy)
        self.btLoeschen.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btLoeschen.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/seo-social-web-network-internet_262_icon-icons.com_61518.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btLoeschen.setIcon(icon4)
        self.btLoeschen.setObjectName("btLoeschen")
        self.btClear = QtWidgets.QPushButton(self.groupBox)
        self.btClear.setGeometry(QtCore.QRect(93, 280, 93, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btClear.sizePolicy().hasHeightForWidth())
        self.btClear.setSizePolicy(sizePolicy)
        self.btClear.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btClear.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/-clear_90704.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btClear.setIcon(icon5)
        self.btClear.setObjectName("btClear")
        self.btSpeichern = QtWidgets.QPushButton(self.groupBox)
        self.btSpeichern.setGeometry(QtCore.QRect(186, 280, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btSpeichern.sizePolicy().hasHeightForWidth())
        self.btSpeichern.setSizePolicy(sizePolicy)
        self.btSpeichern.setMinimumSize(QtCore.QSize(100, 0))
        self.btSpeichern.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btSpeichern.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/save_3621.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSpeichern.setIcon(icon6)
        self.btSpeichern.setObjectName("btSpeichern")
        self.btHilfe = QtWidgets.QPushButton(self.groupBox)
        self.btHilfe.setGeometry(QtCore.QRect(680, 280, 95, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btHilfe.sizePolicy().hasHeightForWidth())
        self.btHilfe.setSizePolicy(sizePolicy)
        self.btHilfe.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btHilfe.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/info_13213.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btHilfe.setIcon(icon7)
        self.btHilfe.setObjectName("btHilfe")
        self.gbWochentage = QtWidgets.QGroupBox(self.groupBox)
        self.gbWochentage.setGeometry(QtCore.QRect(28, 190, 331, 71))
        self.gbWochentage.setObjectName("gbWochentage")
        self.cbFr = QtWidgets.QCheckBox(self.gbWochentage)
        self.cbFr.setGeometry(QtCore.QRect(270, 32, 51, 20))
        self.cbFr.setObjectName("cbFr")
        self.cbDo = QtWidgets.QCheckBox(self.gbWochentage)
        self.cbDo.setGeometry(QtCore.QRect(210, 32, 51, 20))
        self.cbDo.setObjectName("cbDo")
        self.cbMi = QtWidgets.QCheckBox(self.gbWochentage)
        self.cbMi.setGeometry(QtCore.QRect(150, 32, 51, 20))
        self.cbMi.setObjectName("cbMi")
        self.cbMo = QtWidgets.QCheckBox(self.gbWochentage)
        self.cbMo.setGeometry(QtCore.QRect(30, 32, 51, 20))
        self.cbMo.setObjectName("cbMo")
        self.cbDi = QtWidgets.QCheckBox(self.gbWochentage)
        self.cbDi.setGeometry(QtCore.QRect(90, 32, 51, 20))
        self.cbDi.setObjectName("cbDi")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(291, 381, 391, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gbAnsprechsperson = QtWidgets.QGroupBox(self.groupBox)
        self.gbAnsprechsperson.setGeometry(QtCore.QRect(387, 149, 371, 121))
        self.gbAnsprechsperson.setObjectName("gbAnsprechsperson")
        self.leAnsprechspersontel = QtWidgets.QLineEdit(self.gbAnsprechsperson)
        self.leAnsprechspersontel.setGeometry(QtCore.QRect(130, 90, 231, 22))
        self.leAnsprechspersontel.setObjectName("leAnsprechspersontel")
        self.lblAnsprechspersonname = QtWidgets.QLabel(self.gbAnsprechsperson)
        self.lblAnsprechspersonname.setGeometry(QtCore.QRect(52, 32, 81, 20))
        self.lblAnsprechspersonname.setObjectName("lblAnsprechspersonname")
        self.leAnsprechspersonname = QtWidgets.QLineEdit(self.gbAnsprechsperson)
        self.leAnsprechspersonname.setGeometry(QtCore.QRect(130, 30, 181, 22))
        self.leAnsprechspersonname.setObjectName("leAnsprechspersonname")
        self.lblApTelnr = QtWidgets.QLabel(self.gbAnsprechsperson)
        self.lblApTelnr.setGeometry(QtCore.QRect(50, 60, 71, 21))
        self.lblApTelnr.setObjectName("lblApTelnr")
        self.leAnsprechspersonemail = QtWidgets.QLineEdit(self.gbAnsprechsperson)
        self.leAnsprechspersonemail.setGeometry(QtCore.QRect(130, 60, 181, 22))
        self.leAnsprechspersonemail.setObjectName("leAnsprechspersonemail")
        self.lblApEmail = QtWidgets.QLabel(self.gbAnsprechsperson)
        self.lblApEmail.setGeometry(QtCore.QRect(50, 90, 81, 20))
        self.lblApEmail.setObjectName("lblApEmail")
        self.gbAbteilungsleiter = QtWidgets.QGroupBox(self.groupBox)
        self.gbAbteilungsleiter.setGeometry(QtCore.QRect(387, 20, 371, 121))
        self.gbAbteilungsleiter.setObjectName("gbAbteilungsleiter")
        self.leAbteilungsleitertel = QtWidgets.QLineEdit(self.gbAbteilungsleiter)
        self.leAbteilungsleitertel.setGeometry(QtCore.QRect(130, 90, 231, 22))
        self.leAbteilungsleitertel.setObjectName("leAbteilungsleitertel")
        self.lblAlTelnr = QtWidgets.QLabel(self.gbAbteilungsleiter)
        self.lblAlTelnr.setGeometry(QtCore.QRect(50, 61, 81, 21))
        self.lblAlTelnr.setObjectName("lblAlTelnr")
        self.leAbteilungsleiteremail = QtWidgets.QLineEdit(self.gbAbteilungsleiter)
        self.leAbteilungsleiteremail.setGeometry(QtCore.QRect(130, 60, 181, 22))
        self.leAbteilungsleiteremail.setObjectName("leAbteilungsleiteremail")
        self.lblAbteilungsleitername = QtWidgets.QLabel(self.gbAbteilungsleiter)
        self.lblAbteilungsleitername.setGeometry(QtCore.QRect(53, 31, 71, 21))
        self.lblAbteilungsleitername.setObjectName("lblAbteilungsleitername")
        self.lblAlEmail = QtWidgets.QLabel(self.gbAbteilungsleiter)
        self.lblAlEmail.setGeometry(QtCore.QRect(50, 90, 81, 20))
        self.lblAlEmail.setObjectName("lblAlEmail")
        self.leAbteilungsleitername = QtWidgets.QLineEdit(self.gbAbteilungsleiter)
        self.leAbteilungsleitername.setGeometry(QtCore.QRect(130, 30, 181, 22))
        self.leAbteilungsleitername.setObjectName("leAbteilungsleitername")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Fachabteilungen)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.lab_INFO = QtWidgets.QLabel(Fachabteilungen)
        self.lab_INFO.setText("")
        self.lab_INFO.setObjectName("lab_INFO")
        self.gridLayout.addWidget(self.lab_INFO, 2, 0, 1, 1)

        self.retranslateUi(Fachabteilungen)
        QtCore.QMetaObject.connectSlotsByName(Fachabteilungen)
        Fachabteilungen.setTabOrder(self.leFachabteilungabk, self.leFachabteilungbez)
        Fachabteilungen.setTabOrder(self.leFachabteilungbez, self.leGebaeude)
        Fachabteilungen.setTabOrder(self.leGebaeude, self.leStock)
        Fachabteilungen.setTabOrder(self.leStock, self.cbMo)
        Fachabteilungen.setTabOrder(self.cbMo, self.cbDi)
        Fachabteilungen.setTabOrder(self.cbDi, self.cbMi)
        Fachabteilungen.setTabOrder(self.cbMi, self.cbDo)
        Fachabteilungen.setTabOrder(self.cbDo, self.cbFr)
        Fachabteilungen.setTabOrder(self.cbFr, self.leAbteilungsleitername)
        Fachabteilungen.setTabOrder(self.leAbteilungsleitername, self.leAbteilungsleiteremail)
        Fachabteilungen.setTabOrder(self.leAbteilungsleiteremail, self.leAbteilungsleitertel)
        Fachabteilungen.setTabOrder(self.leAbteilungsleitertel, self.leAnsprechspersonname)
        Fachabteilungen.setTabOrder(self.leAnsprechspersonname, self.leAnsprechspersonemail)
        Fachabteilungen.setTabOrder(self.leAnsprechspersonemail, self.leAnsprechspersontel)
        Fachabteilungen.setTabOrder(self.leAnsprechspersontel, self.btSuchen)
        Fachabteilungen.setTabOrder(self.btSuchen, self.btClear)
        Fachabteilungen.setTabOrder(self.btClear, self.btSpeichern)
        Fachabteilungen.setTabOrder(self.btSpeichern, self.btLoeschen)
        Fachabteilungen.setTabOrder(self.btLoeschen, self.btAbbrechen)
        Fachabteilungen.setTabOrder(self.btAbbrechen, self.btExcel)
        Fachabteilungen.setTabOrder(self.btExcel, self.btCSV)
        Fachabteilungen.setTabOrder(self.btCSV, self.btHilfe)
        Fachabteilungen.setTabOrder(self.btHilfe, self.tableWidget)

    def retranslateUi(self, Fachabteilungen):
        _translate = QtCore.QCoreApplication.translate
        Fachabteilungen.setWindowTitle(_translate("Fachabteilungen", "Fachabteilungen"))
        self.groupBox.setTitle(_translate("Fachabteilungen", "Fachabteilungen"))
        self.lblfachabteilungabk.setText(_translate("Fachabteilungen", "Abt.-KZ:"))
        self.lblgebeaude.setText(_translate("Fachabteilungen", "Gebäude:"))
        self.lblfachabteilungbez.setText(_translate("Fachabteilungen", "Bezeichnung:"))
        self.lblstock.setText(_translate("Fachabteilungen", "Stock:"))
        self.btCSV.setText(_translate("Fachabteilungen", "Report"))
        self.btAbbrechen.setText(_translate("Fachabteilungen", "Hauptmenü"))
        self.btExcel.setText(_translate("Fachabteilungen", "Excel"))
        self.btSuchen.setText(_translate("Fachabteilungen", "Suchen"))
        self.btLoeschen.setText(_translate("Fachabteilungen", "Löschen"))
        self.btClear.setText(_translate("Fachabteilungen", "Leeren"))
        self.btSpeichern.setText(_translate("Fachabteilungen", "Speichern"))
        self.btHilfe.setText(_translate("Fachabteilungen", "Hilfe"))
        self.gbWochentage.setTitle(_translate("Fachabteilungen", "Pflichtanwesenheit"))
        self.cbFr.setText(_translate("Fachabteilungen", "Fr"))
        self.cbDo.setText(_translate("Fachabteilungen", "Do"))
        self.cbMi.setText(_translate("Fachabteilungen", "Mi"))
        self.cbMo.setText(_translate("Fachabteilungen", "Mo"))
        self.cbDi.setText(_translate("Fachabteilungen", "Di"))
        self.groupBox_2.setTitle(_translate("Fachabteilungen", "GroupBox"))
        self.gbAnsprechsperson.setTitle(_translate("Fachabteilungen", "Ansprechsperson"))
        self.lblAnsprechspersonname.setText(_translate("Fachabteilungen", "Name:"))
        self.lblApTelnr.setText(_translate("Fachabteilungen", "Tel-Nr:"))
        self.lblApEmail.setText(_translate("Fachabteilungen", "E-Mail:"))
        self.gbAbteilungsleiter.setTitle(_translate("Fachabteilungen", "Abteilungsleiter"))
        self.lblAlTelnr.setText(_translate("Fachabteilungen", "Tel-Nr:"))
        self.lblAbteilungsleitername.setText(_translate("Fachabteilungen", "Name:"))
        self.lblAlEmail.setText(_translate("Fachabteilungen", "E-Mail:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fachabteilungen = QtWidgets.QDialog()
    ui = Ui_Fachabteilungen()
    ui.setupUi(Fachabteilungen)
    Fachabteilungen.show()
    sys.exit(app.exec_())