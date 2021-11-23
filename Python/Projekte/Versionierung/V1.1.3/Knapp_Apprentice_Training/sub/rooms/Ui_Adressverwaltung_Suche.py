# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\Projekte\Knapp_Apprentice_Training\sub\rooms\Adressverwaltung_Suche.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(718, 331)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.pB_BEENDEN = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../UsedSymbols/log-out_icon-icons.com_50106.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_BEENDEN.setIcon(icon)
        self.pB_BEENDEN.setObjectName("pB_BEENDEN")
        self.gridLayout.addWidget(self.pB_BEENDEN, 0, 5, 1, 1)
        self.lb_Room = QtWidgets.QLabel(Dialog)
        self.lb_Room.setObjectName("lb_Room")
        self.gridLayout.addWidget(self.lb_Room, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.tableView_db = QtWidgets.QTableView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_db.sizePolicy().hasHeightForWidth())
        self.tableView_db.setSizePolicy(sizePolicy)
        self.tableView_db.setMinimumSize(QtCore.QSize(0, 200))
        self.tableView_db.setObjectName("tableView_db")
        self.gridLayout.addWidget(self.tableView_db, 1, 0, 1, 6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pB_BEENDEN.setText(_translate("Dialog", "Beenden"))
        self.lb_Room.setText(_translate("Dialog", "Names des Raumes:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
