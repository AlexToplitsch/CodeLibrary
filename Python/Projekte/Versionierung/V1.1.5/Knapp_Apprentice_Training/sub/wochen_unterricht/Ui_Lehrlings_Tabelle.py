# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\Projekte\Knapp_Apprentice_Training\sub\wochen_unterricht\Lehrlings_Tabelle.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 477)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget_lehrlinge_liste = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_lehrlinge_liste.setObjectName("tableWidget_lehrlinge_liste")
        self.tableWidget_lehrlinge_liste.setColumnCount(0)
        self.tableWidget_lehrlinge_liste.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_lehrlinge_liste)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_hinzufuegen = QtWidgets.QPushButton(Dialog)
        self.pushButton_hinzufuegen.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/add_insert_new_plus_icon_148990.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_hinzufuegen.setIcon(icon)
        self.pushButton_hinzufuegen.setObjectName("pushButton_hinzufuegen")
        self.horizontalLayout.addWidget(self.pushButton_hinzufuegen)
        self.pushButton_abbrechen = QtWidgets.QPushButton(Dialog)
        self.pushButton_abbrechen.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("_Symbole/UsedSymbols/closewindowapplication_cerca_ventan_2874.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_abbrechen.setIcon(icon1)
        self.pushButton_abbrechen.setObjectName("pushButton_abbrechen")
        self.horizontalLayout.addWidget(self.pushButton_abbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Lehrlinge"))
        self.pushButton_hinzufuegen.setText(_translate("Dialog", "Hinzufügen"))
        self.pushButton_abbrechen.setText(_translate("Dialog", "Abbrechen"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
