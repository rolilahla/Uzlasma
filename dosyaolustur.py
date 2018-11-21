# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dosyaolustur.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DosyaOlustur(object):
    def setupUi(self, DosyaOlustur):
        DosyaOlustur.setObjectName("DosyaOlustur")
        DosyaOlustur.resize(424, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/faenza-icon-theme-master/Faenza/apps/32/ubuntuone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DosyaOlustur.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(DosyaOlustur)
        self.label.setGeometry(QtCore.QRect(130, 10, 90, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(DosyaOlustur)
        self.lineEdit.setGeometry(QtCore.QRect(240, 10, 170, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(DosyaOlustur)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 40, 170, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(DosyaOlustur)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 90, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DosyaOlustur)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 90, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(DosyaOlustur)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 70, 170, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(DosyaOlustur)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 100, 170, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(DosyaOlustur)
        self.label_4.setGeometry(QtCore.QRect(130, 100, 90, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(DosyaOlustur)
        self.label_5.setGeometry(QtCore.QRect(130, 130, 90, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(DosyaOlustur)
        self.pushButton.setGeometry(QtCore.QRect(340, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(DosyaOlustur)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 121, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../Downloads/faenza-icon-theme-master/Faenza/apps/96/ubuntuone.png"))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(DosyaOlustur)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 130, 170, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(DosyaOlustur)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 160, 170, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(DosyaOlustur)
        self.label_7.setGeometry(QtCore.QRect(130, 160, 90, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(DosyaOlustur)
        self.label_8.setGeometry(QtCore.QRect(130, 190, 90, 20))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(DosyaOlustur)
        self.textEdit.setGeometry(QtCore.QRect(240, 190, 171, 81))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(DosyaOlustur)
        self.pushButton.clicked.connect(DosyaOlustur.close)
        QtCore.QMetaObject.connectSlotsByName(DosyaOlustur)

    def retranslateUi(self, DosyaOlustur):
        _translate = QtCore.QCoreApplication.translate
        DosyaOlustur.setWindowTitle(_translate("DosyaOlustur", "Dosya Oluştur"))
        self.label.setText(_translate("DosyaOlustur", "Soruşturma No"))
        self.label_2.setText(_translate("DosyaOlustur", "Uzlaşma No"))
        self.label_3.setText(_translate("DosyaOlustur", "Mahkeme Esas No"))
        self.label_4.setText(_translate("DosyaOlustur", "Suç / Suçlar"))
        self.label_5.setText(_translate("DosyaOlustur", "Teklif/Davet Tarihi"))
        self.pushButton.setText(_translate("DosyaOlustur", "Oluştur"))
        self.label_7.setText(_translate("DosyaOlustur", "Taraf Sayısı"))
        self.label_8.setText(_translate("DosyaOlustur", "Olay Özeti"))

