# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\apprentice_management_system\sub/specialmodules/spezial_suche.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1072, 720)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(754, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.pB_BEENDEN = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\apprentice_management_system\\sub/specialmodules\\../../../_Symbole/Icons/computer/MSGBOX01.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_BEENDEN.setIcon(icon)
        self.pB_BEENDEN.setObjectName("pB_BEENDEN")
        self.gridLayout.addWidget(self.pB_BEENDEN, 0, 2, 1, 1)
        self.tableView_db = QtWidgets.QTableView(Dialog)
        self.tableView_db.setObjectName("tableView_db")
        self.gridLayout.addWidget(self.tableView_db, 1, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Filter für Datenanzeige eingeben"))
        self.pB_BEENDEN.setText(_translate("Dialog", "Beenden"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())