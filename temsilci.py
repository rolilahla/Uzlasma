# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temsilci.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Temsilci(object):
    def setupUi(self, Temsilci):
        Temsilci.setObjectName("Temsilci")
        Temsilci.resize(265, 135)
        self.label_13 = QtWidgets.QLabel(Temsilci)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(Temsilci)
        self.lineEdit_12.setGeometry(QtCore.QRect(100, 10, 141, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_14 = QtWidgets.QLabel(Temsilci)
        self.label_14.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_13 = QtWidgets.QLineEdit(Temsilci)
        self.lineEdit_13.setGeometry(QtCore.QRect(100, 40, 141, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton = QtWidgets.QPushButton(Temsilci)
        self.pushButton.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Temsilci)
        QtCore.QMetaObject.connectSlotsByName(Temsilci)

    def retranslateUi(self, Temsilci):
        _translate = QtCore.QCoreApplication.translate
        Temsilci.setWindowTitle(_translate("Temsilci", "Kanuni Temsilci Bilgileri"))
        self.label_13.setText(_translate("Temsilci", "Ad Soyad"))
        self.label_14.setText(_translate("Temsilci", "Sicil No"))
        self.pushButton.setText(_translate("Temsilci", "Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Temsilci = QtWidgets.QDialog()
    ui = Ui_Temsilci()
    ui.setupUi(Temsilci)
    Temsilci.show()
    sys.exit(app.exec_())

