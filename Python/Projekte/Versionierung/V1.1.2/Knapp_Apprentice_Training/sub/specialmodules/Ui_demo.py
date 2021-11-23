# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\Projekte\Knapp_Apprentice_Training\sub\specialmodules\demo.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(859, 749)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_speichern = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../_Symbole/Icons/computer/DISK04.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_speichern.setIcon(icon)
        self.btn_speichern.setObjectName("btn_speichern")
        self.gridLayout.addWidget(self.btn_speichern, 1, 1, 1, 1)
        self.btn_Suchen = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../_Symbole/Icons/misc/BINOCULR.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Suchen.setIcon(icon1)
        self.btn_Suchen.setObjectName("btn_Suchen")
        self.gridLayout.addWidget(self.btn_Suchen, 1, 0, 1, 1)
        self.btn_excel = QtWidgets.QPushButton(Dialog)
        self.btn_excel.setObjectName("btn_excel")
        self.gridLayout.addWidget(self.btn_excel, 1, 4, 1, 1)
        self.btn_report = QtWidgets.QPushButton(Dialog)
        self.btn_report.setObjectName("btn_report")
        self.gridLayout.addWidget(self.btn_report, 1, 5, 1, 1)
        self.btn_menue = QtWidgets.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../_Symbole/Icons/computer/W95MBX01.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menue.setIcon(icon2)
        self.btn_menue.setObjectName("btn_menue")
        self.gridLayout.addWidget(self.btn_menue, 1, 3, 1, 1)
        self.gb_Spezial = QtWidgets.QGroupBox(Dialog)
        self.gb_Spezial.setObjectName("gb_Spezial")
        self.lb_mod = QtWidgets.QLabel(self.gb_Spezial)
        self.lb_mod.setGeometry(QtCore.QRect(130, 50, 91, 16))
        self.lb_mod.setObjectName("lb_mod")
        self.lb_beschr = QtWidgets.QLabel(self.gb_Spezial)
        self.lb_beschr.setGeometry(QtCore.QRect(60, 120, 151, 21))
        self.lb_beschr.setObjectName("lb_beschr")
        self.le_Modul = QtWidgets.QLineEdit(self.gb_Spezial)
        self.le_Modul.setGeometry(QtCore.QRect(240, 50, 411, 22))
        self.le_Modul.setObjectName("le_Modul")
        self.te_Beschreib = QtWidgets.QTextEdit(self.gb_Spezial)
        self.te_Beschreib.setGeometry(QtCore.QRect(240, 100, 411, 181))
        self.te_Beschreib.setToolTipDuration(-1)
        self.te_Beschreib.setObjectName("te_Beschreib")
        self.gridLayout.addWidget(self.gb_Spezial, 0, 0, 1, 7)
        self.btn_hilfe = QtWidgets.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../_Symbole/Icons/computer/MSGBOX04.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hilfe.setIcon(icon3)
        self.btn_hilfe.setObjectName("btn_hilfe")
        self.gridLayout.addWidget(self.btn_hilfe, 1, 6, 1, 1)
        self.btn_loschen = QtWidgets.QPushButton(Dialog)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../_Symbole/Icons/computer/TRASH01.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_loschen.setIcon(icon4)
        self.btn_loschen.setObjectName("btn_loschen")
        self.gridLayout.addWidget(self.btn_loschen, 1, 2, 1, 1)
        self.tw_Table = QtWidgets.QTableWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_Table.sizePolicy().hasHeightForWidth())
        self.tw_Table.setSizePolicy(sizePolicy)
        self.tw_Table.setFrameShape(QtWidgets.QFrame.Box)
        self.tw_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tw_Table.setObjectName("tw_Table")
        self.tw_Table.setColumnCount(0)
        self.tw_Table.setRowCount(0)
        self.gridLayout.addWidget(self.tw_Table, 2, 0, 1, 7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_speichern.setText(_translate("Dialog", "Speichern"))
        self.btn_Suchen.setText(_translate("Dialog", "Suchen"))
        self.btn_excel.setText(_translate("Dialog", "Excel"))
        self.btn_report.setText(_translate("Dialog", "Report"))
        self.btn_menue.setText(_translate("Dialog", "Hauptmenü"))
        self.gb_Spezial.setTitle(_translate("Dialog", "Spezialmodule"))
        self.lb_mod.setText(_translate("Dialog", "Spezialmodul"))
        self.lb_beschr.setText(_translate("Dialog", "Beschreibung/Anmerkung"))
        self.btn_hilfe.setText(_translate("Dialog", "Hilfe"))
        self.btn_loschen.setText(_translate("Dialog", "Löschen"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
