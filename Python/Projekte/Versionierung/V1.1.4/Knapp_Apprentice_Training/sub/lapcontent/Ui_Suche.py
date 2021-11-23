# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\Projekte\Knapp_Apprentice_Training\sub\lapcontent\Suche.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LAP_Themenkatalog_Suche(object):
    def setupUi(self, LAP_Themenkatalog_Suche):
        LAP_Themenkatalog_Suche.setObjectName("LAP_Themenkatalog_Suche")
        LAP_Themenkatalog_Suche.resize(713, 450)
        LAP_Themenkatalog_Suche.setMinimumSize(QtCore.QSize(713, 450))
        LAP_Themenkatalog_Suche.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(LAP_Themenkatalog_Suche)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gB_Suchfelder = QtWidgets.QGroupBox(LAP_Themenkatalog_Suche)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gB_Suchfelder.sizePolicy().hasHeightForWidth())
        self.gB_Suchfelder.setSizePolicy(sizePolicy)
        self.gB_Suchfelder.setMinimumSize(QtCore.QSize(695, 120))
        self.gB_Suchfelder.setObjectName("gB_Suchfelder")
        self.gridLayout = QtWidgets.QGridLayout(self.gB_Suchfelder)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_Ausbilder = QtWidgets.QLabel(self.gB_Suchfelder)
        self.lbl_Ausbilder.setObjectName("lbl_Ausbilder")
        self.gridLayout.addWidget(self.lbl_Ausbilder, 0, 2, 1, 1)
        self.lbl_Fachrichtung = QtWidgets.QLabel(self.gB_Suchfelder)
        self.lbl_Fachrichtung.setObjectName("lbl_Fachrichtung")
        self.gridLayout.addWidget(self.lbl_Fachrichtung, 0, 0, 1, 1)
        self.le_Fachrichtung = QtWidgets.QLineEdit(self.gB_Suchfelder)
        self.le_Fachrichtung.setObjectName("le_Fachrichtung")
        self.gridLayout.addWidget(self.le_Fachrichtung, 0, 1, 1, 1)
        self.lbl_Thema = QtWidgets.QLabel(self.gB_Suchfelder)
        self.lbl_Thema.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Thema.setObjectName("lbl_Thema")
        self.gridLayout.addWidget(self.lbl_Thema, 1, 0, 1, 1)
        self.le_Ausbilder = QtWidgets.QLineEdit(self.gB_Suchfelder)
        self.le_Ausbilder.setObjectName("le_Ausbilder")
        self.gridLayout.addWidget(self.le_Ausbilder, 0, 3, 1, 1)
        self.le_Thema = QtWidgets.QLineEdit(self.gB_Suchfelder)
        self.le_Thema.setObjectName("le_Thema")
        self.gridLayout.addWidget(self.le_Thema, 1, 1, 1, 3)
        self.gridLayout_2.addWidget(self.gB_Suchfelder, 0, 0, 1, 1)
        self.tW_LAP_Themenkatalog_DB = QtWidgets.QTableWidget(LAP_Themenkatalog_Suche)
        self.tW_LAP_Themenkatalog_DB.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tW_LAP_Themenkatalog_DB.setObjectName("tW_LAP_Themenkatalog_DB")
        self.tW_LAP_Themenkatalog_DB.setColumnCount(0)
        self.tW_LAP_Themenkatalog_DB.setRowCount(0)
        self.gridLayout_2.addWidget(self.tW_LAP_Themenkatalog_DB, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(500)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pB_Suchen = QtWidgets.QPushButton(LAP_Themenkatalog_Suche)
        self.pB_Suchen.setMaximumSize(QtCore.QSize(100, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../_Symbole/UsedSymbols/searchmagnifierinterfacesymbol1_79893.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Suchen.setIcon(icon)
        self.pB_Suchen.setObjectName("pB_Suchen")
        self.horizontalLayout.addWidget(self.pB_Suchen)
        self.pB_Beenden = QtWidgets.QPushButton(LAP_Themenkatalog_Suche)
        self.pB_Beenden.setMaximumSize(QtCore.QSize(100, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../_Symbole/UsedSymbols/log-out_icon-icons.com_50106.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Beenden.setIcon(icon1)
        self.pB_Beenden.setObjectName("pB_Beenden")
        self.horizontalLayout.addWidget(self.pB_Beenden)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(LAP_Themenkatalog_Suche)
        QtCore.QMetaObject.connectSlotsByName(LAP_Themenkatalog_Suche)

    def retranslateUi(self, LAP_Themenkatalog_Suche):
        _translate = QtCore.QCoreApplication.translate
        LAP_Themenkatalog_Suche.setWindowTitle(_translate("LAP_Themenkatalog_Suche", "Suche"))
        self.gB_Suchfelder.setTitle(_translate("LAP_Themenkatalog_Suche", "Suchfelder"))
        self.lbl_Ausbilder.setText(_translate("LAP_Themenkatalog_Suche", "Ausblider:"))
        self.lbl_Fachrichtung.setText(_translate("LAP_Themenkatalog_Suche", "Fachrichtung:"))
        self.lbl_Thema.setText(_translate("LAP_Themenkatalog_Suche", "Thema:"))
        self.pB_Suchen.setText(_translate("LAP_Themenkatalog_Suche", "Suchen"))
        self.pB_Beenden.setText(_translate("LAP_Themenkatalog_Suche", "Beenden"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LAP_Themenkatalog_Suche = QtWidgets.QDialog()
    ui = Ui_LAP_Themenkatalog_Suche()
    ui.setupUi(LAP_Themenkatalog_Suche)
    LAP_Themenkatalog_Suche.show()
    sys.exit(app.exec_())
