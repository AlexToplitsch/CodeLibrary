# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gornicec\Downloads\V1.5\Knapp_Apprentice_Training\users.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(607, 470)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QPushButton:hover {\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton:focus {\n"
"    border-width: 2px;\n"
"}\n"
"QPushButton{\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"background-color: #DDDDDD;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit{\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"background-color: #FFFFFF;\n"
"border-radius:4px;\n"
"}\n"
"QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(216, 216, 216, 255), stop:1 rgba(162, 162, 162, 255))\n"
"}\n"
"\n"
"")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSpeichern = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSpeichern.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\gornicec\\Downloads\\V1.5\\Knapp_Apprentice_Training\\_Symbole/UsedSymbols/save_3621.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSpeichern.setIcon(icon)
        self.btnSpeichern.setCheckable(False)
        self.btnSpeichern.setObjectName("btnSpeichern")
        self.gridLayout.addWidget(self.btnSpeichern, 0, 2, 1, 1)
        self.leBenutzername = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leBenutzername.setFont(font)
        self.leBenutzername.setFrame(False)
        self.leBenutzername.setObjectName("leBenutzername")
        self.gridLayout.addWidget(self.leBenutzername, 0, 1, 1, 1)
        self.btnAbbrechen = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAbbrechen.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\gornicec\\Downloads\\V1.5\\Knapp_Apprentice_Training\\_Symbole/UsedSymbols/-clear_90704.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAbbrechen.setIcon(icon1)
        self.btnAbbrechen.setObjectName("btnAbbrechen")
        self.gridLayout.addWidget(self.btnAbbrechen, 1, 2, 1, 2)
        self.cbAdmin = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbAdmin.setFont(font)
        self.cbAdmin.setObjectName("cbAdmin")
        self.gridLayout.addWidget(self.cbAdmin, 2, 0, 1, 1)
        self.lblPasswort = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPasswort.setFont(font)
        self.lblPasswort.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblPasswort.setStyleSheet("")
        self.lblPasswort.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPasswort.setObjectName("lblPasswort")
        self.gridLayout.addWidget(self.lblPasswort, 1, 0, 1, 1)
        self.btnLoeschen = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnLoeschen.setFont(font)
        self.btnLoeschen.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\gornicec\\Downloads\\V1.5\\Knapp_Apprentice_Training\\_Symbole/UsedSymbols/seo-social-web-network-internet_262_icon-icons.com_61518.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLoeschen.setIcon(icon2)
        self.btnLoeschen.setObjectName("btnLoeschen")
        self.gridLayout.addWidget(self.btnLoeschen, 0, 3, 1, 1)
        self.lblBenutzername = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblBenutzername.setFont(font)
        self.lblBenutzername.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblBenutzername.setObjectName("lblBenutzername")
        self.gridLayout.addWidget(self.lblBenutzername, 0, 0, 1, 1)
        self.cbStammdaten = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbStammdaten.setFont(font)
        self.cbStammdaten.setObjectName("cbStammdaten")
        self.gridLayout.addWidget(self.cbStammdaten, 3, 0, 1, 2)
        self.lePasswort = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lePasswort.setFont(font)
        self.lePasswort.setStyleSheet("")
        self.lePasswort.setFrame(False)
        self.lePasswort.setObjectName("lePasswort")
        self.gridLayout.addWidget(self.lePasswort, 1, 1, 1, 1)
        self.cbWochenplan = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbWochenplan.setFont(font)
        self.cbWochenplan.setObjectName("cbWochenplan")
        self.gridLayout.addWidget(self.cbWochenplan, 4, 0, 1, 2)
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table.setStyleSheet("\n"
"")
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.table, 5, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.leBenutzername, self.lePasswort)
        Dialog.setTabOrder(self.lePasswort, self.cbAdmin)
        Dialog.setTabOrder(self.cbAdmin, self.cbStammdaten)
        Dialog.setTabOrder(self.cbStammdaten, self.cbWochenplan)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nutzerverwaltung"))
        self.btnSpeichern.setText(_translate("Dialog", "Speichern"))
        self.leBenutzername.setPlaceholderText(_translate("Dialog", "mustermann"))
        self.btnAbbrechen.setText(_translate("Dialog", "Abbrechen"))
        self.cbAdmin.setText(_translate("Dialog", "Test"))
        self.lblPasswort.setText(_translate("Dialog", "Passwort"))
        self.btnLoeschen.setText(_translate("Dialog", "Löschen"))
        self.lblBenutzername.setText(_translate("Dialog", "Benutzername"))
        self.cbStammdaten.setText(_translate("Dialog", "Stammdaten"))
        self.lePasswort.setPlaceholderText(_translate("Dialog", "musterpasswort"))
        self.cbWochenplan.setText(_translate("Dialog", "Wochenplan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())