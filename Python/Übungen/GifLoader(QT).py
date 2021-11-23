# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYffVAB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient, QMovie)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(428, 179)
        self.label = QLabel(Dialog)
        self.movie = QMovie("C://Users//toplitsc//Downloads//ajax-loader.gif")
        self.label.setMovie(self.movie)
        self.label.show()
        self.movie.start()
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 40, 151, 61))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", None, None))
    # retranslateUi


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
