# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'b1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Uzlasma(object):
    def setupUi(self, Uzlasma):
        Uzlasma.setObjectName("Uzlasma")
        Uzlasma.resize(308, 243)
        self.label_5 = QtWidgets.QLabel(Uzlasma)
        self.label_5.setGeometry(QtCore.QRect(11, 130, 93, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Uzlasma)
        self.label_2.setGeometry(QtCore.QRect(11, 40, 55, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Uzlasma)
        self.pushButton.setGeometry(QtCore.QRect(190, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Uzlasma)
        self.label.setGeometry(QtCore.QRect(11, 12, 71, 20))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Uzlasma)
        self.label_4.setGeometry(QtCore.QRect(11, 100, 56, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Uzlasma)
        self.label_3.setGeometry(QtCore.QRect(11, 70, 86, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Uzlasma)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Uzlasma)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Uzlasma)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 70, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Uzlasma)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 100, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Uzlasma)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 130, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Uzlasma)
        self.label_6.setGeometry(QtCore.QRect(11, 160, 93, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(Uzlasma)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 160, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Uzlasma)
        self.pushButton.clicked.connect(Uzlasma.close)
        QtCore.QMetaObject.connectSlotsByName(Uzlasma)

    def retranslateUi(self, Uzlasma):
        _translate = QtCore.QCoreApplication.translate
        Uzlasma.setWindowTitle(_translate("Uzlasma", "Uzlaşma Oluştur"))
        self.label_5.setText(_translate("Uzlasma", "Teklif / Davet Tarihi"))
        self.label_2.setText(_translate("Uzlasma", "Uzlaşma No"))
        self.pushButton.setText(_translate("Uzlasma", "Kaydet"))
        self.label.setText(_translate("Uzlasma", "Soruşturma No"))
        self.label_4.setText(_translate("Uzlasma", "Suç / Suçlar"))
        self.label_3.setText(_translate("Uzlasma", "Mahkeme Esas No"))
        self.label_6.setText(_translate("Uzlasma", "Taraf Sayısı"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Uzlasma = QtWidgets.QDialog()
    ui = Ui_Uzlasma()
    ui.setupUi(Uzlasma)
    Uzlasma.show()
    sys.exit(app.exec_())

