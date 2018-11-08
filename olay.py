# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'olay.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_olay(object):
    def setupUi(self, olay):
        olay.setObjectName("olay")
        olay.resize(506, 328)
        self.label_7 = QtWidgets.QLabel(olay)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(olay)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 10, 141, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(olay)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(olay)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 331, 221))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(olay)
        self.pushButton.setGeometry(QtCore.QRect(420, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(olay)
        self.label_9.setGeometry(QtCore.QRect(20, 40, 131, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(olay)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 40, 141, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(olay)
        self.pushButton.clicked.connect(olay.close)
        QtCore.QMetaObject.connectSlotsByName(olay)

    def retranslateUi(self, olay):
        _translate = QtCore.QCoreApplication.translate
        olay.setWindowTitle(_translate("olay", "Dialog"))
        self.label_7.setText(_translate("olay", "Soruşturma No"))
        self.label_8.setText(_translate("olay", "Olay Açıklaması"))
        self.pushButton.setText(_translate("olay", "Ekle"))
        self.label_9.setText(_translate("olay", "Olay Başlığı"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    olay = QtWidgets.QDialog()
    ui = Ui_olay()
    ui.setupUi(olay)
    olay.show()
    sys.exit(app.exec_())

