# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Knapp_Apprentice_Training\sub\ausbildungsthemen\Unterrichtsthemen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Unterrichtsthemen(object):
    def setupUi(self, Unterrichtsthemen):
        Unterrichtsthemen.setObjectName("Unterrichtsthemen")
        Unterrichtsthemen.resize(632, 428)
        Unterrichtsthemen.setSizeGripEnabled(True)
        self.groupBox = QtWidgets.QGroupBox(Unterrichtsthemen)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 611, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.le_name = QtWidgets.QLineEdit(self.groupBox)
        self.le_name.setGeometry(QtCore.QRect(50, 30, 541, 20))
        self.le_name.setObjectName("le_name")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.label.setObjectName("label")
        self.tw_anzeige = QtWidgets.QTableWidget(self.groupBox)
        self.tw_anzeige.setGeometry(QtCore.QRect(0, 110, 611, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_anzeige.sizePolicy().hasHeightForWidth())
        self.tw_anzeige.setSizePolicy(sizePolicy)
        self.tw_anzeige.setObjectName("tw_anzeige")
        self.tw_anzeige.setColumnCount(0)
        self.tw_anzeige.setRowCount(0)
        self.pb_excel = QtWidgets.QPushButton(self.groupBox)
        self.pb_excel.setGeometry(QtCore.QRect(380, 80, 71, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/microsoft_excel_icon_132212.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_excel.setIcon(icon)
        self.pb_excel.setObjectName("pb_excel")
        self.pb_back = QtWidgets.QPushButton(self.groupBox)
        self.pb_back.setGeometry(QtCore.QRect(270, 80, 91, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/log-out_icon-icons.com_50106.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_back.setIcon(icon1)
        self.pb_back.setObjectName("pb_back")
        self.pb_delete = QtWidgets.QPushButton(self.groupBox)
        self.pb_delete.setGeometry(QtCore.QRect(180, 80, 71, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/seo-social-web-network-internet_262_icon-icons.com_61518.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_delete.setIcon(icon2)
        self.pb_delete.setObjectName("pb_delete")
        self.pb_report = QtWidgets.QPushButton(self.groupBox)
        self.pb_report.setGeometry(QtCore.QRect(460, 80, 71, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/reporting_noun_report_document_file_icon_148360.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_report.setIcon(icon3)
        self.pb_report.setObjectName("pb_report")
        self.pb_hilfe = QtWidgets.QPushButton(self.groupBox)
        self.pb_hilfe.setGeometry(QtCore.QRect(540, 80, 71, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/info_13213.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_hilfe.setIcon(icon4)
        self.pb_hilfe.setObjectName("pb_hilfe")
        self.pb_suchen = QtWidgets.QPushButton(self.groupBox)
        self.pb_suchen.setGeometry(QtCore.QRect(0, 80, 71, 23))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/searchmagnifierinterfacesymbol1_79893.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_suchen.setIcon(icon5)
        self.pb_suchen.setObjectName("pb_suchen")
        self.pb_speichern = QtWidgets.QPushButton(self.groupBox)
        self.pb_speichern.setGeometry(QtCore.QRect(80, 80, 91, 23))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/save_3621.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_speichern.setIcon(icon6)
        self.pb_speichern.setObjectName("pb_speichern")
        self.lab_INFO = QtWidgets.QLabel(Unterrichtsthemen)
        self.lab_INFO.setGeometry(QtCore.QRect(10, 394, 611, 31))
        self.lab_INFO.setText("")
        self.lab_INFO.setObjectName("lab_INFO")

        self.retranslateUi(Unterrichtsthemen)
        QtCore.QMetaObject.connectSlotsByName(Unterrichtsthemen)

    def retranslateUi(self, Unterrichtsthemen):
        _translate = QtCore.QCoreApplication.translate
        Unterrichtsthemen.setWindowTitle(_translate("Unterrichtsthemen", "Ausbildungsthemen"))
        self.groupBox.setTitle(_translate("Unterrichtsthemen", "Ausbildungsthemen"))
        self.label.setText(_translate("Unterrichtsthemen", "Name:"))
        self.pb_excel.setText(_translate("Unterrichtsthemen", "Excel"))
        self.pb_back.setText(_translate("Unterrichtsthemen", "Hauptmenü"))
        self.pb_delete.setText(_translate("Unterrichtsthemen", "Löschen"))
        self.pb_report.setText(_translate("Unterrichtsthemen", "Report"))
        self.pb_hilfe.setText(_translate("Unterrichtsthemen", "Hilfe"))
        self.pb_suchen.setText(_translate("Unterrichtsthemen", "Suchen"))
        self.pb_speichern.setText(_translate("Unterrichtsthemen", "Speichern"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Unterrichtsthemen = QtWidgets.QDialog()
    ui = Ui_Unterrichtsthemen()
    ui.setupUi(Unterrichtsthemen)
    Unterrichtsthemen.show()
    sys.exit(app.exec_())